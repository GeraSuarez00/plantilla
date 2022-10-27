<template>
    <div class="content">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">
            <card class="strpied-tabled-with-hover"
                  body-classes="table-full-width table-responsive">
              <template slot="header">
                  
              <div class="row">
                <div class="col-xl-3 col-md-6">
                <h4 class="card-title">Listado de Personas</h4>
                </div>
                <div class="col-xl-3 col-md-3">
                  <b-button to="/admin/create-person" size="sm" variant="danger">Agregar</b-button>
                </div>
              </div> 
           
              </template>
              <table class="table table-striped table-bordered table-hover">
               <thead class="table-danger">
                  <tr class="table-danger">
                    <th>ID</th>
                    <th>Nombres</th>
                    <th>Apellidos</th>
                    <th>Tipo de identificación</th>
                    <th>Número de identificación</th>
                    <th>Fecha de Nacimiento</th>
                    <th>Número de teléfono personal</th>
                    <th>Acciones</th>
                  </tr>
                </thead>
                <tbody v-for="dato in datos">
                  <tr  class="table-ligth">
                    <td>{{dato.id}}</td>
                    <td>{{dato.per_names}}</td>
                    <td>{{dato.per_surnames}}</td>
                    <td>{{dato.per_identification_type}}</td>
                    <td>{{dato.per_identity_number}}</td>
                    <td>{{dato.per_birth_date}}</td>
                    <td>{{dato.per_personal_phone}}</td>
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
          const path = 'http://127.0.0.1:8000/api/Person/'
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
          axios.delete("http://127.0.0.1:8000/api/Person/" + id + "/").then(result => {
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
  
  