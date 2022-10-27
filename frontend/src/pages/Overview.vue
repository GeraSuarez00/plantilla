<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-warning">
              <i class="nc-icon nc-badge text-warning"></i>
            </div>
            <div slot="content">
              <p class="card-category">Reportes</p>
              <h5 class="card-title">Estudiantes</h5>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>Consultar ahora
            </div>
          </stats-card>
        </div>

        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-warning">
              <i class="nc-icon nc-credit-card text-warning"></i>
            </div>
            <div slot="content">
              <p class="card-category">Reportes</p>
              <h5 class="card-title">Pagos</h5>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>Consultar ahora
            </div>
          </stats-card>
        </div>

        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-warning">
              <i class="nc-icon nc-paper-2 text-warning"></i>
            </div>
            <div slot="content">
              <p class="card-category">Reportes</p>
              <h5 class="card-title">Matrículas</h5>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>Consultar ahora
            </div>
          </stats-card>
        </div>

        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-warning">
              <i class="nc-icon nc-notes text-warning"></i>
            </div>
            <div slot="content">
              <p class="card-category">Reportes</p>
              <h5 class="card-title">...</h5>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>Consultar ahora
            </div>
          </stats-card>
        </div>

      </div>
      </div>
    </div>

</template>
<script>
  import ChartCard from 'src/components/Cards/ChartCard.vue'
  import StatsCard from 'src/components/Cards/StatsCard.vue'
  import LTable from 'src/components/Table.vue'

  export default {
    components: {
      LTable,
      ChartCard,
      StatsCard
    },
  }
</script>
<style>

</style>
