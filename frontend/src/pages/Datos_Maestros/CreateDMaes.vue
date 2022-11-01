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
                  <h4 class="card-title">Crear un Dato Maestro</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                <form>
                <div class="form-group row">
                    <label  class="col-sm-5">Nombre</label>
                    <div class="col-sm-6">
                        <input  type="text" v-model="maes_names" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Valor</label>
                    <div class="col-sm-6">
                        <input type="text"  v-model="maes_value" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Dependencia</label>
                    <div class="col-sm-6">
                        <input type="text"  v-model="maes_dependency" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Estado</label>
                    <div class="col-sm-6">
                        <input type="text"  v-model="maes_status_type" required/>
                    </div>
                </div>
               
                <button type="submit" class="btn btn-danger" v-on:click="agregar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/ajustes" size="sm" variant="dark">Ir al Listado</b-button>
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
    
    name:'CreateDMaes',
    components: {
        Card
    },
    data(){
        return{
        datos: null,
        id:"",
        maes_names:"",
        maes_value:"",
        maes_dependency:"",
        maes_status_type:"",
        }
    },
    methods:{
        agregar(){
            const Swal = require('sweetalert2')
            let post = {
                "id":this.id,
                "maes_names":this.maes_names,
                "maes_value":this.maes_value,
                "maes_dependency":this.maes_dependency,
                "maes_status_type":this.maes_status_type,
            }
            axios.post('http://127.0.0.1:8000/api/DatosMaestros/',post)
            .then(result => {
                this.id="";
                this.maes_names="";
                this.maes_value="";
                this.maes_dependency="";
                this.maes_status_type="";
                Swal.fire({
                    title: 'Dato Maestro Agregado',
                    text: '¡Se ha creado correctamente!',
                    icon: 'success',
                    showConfirmButton: false,
                    timer: 8000
                    })
                
                console.log(result)
            })
            .catch((error) => {
            console.log(error)
        })
        },
        
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
    }
  </script>
  <style lang="css" scoped>
  </style>
  