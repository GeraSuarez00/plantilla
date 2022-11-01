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
                  <h4 class="card-title">Editar Persona</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                
                <form>
                <div class="form-group row">
                <label class="col-sm-5">Nombres</label>
                <div class="col-sm-6">
                    <input  class="form-control" type="text" v-model="registro.per_names" required/>
                </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Apellidos</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.per_surnames" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Tipo de Identificación</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="registro.per_identification_type.id" aria-label="Default select example" required>
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
                        <input  class="form-control" type="text" v-model="registro.per_identity_number" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Fecha de Nacimiento</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="date" v-model="registro.per_birth_date" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Número de teléfono personal</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.per_personal_phone" required/>
                    </div>
                </div>
                
                <button type="submit" class="btn btn-danger" v-on:click="guardar()">Guardar</button>
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
    
    name:'EditPersona',
    components: {
        Card
    },
    data(){
        return{
            datos: [],
            registro: {
                id: "",
                per_names: "",
                per_surnames: "",
                per_identification_type: "",
                per_identity_number: "",
                per_birth_date: "",
                per_personal_phone: "",
    
            }
        
        }
    },
    methods:{
        async guardar(){
            const Swal = require('sweetalert2')
            const id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/Person/' + id  + "/"
            console.log(this.registro)
            const response = await axios.put(path, {
                "per_names": this.registro.per_names,
                "per_surnames": this.registro.per_surnames,
                "per_identification_type": this.registro.per_identification_type.id,
                "per_identity_number": this.registro.per_identity_number,
                "per_birth_date": this.registro.per_birth_date,
                "per_personal_phone": this.registro.per_personal_phone,
            })
            Swal.fire({
                    title: 'Persona Editada',
                    text: '¡Se ha editado correctamente!',
                    icon: 'success',
                    showConfirmButton: false,
                    timer: 3000
                    })
            
            console.log(response)
        }
    },

    async beforeMount(){
        const path = 'http://127.0.0.1:8000/api/Person/'
        const response = await axios.get(path)
        const registro = response.data.filter(registro => registro.id == this.$route.params.id);
        this.$data.registro = registro[0];
        console.log(this.$data.registro)
      
    }
  
    }
  </script>
  <style lang="css" scoped>
  </style>
  








