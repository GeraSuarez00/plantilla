<template>
  <div class="wrapper">
    <side-bar>
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/admin/students">
        <i class="nc-icon nc-badge"></i>
        <p>Estudiantes</p>
      </sidebar-link>
      <sidebar-link to="/admin/attendant">
        <i class="nc-icon nc-single-02"></i>
        <p>Acudientes</p>
      </sidebar-link>
      <sidebar-link to="/admin/payment">
        <i class="nc-icon nc-credit-card"></i>
        <p>Pagos</p>
      </sidebar-link>
      <sidebar-link to="/admin/registration">
        <i class="nc-icon nc-paper-2"></i>
        <p>Matrículas</p>
      </sidebar-link>
      <sidebar-link to="/admin/persons">
        <i class="nc-icon nc-circle-09"></i>
        <p>Personas</p>
      </sidebar-link>
      <sidebar-link to="/admin/acu_estu">
        <i class="nc-icon nc-circle-09"></i>
        <p>Acudientes-Estudiantes</p>
      </sidebar-link>
      <template slot="bottom-links">
        <sidebar-link class="active"
                      to="/admin/ajustes">
          <i class="nc-icon nc-settings-gear-64"></i>
          <p>Ajustes</p>
        </sidebar-link>
      </template>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click="toggleSidebar">

      </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">

</style>
<script>
  import TopNavbar from './TopNavbar.vue'
  import ContentFooter from './ContentFooter.vue'
  import DashboardContent from './Content.vue'
  import MobileMenu from './MobileMenu.vue'
  export default {
    components: {
      TopNavbar,
      ContentFooter,
      DashboardContent,
      MobileMenu
    },
    methods: {
      toggleSidebar () {
        if (this.$sidebar.showSidebar) {
          this.$sidebar.displaySidebar(false)
        }
      }
    }
  }

</script>
