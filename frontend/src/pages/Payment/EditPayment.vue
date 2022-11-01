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
                  <h4 class="card-title">Editar Pagos</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                
                <form>
                    <div class="form-group row">
                    <label class="col-sm-5">Mes a pagar</label>
                    <div class="col-sm-6">
                        <select class="form-select" multiple v-model="registro.pay_month" aria-label="Default select example" required>
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
                        <input  class="form-control" type="date" v-model="registro.pay_date" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Valor a Pagar</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.pay_value" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Descuento</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.pay_discount" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Valor Total</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.pay_total_value" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Tipo de Pago</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="registro.payment_type.id" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="14">Total</option>
                            <option value="15">Parcial</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Concepto</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="registro.item_type.id" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="17">Pensión</option>
                            <option value="18">Matrícula</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Método de Pago</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="registro.payment_method_type.id" aria-label="Default select example" required>
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
                        <input  class="form-control" type="text" v-model="registro.reg_id.id" required/>
                    </div>
                </div>
                
              
                <button type="submit" class="btn btn-danger" v-on:click="guardar()">Guardar</button>
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
    
    name:'EditPayment',
    components: {
        Card
    },
    data(){
        return{
            datos: [],
            registro: {
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
        
        }
    },
    methods:{
        async guardar(){
            const Swal = require('sweetalert2')
            const id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/Payment/' + id  + "/"
            console.log(this.registro)
            const response = await axios.put(path, {
                "pay_month": this.registro.pay_month,
                "pay_date": this.registro.pay_date,
                "pay_value": this.registro.pay_value,
                "pay_discount": this.registro.pay_discount,
                "pay_total_value": this.registro.pay_total_value,
                "payment_type": this.registro.payment_type.id,
                "item_type": this.registro.item_type.id,
                "payment_method_type": this.registro.payment_method_type.id,
                "reg_id": this.registro.reg_id.id,
            })
            Swal.fire({
                    title: 'Pago Editado',
                    text: '¡Se ha editado correctamente!',
                    icon: 'success',
                    showConfirmButton: false,
                    timer: 3000
                    })
            console.log(response)
        }
    },

    async beforeMount(){
        const path = 'http://127.0.0.1:8000/api/Payment/'
        const response = await axios.get(path)
        const registro = response.data.filter(registro => registro.id == this.$route.params.id);
        this.$data.registro = registro[0];
        console.log(this.$data.registro)
      
    }
  
    }
  </script>
  <style lang="css" scoped>
  </style>
  








