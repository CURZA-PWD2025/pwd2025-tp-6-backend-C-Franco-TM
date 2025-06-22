<template>
  <div>
    <h2>{{ form.id ? "Editar proveedor" : "Crear proveedor" }}</h2>

    <form @submit.prevent="handleSubmit">
      <input v-model="form.nombre" placeholder="Nombre" required />
      <input v-model="form.telefono" placeholder="Teléfono" required />
      <input v-model="form.direccion" placeholder="Dirección" required />
      <input v-model="form.email" placeholder="Email" type="email" required />

      <div class="acciones">
        <button type="submit">{{ form.id ? "Actualizar" : "Crear" }}</button>
        <button type="button" @click="cancelar">Cancelar</button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { useProveedorStore } from '@/stores/proveedores';

const store = useProveedorStore();

const form = ref({
  id: null,
  nombre: '',
  telefono: '',
  direccion: '',
  email: ''
});

const props = defineProps({
  proveedorEditar: Object,
});

const emit = defineEmits(['reset']);

watch(() => props.proveedorEditar, (nuevo) => {
  if (nuevo) form.value = { ...nuevo };
});

function handleSubmit() {
  if (form.value.id) {
    store.updateProveedor(form.value.id, form.value);
  } else {
    store.createProveedor(form.value);
  }
  cancelar();
}

function cancelar() {
  reset();
  emit('reset');
}

function reset() {
  form.value = {
    id: null,
    nombre: '',
    telefono: '',
    direccion: '',
    email: ''
  };
}
</script>

<style scoped>
.acciones {
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
}

.acciones button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  background-color: #2c2c2c;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.acciones button[type="button"] {
  background-color: #e5e7eb;
  color: #111;
}

.acciones button:hover {
  opacity: 0.9;
}
</style>
