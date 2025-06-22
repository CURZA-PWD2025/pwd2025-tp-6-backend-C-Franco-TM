import { defineStore } from "pinia";
import ApiService from "@/services/ApiService";

interface Proveedor {
  id: number;
  nombre: string;
  telefono: string;
  direccion: string;
  email: string;
}

export const useProveedorStore = defineStore("proveedor", {
  state: () => ({
    proveedores: [] as Proveedor[],
  }),

  actions: {
    async fetchProveedores() {
      try {
        const res = await ApiService.getAll("proveedores");
        this.proveedores = res.data;
      } catch (error) {
        console.error("Error al obtener proveedores:", error);
      }
    },

    async createProveedor(data: Omit<Proveedor, "id">) {
      try {
        await ApiService.create("proveedores", data);
        this.fetchProveedores(); // Refrescar la lista
      } catch (error) {
        console.error("Error al crear proveedor:", error);
      }
    },

    async updateProveedor(id: number, data: Omit<Proveedor, "id">) {
      try {
        await ApiService.update("proveedores", id, data);
        this.fetchProveedores(); // Refrescar
      } catch (error) {
        console.error("Error al actualizar proveedor:", error);
      }
    },

    async deleteProveedor(id: number) {
      try {
        await ApiService.delete("proveedores", id);
        this.fetchProveedores(); // Refrescar
      } catch (error) {
        console.error("Error al eliminar proveedor:", error);
      }
    },
  },
});
