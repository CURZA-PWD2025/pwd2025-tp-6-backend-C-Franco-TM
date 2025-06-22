<template>
  <div id="app">
    <NavBar />
    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
import NavBar from "@/components/NavBar.vue";
</script>

<style>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: white;
/*  background-color: #f5f5f5;*/
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  width: 100vw;
  overflow-x: hidden;
}


.main-content {
  flex: 1;
  padding: 2rem;
  width: 100%;
  max-width: none;
  background-color: transparent;
  box-shadow: none;
  border-radius: 0;
}

/*.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1000px;
  margin: 0 auto;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
}*/
</style>
