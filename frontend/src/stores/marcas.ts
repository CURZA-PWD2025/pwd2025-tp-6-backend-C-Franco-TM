import { defineStore } from "pinia";
import ApiService from "@/services/ApiService";

interface Marca {
  id: number;
  nombre: string;
}

export const useMarcaStore = defineStore("marca", {
  state: () => ({
    marcas: [] as Marca[],
  }),

  actions: {
    async fetchMarcas() {
      try {
        const res = await ApiService.getAll("marcas");
        this.marcas = res.data;
      } catch (error) {
        console.error("Error al obtener marcas:", error);
      }
    },

    async createMarca(data: Omit<Marca, "id">) {
      try {
        await ApiService.create("marcas", data);
        this.fetchMarcas();
      } catch (error) {
        console.error("Error al crear marca:", error);
      }
    },

    async updateMarca(id: number, data: Omit<Marca, "id">) {
      try {
        await ApiService.update("marcas", id, data);
        this.fetchMarcas();
      } catch (error) {
        console.error("Error al actualizar marca:", error);
      }
    },

    async deleteMarca(id: number) {
      try {
        await ApiService.delete("marcas", id);
        this.fetchMarcas();
      } catch (error) {
        console.error("Error al eliminar marca:", error);
      }
    },
  },
});
