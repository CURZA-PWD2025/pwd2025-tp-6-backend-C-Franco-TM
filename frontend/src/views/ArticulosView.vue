<template>
  <div class="main-content">
    <h1>Gestión de Artículos</h1>
    <div class="layout">
      <section class="listado">
        <ArticulosList @editar="editar" />
      </section>
      <aside class="crear">
        <ArticuloForm :articulo="articuloSeleccionado" @guardado="recargar" />
      </aside>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import ArticuloForm from "@/components/articulos/ArticulosForm.vue";
import ArticulosList from "@/components/articulos/ArticulosList.vue";

const articuloSeleccionado = ref(null);

function editar(articulo: any) {
  articuloSeleccionado.value = { ...articulo };
}

function recargar() {
  articuloSeleccionado.value = null;
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
}
</style>
