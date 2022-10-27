<template>
  <ul class="nav nav-mobile-menu">
    <sidebar-link to="/admin/overview">
        <i class="nc-icon nc-tv-2 hidden-lg-up"></i>
        <p>Inicio</p>
      </sidebar-link>
    <!-- <base-dropdown title="Dropdown">
      <a class="dropdown-item" href="#">Action</a>
      <a class="dropdown-item" href="#">Another action</a>
      <a class="dropdown-item" href="#">Something</a>
      <a class="dropdown-item" href="#">Something else here</a>
      <div class="divider"></div>
      <a class="dropdown-item" href="#">Separated link</a>
    </base-dropdown> -->

    <li class="nav-item">
      <a class="nav-link" href="#gera">
        <i class="nc-icon nc-button-power hidden-lg-up"></i>
        <span class="d-lg-none">Log out</span>
      </a>
    </li>
  </ul>
</template>
<script>
  export default {
    name: 'mobile-menu'
  }
</script>
<style>
</style>
