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
                  <h4 class="card-title">Editar Datos Maestros</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                
                <form>
                    <div class="form-group row">
                    <label  class="col-sm-5">Nombre</label>
                    <div class="col-sm-6">
                        <input  type="text" v-model="registro.maes_names" required/>
                    </div>
                    </div>
                    <div class="form-group row">
                        <label class="col-sm-5">Valor</label>
                        <div class="col-sm-6">
                            <input type="text"  v-model="registro.maes_value" required/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label class="col-sm-5">Dependencia</label>
                        <div class="col-sm-6">
                            <input type="number"  v-model="registro.maes_dependency" required/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label class="col-sm-5">Estado</label>
                        <div class="col-sm-6">
                            <input type="number"  v-model="registro.maes_status_type" required/>
                        </div>
                    </div>

                    <button type="submit" class="btn btn-danger" v-on:click="guardar()">Guardar</button>
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
    
    name:'EditStudent',
    components: {
        Card
    },
    data(){
        return{
            datos: [],
            registro: {
                id:"",
                maes_names:"",
                maes_value:"",
                maes_dependency:"",
                maes_status_type:"",
               
            }
        
        }
    },
    methods:{
        async guardar(){
            const Swal = require('sweetalert2')
            const id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/DatosMaestros/' + id  + "/"
            console.log(this.registro)
            const response = await axios.put(path, {
                "maes_names": this.registro.maes_names,
                "maes_value": this.registro.maes_value,
                "maes_dependency": this.registro.maes_dependency,
                "maes_status_type": this.registro.maes_status_type,
                
            })
            Swal.fire({
                    title: 'Dato Maestro Editado',
                    text: '¡Se ha editado correctamente!',
                    icon: 'success',
                    showConfirmButton: false,
                    timer: 3000
                    })
            console.log(response)
        }
    },

    async beforeMount(){
        const path = 'http://127.0.0.1:8000/api/DatosMaestros/'
        const response = await axios.get(path)
        const registro = response.data.filter(registro => registro.id == this.$route.params.id);
        this.$data.registro = registro[0];
        console.log(this.$data.registro)
      
    }
  
    }
  </script>
  <style lang="css" scoped>
  </style>
  








