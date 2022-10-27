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
                <h4 class="card-title">Listado de Datos Maestros </h4>
                </div>
                <div class="col-xl-3 col-md-3">
                  <b-button to="/admin/create-dm" size="sm" variant="danger">Agregar</b-button>
                </div>
              </div> 
           
            </template>
            <table class="table table-striped table-bordered table-hover">
             <thead class="table-dark">
                <tr class="bg-dark">
                  <td>ID</td>
                  <td>Nombre</td>
                  <td>Valor</td>
                  <td>Dependencia</td>
                  <td>Estado</td>
                  <!-- <td>Acciones</td> -->
                </tr>
              </thead>
              <tbody v-for="dato in datos">
                <tr  class="table-ligth">
                  <td>{{dato.id}}</td>
                  <td>{{dato.maes_names}}</td>
                  <td>{{dato.maes_value}}</td>
                  <td>{{dato.maes_dependency}}</td>
                  <td>{{dato.maes_status_type}}</td>
                  <!-- <td>
                    <a href="#" class="btn btn-secondary btn-sm">
                      <i class="nc-icon nc-settings-tool-66 hidden-lg-up"></i>
                      &nbsp Editar
                    </a>
                    &nbsp
                  </td> -->
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
        const path = 'http://127.0.0.1:8000/api/DatosMaestros/'
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
    }
  }
</script>
<style lang="css" scoped>
</style>

