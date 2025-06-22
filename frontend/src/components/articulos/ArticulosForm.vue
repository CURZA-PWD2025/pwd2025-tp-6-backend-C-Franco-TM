<template>
  <div>
    <h2>{{ isEdit ? "Editar" : "Nuevo" }} Artículo</h2>
    <form @submit.prevent="guardar">
      <label for="descripcion">Descripción</label>
      <input id="descripcion" v-model="form.descripcion" placeholder="Descripción" required />

      <label for="precio">Precio</label>
      <input id="precio" v-model.number="form.precio" type="number" placeholder="Precio" required />

      <label for="stock">Stock</label>
      <input id="stock" v-model.number="form.stock" type="number" placeholder="Stock" required />

      <label for="marca">Marca</label>
      <select id="marca" v-model="form.marca_id" required>
        <option value="" disabled hidden>Seleccione una marca</option>
        <option v-for="m in marcasStore.marcas" :key="m.id" :value="m.id">
          {{ m.nombre }}
        </option>
      </select>

      <label for="proveedor">Proveedor</label>
      <select id="proveedor" v-model="form.proveedor_id" required>
        <option value="" disabled hidden>Seleccione un proveedor</option>
        <option v-for="p in proveedoresStore.proveedores" :key="p.id" :value="p.id">
          {{ p.nombre }}
        </option>
      </select>

      <label for="categorias">Categorías</label>
      <select id="categorias" v-model="form.categoria_ids" multiple class="select-multiple">
        <option v-for="cat in categoriasStore.categorias" :key="cat.id" :value="cat.id">
          {{ cat.nombre }}
        </option>
      </select>

      <div class="acciones">
        <button type="submit">Guardar</button>
        <button type="button" @click="resetForm">Cancelar</button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { reactive, watch, onMounted, computed } from "vue";
import { useArticuloStore } from "@/stores/articulos";
import { useMarcaStore } from "@/stores/marcas";
import { useProveedorStore } from "@/stores/proveedores";
import { useCategoriaStore } from "@/stores/categorias";

const props = defineProps<{ articulo?: any }>();
const emit = defineEmits(["guardado"]);

const articulosStore = useArticuloStore();
const marcasStore = useMarcaStore();
const proveedoresStore = useProveedorStore();
const categoriasStore = useCategoriaStore();

const form = reactive({
  descripcion: "",
  precio: 0,
  stock: 0,
  marca_id: "",
  proveedor_id: "",
  categoria_ids: [] as number[],
});

const isEdit = computed(() => !!props.articulo?.id);

watch(
  () => props.articulo,
  (nuevo) => {
    if (nuevo) {
      form.descripcion = nuevo.descripcion;
      form.precio = nuevo.precio;
      form.stock = nuevo.stock;
      form.marca_id = nuevo.marca?.id || "";
      form.proveedor_id = nuevo.proveedor?.id || "";
      form.categoria_ids = nuevo.categorias?.map((c: any) => c.id) || [];
    } else {
      resetForm();
    }
  },
  { immediate: true }
);

onMounted(() => {
  categoriasStore.fetchCategorias();
  marcasStore.fetchMarcas();
  proveedoresStore.fetchProveedores();
});

function guardar() {
  if (form.categoria_ids.length === 0) {
    alert("Debe seleccionar al menos una categoría.");
    return;
  }

  const data = {
    descripcion: form.descripcion,
    precio: form.precio,
    stock: form.stock,
    marca: { id: Number(form.marca_id) },
    proveedor: { id: Number(form.proveedor_id) },
    categorias: form.categoria_ids.map((id) => ({ id })),
  };

  if (isEdit.value) {
    articulosStore.updateArticulo(props.articulo.id, data);
  } else {
    articulosStore.createArticulo(data);
  }

  resetForm();
  emit("guardado");
}

function resetForm() {
  form.descripcion = "";
  form.precio = 0;
  form.stock = 0;
  form.marca_id = "";
  form.proveedor_id = "";
  form.categoria_ids = [];
}
</script>

<style scoped>
input,
select {
  display: block;
  margin-bottom: 10px;
  padding: 6px;
  width: 100%;
  max-width: 400px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
}

.select-multiple {
  height: auto;
  min-height: 120px;
}

select option[value=""] {
  color: #aaa;
  font-style: normal;
}

label {
  font-weight: bold;
  margin-bottom: 4px;
  display: block;
}

.acciones {
  margin-top: 1rem;
  display: flex;
  gap: 8px;
}

.acciones button {
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.acciones button[type="submit"] {
  background-color: #2c2c2c; /* negro más claro */
  color: white;
}

.acciones button[type="button"] {
  background-color: #e5e7eb; /* gris claro */
  color: #111;
}

.acciones button:hover {
  opacity: 0.9;
}
</style>
