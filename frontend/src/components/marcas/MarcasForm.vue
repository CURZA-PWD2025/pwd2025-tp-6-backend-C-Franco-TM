<template>
  <div>
    <h2>{{ marca.id ? "Editar Marca" : "Crear Marca" }}</h2>
    <form @submit.prevent="guardar">
      <input v-model="marca.nombre" placeholder="Nombre de la marca" required />

      <div class="acciones">
        <button type="submit">{{ marca.id ? "Actualizar" : "Crear" }}</button>
        <button type="button" @click="cancelar">Cancelar</button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { reactive, watch } from "vue";
import { useMarcaStore } from "@/stores/marcas";

const store = useMarcaStore();
const emit = defineEmits(["guardado", "reset"]);

const props = defineProps<{
  modelo?: { id?: number; nombre: string };
}>();

const marca = reactive<{ id?: number; nombre: string }>({
  id: undefined,
  nombre: "",
});

watch(
  () => props.modelo,
  (nuevo) => {
    if (nuevo) {
      marca.id = nuevo.id;
      marca.nombre = nuevo.nombre;
    }
  },
  { immediate: true }
);

function guardar() {
  if (marca.id) {
    store.updateMarca(marca.id, { nombre: marca.nombre });
  } else {
    store.createMarca({ nombre: marca.nombre });
  }
  cancelar();
  emit("guardado");
}

function cancelar() {
  reset();
  emit("reset");
}

function reset() {
  marca.id = undefined;
  marca.nombre = "";
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 12px;
}

input {
  padding: 6px;
}

.acciones {
  display: flex;
  gap: 10px;
}

.acciones button {
  padding: 6px 12px;
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
</style>
