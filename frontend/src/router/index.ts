import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import MarcasView from "../views/MarcasView.vue";
import CategoriasView from "../views/CategoriasView.vue";
import ProveedoresView from "../views/ProveedoresView.vue";
import ArticulosView from "../views/ArticulosView.vue";

const routes = [
  { path: "/", name: "home", component: HomeView },
  { path: "/marcas", name: "marcas", component: MarcasView },
  { path: "/categorias", name: "categorias", component: CategoriasView },
  { path: "/proveedores", name: "proveedores", component: ProveedoresView },
  { path: "/articulos", name: "articulos", component: ArticulosView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
