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
                <h4 class="card-title">Listado de Matrículas </h4>
                </div>
                <div class="col-xl-3 col-md-3">
                  <b-button to="/admin/create-registration" size="sm" variant="danger">Agregar</b-button>
                </div>
              </div> 
           
            </template>
             
           
            <table v-if="datos" class="table table-striped table-bordered table-hover">
             <thead class="table-danger">
                <tr class="table-danger">
                  <th>ID</th>
                  <th>Año</th>
                  <th>Valor</th>
                  <th>Curso</th>
                  <th>Grupo</th>
                  <th>Historial de estudiante</th>
                  <th>Nivel Escolar</th>
                  <th>Estado de Matrícula</th>
                  <th>Estudiante</th>
                  <th>Acciones</th>
                </tr>
              </thead>
              <tbody v-for="dato in datos" :key="dato.id">
                <tr  class="table-ligth">
                  <td>{{dato.id}}</td>
                  <td>{{dato.reg_year}}</td>
                  <td>{{dato.reg_value}}</td>
                  <td>{{dato.reg_course_type.nombre}}</td>
                  <td>{{dato.reg_group_type.nombre}}</td>
                  <td>{{dato.student_history_type.nombre}}</td>
                  <td>{{dato.school_level.nombre}}</td>
                  <td>{{dato.regist_status_type.nombre}}</td>
                  <td>{{dato.stu_id.nombre}} {{dato.stu_id.apellidos}}-{{dato.stu_id.identificación}}</td>
                  <td>
                    <button type="button" class="btn btn-secondary" v-on:click="editar(dato.id)">
                          <i class="nc-icon nc-settings-tool-66 hidden-lg-up"></i>
                        &nbsp Editar
                        </button>
                  
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
        const path = 'http://127.0.0.1:8000/api/Registration/'
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
      editar(id) {
        console.log(id)
        this.$router.push('edit-registration/' + id);
      },
      eliminar(id) {
          var op = window.confirm('¿Desea Eliminar el registro?')

          if (op){
          axios.delete("http://127.0.0.1:8000/api/Registration/" + id + "/").then(result => {
        
          console.log(result);
          window.location.reload();
          
           })
       }
      },
    }
  }
</script>
<style lang="css" scoped>
</style>
