<template>
  <div class="main-content">
    <h1>Administrar Marcas</h1>
    <div class="layout">
      <section class="listado">
        <MarcasList @editar="editar" />
      </section>
      <aside class="crear">
        <MarcasForm :modelo="marcaSeleccionada" @guardado="refrescar" @reset="marcaSeleccionada = undefined" />
      </aside>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useMarcaStore } from "@/stores/marcas";
import MarcasForm from "@/components/marcas/MarcasForm.vue";
import MarcasList from "@/components/marcas/MarcasList.vue";

const store = useMarcaStore();
const marcaSeleccionada = ref<{ id?: number; nombre: string } | undefined>();

onMounted(() => {
  store.fetchMarcas();
});

function editar(marca: { id: number; nombre: string }) {
  marcaSeleccionada.value = { ...marca };
}

function refrescar() {
  store.fetchMarcas();
  marcaSeleccionada.value = undefined;
}
</script>

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
  border-left: 1px solid rgba(0, 0, 0, 0.1);
}
</style>
