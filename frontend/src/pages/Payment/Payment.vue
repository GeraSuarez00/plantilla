<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <card class="strpied-tabled-with-hover"
                body-classes="table-full-width table-responsive">
            <template slot="header">
              <div class="row">
                <div class="col-xl-6 col-md-6">
                <h4 class="card-title">Listado de Pagos </h4>
                </div>
                <div class="col-xl-3 col-md-3">
                  <b-button to="/admin/create-payment" size="sm" variant="danger">Agregar</b-button>
                </div>
              </div> 
             </template>
            <table class="table table-striped table-bordered table-hover">
             <thead class="table-danger">
                <tr class="table-danger">
                  <th>ID</th>
                  <th>Mes a pagar</th>
                  <th>Fecha de Pago</th>
                  <th>Valor a Pagar</th>
                  <th>Descuento</th>
                  <th>Valor total</th>
                  <th>Tipo de Pago</th>
                  <th>Concepto</th>
                  <th>Método de Pago</th>
                  <th>Matrícula del Estudiante</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody v-for="dato in datos">
                <tr  class="table-ligth">
                  <td>{{dato.id}}</td>
                  <td>{{dato.pay_month}}</td>
                  <td>{{dato.pay_date}}</td>
                  <td>{{dato.pay_value}}</td>
                  <td>{{dato.pay_discount}}</td>
                  <td>{{dato.pay_total_value}}</td>
                  <td>{{dato.payment_type.nombre}}</td>
                  <td>{{dato.item_type.nombre}}</td>
                  <td>{{dato.payment_method_type.nombre}}</td>
                  <td>{{dato.reg_id.nombre}} {{dato.reg_id.apellidos}}, {{dato.reg_id.identificación}}</td>
                  <td>
                    <!-- <button type="button" class="btn btn-primary" v-on:click="editar(dato.id)">
                          <i class="nc-icon nc-settings-tool-66 hidden-lg-up"></i>
                        &nbsp Editar
                        </button> -->
                  
                        &nbsp
                      <button type="button"  class="btn btn-danger" v-on:click="eliminar(dato.id)">
                        <i class="nc-icon nc-simple-remove hidden-lg-up"></i>
                        &nbsp Eliminar
                      </button>
                  </td>
                </tr>
              </tbody>
            </table>
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
    components: {
      Card
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
    data(){
      return{
        datos:[]
      }
    },
    methods:{
      // editar(id) {
      //   console.log(id)
      //   this.$router.push('create-ae/' + id);
      // },
      eliminar(id) {
        console.log(id)

          var op = window.confirm('¿Desea Eliminar el registro?')

          if (op){
          axios.delete("http://127.0.0.1:8000/api/Payment/" + id + "/").then(result => {
          this.mounted()
          console.log(result);
           })
       }
      },
    }
  }
</script>
<style lang="css" scoped>
</style>
