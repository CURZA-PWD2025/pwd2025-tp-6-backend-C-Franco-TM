import { defineStore } from "pinia";
import axios from "axios";

export const useArticuloStore = defineStore("articulo", {
  state: () => ({
    articulos: [] as {
      id: number;
      descripcion: string;
      precio: number;
      stock: number;
      marca: { id: number; nombre: string };
      proveedor: {
        id: number;
        nombre: string;
        telefono: string;
        direccion: string;
        email: string;
      };
      categorias: { id: number; nombre: string }[];
    }[],
  }),
  actions: {
    async fetchArticulos() {
      try {
        const response = await axios.get("http://localhost:5000/articulos/");
        this.articulos = response.data;
      } catch (error) {
        console.error("Error al obtener artículos", error);
      }
    },
    async createArticulo(data: any) {
      try {
        await axios.post("http://localhost:5000/articulos/", data);
        this.fetchArticulos();
      } catch (error) {
        console.error("Error al crear artículo", error);
      }
    },
    async updateArticulo(id: number, data: any) {
      try {
        await axios.put(`http://localhost:5000/articulos/${id}`, data);
        this.fetchArticulos();
      } catch (error) {
        console.error("Error al actualizar artículo", error);
      }
    },
    async deleteArticulo(id: number) {
      try {
        await axios.delete(`http://localhost:5000/articulos/${id}`);
        this.fetchArticulos();
      } catch (error) {
        console.error("Error al eliminar artículo", error);
      }
    },
  },
});
