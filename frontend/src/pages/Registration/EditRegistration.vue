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
                  <h4 class="card-title">Editar Matrícula</h4>
                  </div>
                </div> 
               </template>
               <template slot="header">
                
                <form>
                <div class="form-group row">
                    <label for="reg_year" class="col-sm-5">Año de Matrícula</label>
                    <div class="col-sm-6">
                        <input  type="date" name="reg_year" id="reg_year"  v-model="registro.reg_year" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="reg_value" class="col-sm-5">Valor de Matrícula</label>
                    <div class="col-sm-6">
                        <input type="text" id="reg_value" name="reg_value"  v-model="registro.reg_value" required/>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="reg_course_type" class="col-sm-5">Curso</label>
                    <div class="col-sm-6">
                        <select class="form-select"  aria-label="Default select example" v-model="registro.reg_course_type.id" required>
                            <option selected disabled value=""></option>
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
                        <select class="form-select"  aria-label="Default select example" v-model="registro.reg_group_type.id" required>
                            <option selected disabled value=""></option>
                            <option value="47">01</option>
                            <option value="48">02</option>
                            <option value="49">03</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="student_history_type" class="col-sm-5">Historial de Estudiante</label>
                    <div class="col-sm-6">
                        <select class="form-select"  aria-label="Default select example" v-model="registro.student_history_type.id" required>
                            <option selected disabled value=""></option>
                            <option value="5">Antiguo</option>
                            <option value="6">Nuevo</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="school_level" class="col-sm-5">Nivel Escolar</label>
                    <div class="col-sm-6">
                        <select class="form-select"  aria-label="Default select example" v-model="registro.school_level.id" required>
                            <option selected disabled value=""></option>
                            <option value="8">Preescolar</option>
                            <option value="9">Primaria</option>
                        </select>
                    </div>
                </div>
              
                <div class="form-group row">
                    <label for="regist_status_type" class="col-sm-5">Estado de Matrícula</label>
                    <div class="col-sm-6">
                        <select class="form-select"  aria-label="Default select example" v-model="registro.regist_status_type.id" required>
                            <option selected disabled value=""></option>
                            <option value="11">Activo</option>
                            <option value="12">Inactivo</option>
                        </select>
                    </div>
                </div>
                <div class="form-group row">
                    <label for="stu_id" class="col-sm-5">Estudiante</label>
                    <div class="col-sm-6">
                        <input type="text" id="stu_id" name="stu_id"  v-model="registro.stu_id.id" required/>
                    </div>   
                </div>
              
                <button type="submit" class="btn btn-danger" v-on:click="guardar()">Guardar</button>
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
  import Card from 'src/components/Cards/Card.vue'

    export default {
    
    name:'EditRegistration',
    components: {
        Card
    },
    data(){
        return{
            datos: [],
            registro: {
                regisId: "",
                reg_year: "",
                reg_value: "",
                reg_course_type: "",
                reg_group_type: "",
                student_history_type: "",
                school_level: "",
                regist_status_type: "",
                stu_id: "",
            }
        
        }
    },
    methods:{
        async guardar(){
            const id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/Registration/' + id  + "/"
            console.log(this.registro)
            const response = await axios.put(path, {
                "reg_year": this.registro.reg_year,
                "reg_value": this.registro.reg_value,
                "reg_course_type": this.registro.reg_course_type.id,
                "reg_group_type": this.registro.reg_group_type.id,
                "student_history_type": this.registro.student_history_type.id,
                "school_level": this.registro.school_level.id,
                "regist_status_type": this.registro.regist_status_type.id,
                "stu_id": this.registro.stu_id.id,
            })
            
            console.log(response)
        }
    },

    async beforeMount(){
        const path = 'http://127.0.0.1:8000/api/Registration/'
        const response = await axios.get(path)
        const registro = response.data.filter(registro => registro.id == this.$route.params.id);
        this.$data.registro = registro[0];
        console.log(this.$data.registro)
      
    }
  
    }
  </script>
  <style lang="css" scoped>
  </style>
  








