import DashboardLayout from '../layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../pages/NotFoundPage.vue'

// Admin pages
import Overview from 'src/pages/Overview.vue'

import Payment from 'src/pages/Payment/Payment.vue'
import CreatePayment from 'src/pages/Payment/CreatePayment.vue'
import EditPayment from 'src/pages/Payment/EditPayment.vue'

import Registration from 'src/pages/Registration/Registration.vue'
import CreateRegistration from 'src/pages/Registration/CreateRegistration.vue'
import EditRegistration from 'src/pages/Registration/EditRegistration.vue'

import Icons from 'src/pages/Icons.vue'
import Notifications from 'src/pages/Notifications.vue'

import Datos_Maestros from 'src/pages/Datos_Maestros/Datos_Maestros.vue'
import CreateDMaes from 'src/pages/Datos_Maestros/CreateDMaes.vue'
import EditDM from 'src/pages/Datos_Maestros/EditDM.vue'

import Students from 'src/pages/Student/Students.vue'
import CreateStudent from 'src/pages/Student/CreateStudent.vue'
import EditStudent from 'src/pages/Student/EditStudent.vue'

import Attendant from 'src/pages/Attendant/Attendant.vue'
import CreateAttendant from 'src/pages/Attendant/CreateAttendant.vue'
import EditAttendant from 'src/pages/Attendant/EditAttendant.vue'

import Persons from 'src/pages/Persons/Persons.vue'
import CreatePersons from 'src/pages/Persons/CreatePersons.vue'
import EditPersona from 'src/pages/Persons/EditPersona.vue'


import acu_estu from 'src/pages/Acu-Estu/Acu-Estu.vue'
import CreateAE from 'src/pages/Acu-Estu/CreateAE.vue'
import EditAE from 'src/pages/Acu-Estu/EditAE.vue'



const routes = [
  {
    path: '/',
    component: DashboardLayout,
    redirect: '/admin/overview'
  },
  {
    path: '/admin',
    component: DashboardLayout,
    redirect: '/admin/overview',
    children: [
      {
        path: 'overview',
        name: 'Overview',
        component: Overview
      },
      {
        path: 'students',
        name: 'Students',
        component: Students
      },
      {
        path: 'create-student',
        name: 'CreateStudent',
        component: CreateStudent
      },
      {
        path: 'edit-student/:id',
        name: 'EditStudent',
        component: EditStudent
      },
      {
        path: 'attendant',
        name: 'Attendant',
        component: Attendant
      },
      {
        path: 'create-attendant',
        name: 'CreateAttendant',
        component: CreateAttendant
      },
      {
        path: 'edit-attendant/:id',
        name: 'EditAttendant',
        component: EditAttendant
      },
      {
        path: 'persons',
        name: 'Persons',
        component: Persons
      },
      {
        path: 'edit-persona/:id',
        name: 'EditPersona',
        component: EditPersona
      },
      {
        path: 'create-person',
        name: 'CreatePerson',
        component: CreatePersons,
      },
      {
        path: 'acu_estu',
        name: 'acu_estu',
        component: acu_estu
      },
      {
        path: 'create-ae',
        name: 'CreateAE',
        component: CreateAE
      },
      {
        path: 'edit-ae/:id',
        name: 'EditAE',
        component: EditAE
      },
      {
        path: 'payment',
        name: 'Payment',
        component: Payment
      },
      {
        path: 'create-payment',
        name: 'CreatePayment',
        component: CreatePayment,
      },
      {
        path: 'edit-payment/:id',
        name: 'EditPayment',
        component: EditPayment
      },
      {
        path: 'registration',
        name: 'Registration',
        component: Registration,      
      },
      {
        path: 'create-registration',
        name: 'CreateRegistration',
        component: CreateRegistration
      },
      {
        path: 'edit-registration/:id',
        name: 'EditRegistration',
        component: EditRegistration
      },
      {
        path: 'icons',
        name: 'Icons',
        component: Icons
      },
      {
        path: 'notifications',
        name: 'Notifications',
        component: Notifications
      },
      {
        path: 'ajustes',
        name: 'Datos_Maestros',
        component: Datos_Maestros
      },
      {
        path: 'edit-dm/:id',
        name: 'EditDM',
        component: EditDM
      },
      {
        path: 'create-dm',
        name: 'CreateDMaes',
        component: CreateDMaes
      }
    ]
  },
  { path: '*', component: NotFound }
]

/**
 * Asynchronously load view (Webpack Lazy loading compatible)
 * The specified component must be inside the Views folder
 * @param  {string} name  the filename (basename) of the view to load.
function view(name) {
   var res= require('../components/Dashboard/Views/' + name + '.vue');
   return res;
};**/

export default routes
