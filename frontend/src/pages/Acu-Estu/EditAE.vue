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
                  <h4 class="card-title">Editar Relación de Acudiente con su estudiante</h4>
                  </div>
                </div>  
               </template>
               <template slot="header">
                
                <form>
                    <div class="form-group row">
                    <label class="col-sm-5">Estudiante</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.sa_stu_id.id" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Acudiente</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="registro.sa_att_id.id" required/>
                    </div>
                </div>
                
                <button type="submit" class="btn btn-danger" v-on:click="guardar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/acu_estu" size="sm" variant="dark">Ir al Listado</b-button>

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
  import Card from 'src/components/Cards/Card.vue';
  import Swal from 'sweetalert2';

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
                sa_stu_id:"",
                sa_att_id:"",    
            }
        
        }
    },
    methods:{
        async guardar(){
            const Swal = require('sweetalert2')
            const id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/Student_Attendant/' + id  + "/"
            console.log(this.registro)
            const response = await axios.put(path, {
                "sa_stu_id": this.registro.sa_stu_id.id,
                "sa_att_id": this.registro.sa_att_id.id,
                
            })
            Swal.fire({
                    // title: 'Matrícula Editada',
                    text: '¡Se ha editado correctamente!',
                    icon: 'success',
                    showConfirmButton: false,
                    timer: 3000
                    })
            console.log(response)
        }
    },

    async beforeMount(){
        const path = 'http://127.0.0.1:8000/api/Student_Attendant/'
        const response = await axios.get(path)
        const registro = response.data.filter(registro => registro.id == this.$route.params.id);
        this.$data.registro = registro[0];
        console.log(this.$data.registro)
      
    }
  
    }
  </script>
  <style lang="css" scoped>
  </style>
  








