<template>
    <div class="content">
      <div class="container-fluid">
        <div class="row">
            <div class="col-2">
            </div>  
          <div class="col-8">
            <card class="strpied-tabled-with-hover"
                  body-classes="table-full-width table-responsive">
              <template slot="header">
                
                <div class="row">
                  <div class="col-8">
                  <h4 class="card-title">Registrar Pagos</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                <form>
                <div class="form-group row">
                    <label class="col-sm-5">Mes a pagar</label>
                    <div class="col-sm-6">
                        <select class="form-select" multiple v-model="pay_month" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="Febrero">Febrero</option>
                            <option value="Marzo">Marzo</option>
                            <option value="Abril">Abril</option>
                            <option value="Mayo">Mayo</option>
                            <option value="Junio">Junio</option>
                            <option value="Julio">Julio</option>
                            <option value="Agosto">Agosto</option>
                            <option value="Septiembre">Septiembre</option>
                            <option value="Octubre">Octubre</option>
                            <option value="Noviembre">Noviembre</option>
                        </select>   
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Fecha de Pago</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="date" v-model="pay_date" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Valor a Pagar</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="pay_value" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Descuento</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="pay_discount" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Valor Total</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="pay_total_value" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Tipo de Pago</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="payment_type" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="14">Total</option>
                            <option value="15">Parcial</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Concepto</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="item_type" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="17">Pensión</option>
                            <option value="18">Matrícula</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Método de Pago</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="payment_method_type" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="20">Efectivo</option>
                            <option value="21">Nequi</option>
                            <option value="22">Daviplata</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Matrícula del estudiante</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="reg_id" required/>
                    </div>
                </div>
                
                <button type="submit" class="btn btn-danger" v-on:click="agregar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/payment" size="sm" variant="dark">Ir al Listado</b-button>
               </form>
            </template>
    
            </card>
  
          </div>
  
        </div>
      </div>
    </div>
  </template>
  <script>
  import axios from 'axios';
  import Card from 'src/components/Cards/Card.vue'

    export default {
    
    name:'CreatePayment',
    components: {
        Card
    },
    data(){
        return{
        datos: null,
        id:"",
        pay_month:[],
        pay_date:"",
        pay_value:"",
        pay_discount:"",
        pay_total_value:"",
        payment_type:"",
        item_type:"",
        payment_method_type:"",
        reg_id:"",
        }
    },
    methods:{
        agregar(){
            let post = {
                "id":this.id,
                "pay_month":this.pay_month,
                "pay_date":this.pay_date,
                "pay_value":this.pay_value,
                "pay_discount":this.pay_discount,
                "pay_total_value":this.pay_total_value,
                "payment_type":this.payment_type,
                "item_type":this.item_type,
                "payment_method_type":this.payment_method_type,
                "reg_id":this.reg_id,
            }
            axios.post('http://127.0.0.1:8000/api/Payment/',post)
            .then(result => {
                this.id="";
                this.pay_month="";
                this.pay_date="";
                this.pay_value="";
                this.pay_discount="";
                this.pay_total_value="";
                this.payment_type="";
                this.item_type="";
                this.payment_method_type="";
                this.reg_id="";
                this.updated()
                alert('Se ha agregado correctamente')
                console.log(result)
            })
            .catch((error) => {
            console.log(error)
        })
        },
        updated() {
          let direccion = "http://127.0.0.1:8000/api/Payment/";
          axios.get(direccion).then(response => {
            this.datos = response.data
          })
        }
    },
    mounted() {
        const path = 'http://127.0.0.1:8000/api/Payment/'
        axios.get(path).then((response) => {
            this.datos = response.data
            console.log(this.datos);
        })
        .catch((error) => {
            console.log(error)
        })
      },
    }
  </script>
  <style lang="css" scoped>
  </style>
  