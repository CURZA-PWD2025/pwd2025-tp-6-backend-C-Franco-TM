import { defineStore } from "pinia";
import ApiService from "@/services/ApiService";

interface Categoria {
  id: number;
  nombre: string;
}

export const useCategoriaStore = defineStore("categoria", {
  state: () => ({
    categorias: [] as Categoria[],
  }),
  actions: {
    async fetchCategorias() {
      try {
        const response = await ApiService.getAll("categorias");
        this.categorias = response.data;
      } catch (error) {
        console.error("Error al obtener categorías:", error);
      }
    },

    async createCategoria(data: Categoria) {
      try {
        await ApiService.create("categorias", data);
        await this.fetchCategorias(); // actualizar lista
      } catch (error) {
        console.error("Error al crear categoría:", error);
      }
    },

    async updateCategoria(id: number, data: Categoria) {
      try {
        await ApiService.update("categorias", id, data);
        await this.fetchCategorias();
      } catch (error) {
        console.error("Error al actualizar categoría:", error);
      }
    },

    async deleteCategoria(id: number) {
      try {
        await ApiService.delete("categorias", id);
        await this.fetchCategorias();
      } catch (error) {
        console.error("Error al eliminar categoría:", error);
      }
    },
  },
});
