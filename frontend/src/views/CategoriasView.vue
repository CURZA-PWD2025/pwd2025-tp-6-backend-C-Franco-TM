<template>
  <div class="main-content">
    <h1>Gestión de Categorías</h1>
    <div class="layout">
      <section class="listado">
        <CategoriasList @editar="seleccionarCategoria" />
      </section>
      <aside class="crear">
        <CategoriaForm
          :categoriaEditar="categoriaSeleccionada"
          @guardado="refrescar"
          @reset="categoriaSeleccionada = null"
        />
      </aside>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useCategoriaStore } from "@/stores/categorias";
import CategoriaForm from "@/components/categorias/CategoriaForm.vue";
import CategoriasList from "@/components/categorias/CategoriasList.vue";

const categoriaSeleccionada = ref(null);
const store = useCategoriaStore();

function seleccionarCategoria(categoria: { id: number; nombre: string }) {
  categoriaSeleccionada.value = { ...categoria };
}

function refrescar() {
  store.fetchCategorias();
  categoriaSeleccionada.value = null;
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
