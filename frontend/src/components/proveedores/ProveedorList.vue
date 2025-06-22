<template>
  <div>
    <h2>Lista de Proveedores</h2>
    <table>
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Teléfono</th>
          <th>Dirección</th>
          <th>Email</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in proveedoresStore.proveedores" :key="p.id">
          <td>{{ p.nombre }}</td>
          <td>{{ p.telefono }}</td>
          <td>{{ p.direccion }}</td>
          <td>{{ p.email }}</td>
          <td>
            <div class="acciones">
              <button class="editar" @click="$emit('editar', p)">Editar</button>
              <button class="eliminar" @click="eliminar(p.id)">Eliminar</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { useProveedorStore } from '@/stores/proveedores'
const proveedoresStore = useProveedorStore()

function eliminar(id: number) {
  if (confirm("¿Está seguro de eliminar este proveedor?")) {
    proveedoresStore.deleteProveedor(id)
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
