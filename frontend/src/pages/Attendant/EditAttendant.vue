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
                  <h4 class="card-title">Editar Acudiente</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                
                <form>
                   
                <div class="form-group row">
                <label class="col-sm-5">Ocupación</label>
                <div class="col-sm-6">
                    <input  class="form-control" type="text" v-model="registro.att_ocupation" required/>
                </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Compañía</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.att_company" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Número de Teléfono de la Oficina</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.att_office_phone" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Tipo de Parentesco</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="registro.kinship_type.id" aria-label="Default select example" required>
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
                        <input  class="form-control" type="text" v-model="registro.per_id.id" required/>
                    </div>
                </div>
                <button type="submit" class="btn btn-danger" v-on:click="guardar()">Guardar</button>
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
    
    name:'EditAttendant',
    components: {
        Card
    },
    data(){
        return{
            datos: [],
            registro: {
                id: '',
                att_ocupation: '',
                att_company: '',
                att_office_phone: '',
                kinship_type: '',
                per_id: '',
 
            }
        
        }
    },
    methods:{
        async guardar(){
            const Swal = require('sweetalert2')
            const id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/Attendant/' + id  + "/"
            console.log(this.registro)
            const response = await axios.put(path, {
                "att_ocupation": this.registro.att_ocupation,
                "att_company": this.registro.att_company,
                "att_office_phone": this.registro.att_office_phone,
                "kinship_type": this.registro.kinship_type.id,
                "per_id": this.registro.per_id.id,    
            })
            Swal.fire({
                    title: 'Acudiente Editado',
                    text: '¡Se ha editado correctamente!',
                    icon: 'success',
                    showConfirmButton: false,
                    timer: 3000
                    })
            console.log(response)
        }
    },

    async beforeMount(){
        const path = 'http://127.0.0.1:8000/api/Attendant/'
        const response = await axios.get(path)
        const registro = response.data.filter(registro => registro.id == this.$route.params.id);
        this.$data.registro = registro[0];
        console.log(this.$data.registro)
      
    }
  
    }
  </script>
  <style lang="css" scoped>
  </style>
  








