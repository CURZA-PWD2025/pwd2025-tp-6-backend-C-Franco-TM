<template>
  <div class="form-container">
    <h2>{{ esEdicion ? 'Editar Categoría' : 'Nueva Categoría' }}</h2>

    <form @submit.prevent="guardar">
      <input
        v-model="categoria.nombre"
        type="text"
        placeholder="Nombre de la categoría"
        required
      />

      <div class="acciones">
        <button type="submit">{{ esEdicion ? 'Actualizar' : 'Crear' }}</button>
        <button type="button" @click="cancelar">Cancelar</button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useCategoriaStore } from '@/stores/categorias'

const props = defineProps<{
  categoriaEditar?: { id: number; nombre: string } | null;
}>()

const emit = defineEmits(['guardado', 'reset'])

const store = useCategoriaStore()
const categoria = ref({ id: null as number | null, nombre: '' })
const esEdicion = ref(false)

watch(
  () => props.categoriaEditar,
  (nueva) => {
    if (nueva) {
      categoria.value = { ...nueva }
      esEdicion.value = true
    } else {
      resetForm()
    }
  },
  { immediate: true }
)

function guardar() {
  if (esEdicion.value && categoria.value.id) {
    store.updateCategoria(categoria.value.id, categoria.value).then(() => {
      emit('guardado')
    })
  } else {
    store.createCategoria({ nombre: categoria.value.nombre }).then(() => {
      emit('guardado')
    })
  }
  cancelar()
}

function cancelar() {
  resetForm()
  emit('reset')
}

function resetForm() {
  categoria.value = { id: null, nombre: '' }
  esEdicion.value = false
}
</script>

<style scoped>
.form-container {
  margin-top: 1rem;
}

input {
  padding: 8px;
  margin-bottom: 10px;
  width: 100%;
  max-width: 300px;
}

.acciones {
  margin-top: 1rem;
  display: flex;
  gap: 10px;
}

.acciones button {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.acciones button[type="submit"] {
  background-color: #2c2c2c;
  color: white;
}

.acciones button[type="button"] {
  background-color: #e5e7eb;
  color: #111;
}

.acciones button:hover {
  opacity: 0.9;
}
</style>
