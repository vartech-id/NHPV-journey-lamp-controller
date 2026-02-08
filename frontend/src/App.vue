<script setup>
import { RouterView } from "vue-router";
</script>

<template>
  <router-view v-slot="{ Component, route }">
    <transition name="fade" mode="out-in">
      <component :is="Component" :key="route.path" />
    </transition>
  </router-view>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.btn {
  background-image: linear-gradient(to right, #0A565E, #32A194);
  color: #dddc25;
  background-color: white;
  width: 28%;
  font-size: 4rem;
  border: none;
  border-radius: 9rem;
  padding: 0.5rem;
  font-family: var(--font-btn);
}
</style>
