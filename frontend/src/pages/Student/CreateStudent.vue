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
                  <h4 class="card-title">Registro de Estudiante</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                <form>
                <div class="form-group row">
                    <label class="col-sm-5">Dirección</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="stu_address" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Estado</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="status_type" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="2">Activo</option>
                            <option value="3">Inactivo</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Nacionalidad</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="nationality_type" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="28">Colombiano</option>
                            <option value="29">Extranjero</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Persona</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="per_id" required/>
                    </div>
                </div>
                <button type="submit" class="btn btn-danger" v-on:click="agregar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/students"  variant="dark">Ir al Listado</b-button>
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
    
    name:'CreatePersons',
    components: {
        Card
    },
    data(){
        return{
        datos: null,
        id:"",
        stu_address:"",
        status_type:"",
        nationality_type:"",
        per_id:"",
        }
    },
    methods:{
        agregar(){
            let post = {
                "id":this.id,
                "stu_address":this.stu_address,
                "status_type":this.status_type,
                "nationality_type":this.nationality_type,
                "per_id":this.per_id,
            }
            axios.post('http://127.0.0.1:8000/api/Student/',post)
            .then(result => {
                this.id="";
                this.stu_address="";
                this.status_type="";
                this.nationality_type="";
                this.per_id="";
                this.updated()
                alert('Se ha agregado correctamente')
                console.log(result)
            })
            .catch((error) => {
            console.log(error)
        })
        
        },
        updated() {
          let direccion = "http://127.0.0.1:8000/api/Student/";
          axios.get(direccion).then(response => {
            this.datos = response.data
          })
        }
    },
    mounted() {
        const path = 'http://127.0.0.1:8000/api/Student/'
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
  