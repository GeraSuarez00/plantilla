import DashboardLayout from '../layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../pages/NotFoundPage.vue'

// Admin pages
import Overview from 'src/pages/Overview.vue'

import Payment from 'src/pages/Payment/Payment.vue'
import CreatePayment from 'src/pages/Payment/CreatePayment.vue'

import Registration from 'src/pages/Registration/Registration.vue'
import CreateRegistration from 'src/pages/Registration/CreateRegistration.vue'

import Icons from 'src/pages/Icons.vue'
import Notifications from 'src/pages/Notifications.vue'

import Datos_Maestros from 'src/pages/Datos_Maestros/Datos_Maestros.vue'
import CreateDMaes from 'src/pages/Datos_Maestros/CreateDMaes.vue'

import Students from 'src/pages/Student/Students.vue'
import CreateStudent from 'src/pages/Student/CreateStudent.vue'

import Attendant from 'src/pages/Attendant/Attendant.vue'
import CreateAttendant from 'src/pages/Attendant/CreateAttendant.vue'

import Persons from 'src/pages/Persons/Persons.vue'
import CreatePersons from 'src/pages/Persons/CreatePersons.vue'

import acu_estu from 'src/pages/Acu-Estu/Acu-Estu.vue'
import CreateAE from 'src/pages/Acu-Estu/CreateAE.vue'
import EditRegistration from 'src/pages/Registration/EditRegistration.vue'



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
        path: 'persons',
        name: 'Persons',
        component: Persons
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
