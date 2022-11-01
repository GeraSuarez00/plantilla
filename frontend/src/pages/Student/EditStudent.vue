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
                  <h4 class="card-title">Editar Estudiante</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                
                <form>
                    <div class="form-group row">
                    <label class="col-sm-5">Dirección</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.stu_address" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Estado</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="registro.status_type.id" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="2">Activo</option>
                            <option value="3">Inactivo</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Nacionalidad</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="registro.nationality_type.id" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="28">Colombiano</option>
                            <option value="29">Extranjero</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Persona</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.per_id.id" required/>
                    </div>
                </div>

                <button type="submit" class="btn btn-danger" v-on:click="guardar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/students" size="sm" variant="dark">Ir al Listado</b-button>
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
    
    name:'EditStudent',
    components: {
        Card
    },
    data(){
        return{
            datos: [],
            registro: {
                id:"",
                stu_address: "",
                status_type: "",
                nationality_type: "",
                per_id: "", 
            }
        
        }
    },
    methods:{
        async guardar(){
            const Swal = require('sweetalert2')
            const id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/Student/' + id  + "/"
            console.log(this.registro)
            const response = await axios.put(path, {
                "stu_address": this.registro.stu_address,
                "status_type": this.registro.status_type.id,
                "nationality_type": this.registro.nationality_type.id,
                "per_id": this.registro.per_id.id,
                
            })
            Swal.fire({
                    title: 'Estudiante Editado',
                    text: '¡Se ha editado correctamente!',
                    icon: 'success',
                    showConfirmButton: false,
                    timer: 3000
                    })
            console.log(response)
        }
    },

    async beforeMount(){
        const path = 'http://127.0.0.1:8000/api/Student/'
        const response = await axios.get(path)
        const registro = response.data.filter(registro => registro.id == this.$route.params.id);
        this.$data.registro = registro[0];
        console.log(this.$data.registro)
      
    }
  
    }
  </script>
  <style lang="css" scoped>
  </style>
  








