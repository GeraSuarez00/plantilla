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
                  <h4 class="card-title">Registro de Acudientes con su Estudiante</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                <form>
                <div class="form-group row">
                    <label class="col-sm-5">Estudiante</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="sa_stu_id" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label class="col-sm-5">Acudiente</label>
                    <div class="col-sm-6">
                        <input  class="form-control" type="text" v-model="sa_att_id" required/>
                    </div>
                </div>
                <button type="submit" class="btn btn-danger" v-on:click="agregar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/acu_estu"  variant="dark">Ir al Listado</b-button>
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
    
    name:'CreatePersons',
    components: {
        Card
    },
    data(){
        return{
        datos: null,
        id:"",
        sa_stu_id:"",
        sa_att_id:"",
        }
    },
    methods:{
        agregar(){
            const Swal = require('sweetalert2')
            let post = {
                "id":this.id,
                "sa_stu_id":this.sa_stu_id,
                "sa_att_id":this.sa_att_id,
            }
            axios.post('http://127.0.0.1:8000/api/Student_Attendant/',post)
            .then(result => {
                this.id="";
                this.sa_stu_id="";
                this.sa_att_id="";
                Swal.fire({
                    title: 'Elemento de Acudiente-Estudiante Agregado',
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
        const path = 'http://127.0.0.1:8000/api/Student_Attendant/'
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
  