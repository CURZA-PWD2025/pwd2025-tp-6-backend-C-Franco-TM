<script setup lang="ts">
import ProveedorList from "@/components/proveedores/ProveedorList.vue";
import ProveedorForm from "@/components/proveedores/ProveedorForm.vue";
import { ref } from "vue";

const proveedorSeleccionado = ref(null);

function reset() {
  proveedorSeleccionado.value = null;
}
</script>

<template>
  <div class="main-content">
    <h1>Gestión de Proveedores</h1>
    <div class="layout">
      <section class="listado">
        <ProveedorList @editar="proveedorSeleccionado = $event" />
      </section>
      <aside class="crear">
        <ProveedorForm :proveedorEditar="proveedorSeleccionado" @reset="reset" />
      </aside>
    </div>
  </div>
</template>

<style scoped>
.main-content {
  padding: 2rem;
  background-color: white;
  box-sizing: border-box;
}

.layout {
  display: flex;
  gap: 2rem;
  align-items: flex-start;
  margin-top: 1rem;
}

.listado {
  flex: 2;
  min-width: 0;
}

.crear {
  flex: 1;
  min-width: 300px;
  background: #fafafa;
  padding: 1rem;
  border-radius: 8px;
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.05);
  border-left: 1px solid rgba(0, 0, 0, 0.1); /* separador */
}
</style>
