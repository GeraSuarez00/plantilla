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
                  <h4 class="card-title">Registro de Persona</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                <form>
                <div class="form-group row">
                    <label class="col-sm-5">Nombres</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="per_names" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Apellidos</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="per_surnames" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Tipo de Identificación</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="per_identification_type" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="24">Cédula de Ciudadanía</option>
                            <option value="25">Tarjeta de Identidad</option>
                            <option value="26">Registro Civil de Nacimiento</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Número de Identificación</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="per_identity_number" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Fecha de Nacimiento</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="date" v-model="per_birth_date" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Número de teléfono personal</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="per_personal_phone" required/>
                    </div>
                </div>
                
                <button type="submit" class="btn btn-danger" v-on:click="agregar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/persons" size="sm" variant="dark">Ir al Listado</b-button>
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
        per_names:"",
        per_surnames:"",
        per_identification_type:"",
        per_identity_number:"",
        per_birth_date:"",
        per_personal_phone:"",
        }
    },
    methods:{
        agregar(){
            let post = {
                "id":this.id,
                "per_names":this.per_names,
                "per_surnames":this.per_surnames,
                "per_identification_type":this.per_identification_type,
                "per_identity_number":this.per_identity_number,
                "per_birth_date":this.per_birth_date,
                "per_personal_phone":this.per_personal_phone,
            }
            axios.post('http://127.0.0.1:8000/api/Person/',post)
            .then(result => {
                this.id="";
                this.per_names="";
                this.per_surnames="";
                this.per_identification_type="";
                this.per_identity_number="";
                this.per_birth_date="";
                this.per_personal_phone="";
                this.updated()
                alert('Se ha agregado correctamente')
                console.log(result)
            })
            .catch((error) => {
            console.log(error)
        })
        },
        updated() {
          let direccion = "http://127.0.0.1:8000/api/Person/";
          axios.get(direccion).then(response => {
            this.datos = response.data
          })
        }
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
    }
  </script>
  <style lang="css" scoped>
  </style>
  