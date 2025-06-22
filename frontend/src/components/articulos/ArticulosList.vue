<template>
  <div>
    <h2>Lista de Artículos</h2>
    <table>
      <thead>
        <tr>
          <th>Descripción</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Marca</th>
          <th>Proveedor</th>
          <th>Categorías</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="a in articulosStore.articulos" :key="a.id">
          <td>{{ a.descripcion }}</td>
          <td>{{ a.precio }}</td>
          <td>{{ a.stock }}</td>
          <td>{{ a.marca?.nombre }}</td>
          <td>{{ a.proveedor?.nombre }}</td>
          <td>
            <ul>
              <li v-for="cat in a.categorias" :key="cat.id">{{ cat.nombre }}</li>
            </ul>
          </td>
          <td>
            <div class="acciones">
              <button class="editar" @click="$emit('editar', a)">Editar</button>
              <button class="eliminar" @click="eliminar(a.id)">Eliminar</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useArticuloStore } from '@/stores/articulos'

const articulosStore = useArticuloStore()

onMounted(() => {
  articulosStore.fetchArticulos()
})

function eliminar(id: number) {
  if (confirm("¿Está seguro de eliminar este artículo?")) {
    articulosStore.deleteArticulo(id)
  }
}
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
  text-align: left;
  vertical-align: top;
}

ul {
  margin: 0;
  padding-left: 16px;
}

.acciones {
  display: flex;
  gap: 8px;
}

button {
  padding: 6px 10px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button.editar {
  background-color: #e0e0e0;
  color: #111;
}

button.eliminar {
  background-color: #b0b0b0;
  color: white;
}

button:hover {
  opacity: 0.9;
}
</style>
