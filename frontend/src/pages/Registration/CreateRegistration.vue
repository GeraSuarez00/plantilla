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
                  <h4 class="card-title">Crear Matrícula</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                <form>
                <div class="form-group row">
                    <label for="reg_year" class="col-sm-5">Año de Matrícula</label>
                    <div class="col-sm-6">
                        <input  type="date" name="reg_year" id="reg_year" v-model="reg_year" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="reg_value" class="col-sm-5">Valor de Matrícula</label>
                    <div class="col-sm-6">
                        <input type="text" id="reg_value" name="reg_value" v-model="reg_value" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="reg_course_type" class="col-sm-5">Curso</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="reg_course_type" aria-label="Default select example" required>
                            <option selected disabled value="">Escoja una opción</option>
                            <option value="38">pre-jardín</option>
                            <option value="39">Jardín</option>
                            <option value="40">Transición</option>
                            <option value="41">Primero</option>
                            <option value="42">Segundo</option>
                            <option value="43">Tercero</option>
                            <option value="44">Cuarto</option>
                            <option value="45">Quinto</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="reg_group_type" class="col-sm-5">Grupo</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="reg_group_type" aria-label="Default select example" required>
                            <option selected disabled value="">Escoja una opción</option>
                            <option value="47">01</option>
                            <option value="48">02</option>
                            <option value="49">03</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="student_history_type" class="col-sm-5">Historial de Estudiante</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="student_history_type" aria-label="Default select example" required>
                            <option selected disabled value="">Escoja una opción</option>
                            <option value="5">Antiguo</option>
                            <option value="6">Nuevo</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="school_level" class="col-sm-5">Nivel Escolar</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="school_level" aria-label="Default select example" required>
                            <option selected disabled value="">Escoja una opción</option>
                            <option value="8">Preescolar</option>
                            <option value="9">Primaria</option>
                        </select>
                    </div>
                </div>
              
                <!-- <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Estado de Matrícula</label>
                    <div class="col-sm-6">
                        <select class="form-select" v-model="regist_status_type" aria-label="Default select example" required>
                            <option selected disabled value="">Escoja una opción</option>
                            <option value="11">Activo</option>
                            <option value="12">Inactivo</option>
                        </select>
                    </div>
                </div> -->
                <div class="form-group row">
                    <label for="stu_id" class="col-sm-5">Estudiante</label>
                    <div class="col-sm-6">
                        <input type="text" id="stu_id" name="stu_id" v-model="stu_id" required/>
                    </div>   
                </div>
              
                <button type="submit" class="btn btn-danger" v-on:click="agregar()">Guardar</button>
                &nbsp &nbsp <b-button to="/admin/registration" size="sm" variant="dark">Ir al Listado</b-button>
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
   

    export default {
    
    name:'CreateRegistration',
    components: {
        Card
    },
    data(){
        return{
        datos: null,
        id:"",
        reg_year:"",
        reg_value:"",
        reg_course_type:"",
        reg_group_type:"",
        student_history_type:"",
        school_level:"",
        regist_status_type:"11",
        stu_id:"",
        }
    },
    methods:{
        agregar(){
            const Swal = require('sweetalert2')
            let post = {
                "id":this.id,
                "reg_year":this.reg_year,
                "reg_value":this.reg_value,
                "reg_course_type":this.reg_course_type,
                "reg_group_type":this.reg_group_type,
                "student_history_type":this.student_history_type,
                "school_level":this.school_level,
                "regist_status_type":this.regist_status_type,
                "stu_id": this.stu_id,
            }
            axios.post('http://127.0.0.1:8000/api/Registration/',post)
            .then(result => {
                this.id="";
                this.reg_year="";
                this.reg_value="";
                this.reg_course_type="";
                this.reg_group_type="";
                this.student_history_type="";
                this.school_level="";
                this.regist_status_type="";
                this.stu_id="";
                Swal.fire({
                    title: 'Matrícula Agregada',
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
        const path = 'http://127.0.0.1:8000/api/Registration/'
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
  