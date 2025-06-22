<template>
  <nav class="navbar">
    <router-link to="/">Home</router-link>
    <router-link to="/marcas">Marcas</router-link>
    <router-link to="/categorias">Categorías</router-link>
    <router-link to="/proveedores">Proveedores</router-link>
    <router-link to="/articulos">Artículos</router-link>
  </nav>
</template>

<script setup lang="ts">
</script>

<style scoped>
.navbar {
  width: 100%;
  display: flex;
  justify-content: center;
  gap: 20px;
  padding: 12px 0;
  background-color: #ffffff;
  border-bottom: 1px solid #ddd;
}

a {
  text-decoration: none;
  color: #333;
  padding: 8px 12px;
  font-weight: bold;
  border-bottom: 3px solid transparent;
  transition: background-color 0.2s, border-color 0.2s;
}

a.router-link-active {
  border-bottom: 3px solid #222; /* negro oscuro */
}

a:hover {
  background-color: #f0f0f0; /* gris claro */
  border-radius: 4px;
}
</style>
