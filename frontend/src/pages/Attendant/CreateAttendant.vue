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
                  <h4 class="card-title">Registro de Acudientes</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                
                <form >
                  <div class="form-group row">
                    <label class="col-sm-5">Ocupación</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="att_ocupation" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Compañía</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="att_company" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Número de Teléfono de la Oficina</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="att_office_phone" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Tipo de Parentesco</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="kinship_type" aria-label="Default select example" required>
                            <option selected disabled value=""></option>
                            <option value="31">Padre</option>
                            <option value="32">Madre</option>
                            <option value="33">Tío (a)</option>
                            <option value="34">Hermano (a)</option>
                            <option value="35">Abuelo (a)</option>
                            <option value="36">Primo (a)</option>
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
                &nbsp &nbsp <b-button to="/admin/attendant"  variant="dark">Ir al Listado</b-button>
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
        att_ocupation:"",
        att_company:"",
        att_office_phone:"",
        kinship_type:"",
        per_id:"",
        }
    },
    methods:{
        agregar(){
            let post = {
                "id":this.id,
                "att_ocupation":this.att_ocupation,
                "att_company":this.att_company,
                "att_office_phone":this.att_office_phone,
                "kinship_type":this.kinship_type,
                "per_id":this.per_id,
            }
            axios.post('http://127.0.0.1:8000/api/Attendant/',post)
            .then(result => {
                this.id="";
                this.att_ocupation="";
                this.att_company="";
                this.att_office_phone="";
                this.kinship_type="";
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
          let direccion = "http://127.0.0.1:8000/api/Attendant/";
          axios.get(direccion).then(response => {
            this.datos = response.data
          })
        }
    },
    // mounted() {
    //     const path = 'http://127.0.0.1:8000/api/Attendant/'
    //     axios.get(path).then((response) => {
    //         this.datos = response.data
    //         console.log(this.datos);
    //     })
    //     .catch((error) => {
    //         console.log(error)
    //     })
    //   },
    }
  </script>
  <style lang="css" scoped>
  </style>
  