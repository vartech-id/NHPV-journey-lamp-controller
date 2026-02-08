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

/* MODAL ACTIONS */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1.5rem;
  z-index: 20;
  backdrop-filter: blur(4px);
}

.modal {
  background: #F2E8D6;
  border-radius: 32px;
  padding: clamp(2rem, 5vw, 3rem);
  text-align: center;
  color: #fff;
  min-width: min(rem, 90vw);
  min-height: min(30rem, 90vw);
  box-shadow: 0 24px 48px rgba(0, 0, 0, 0.35);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.modal > h2 {
  font-size: 84px;
  margin: 0 0 5rem;
  font-weight: 700;
  font-family: "Poppins", sans-serif;
  font-style: normal;
  color: #124F5A;
}

.modal-actions {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  flex-wrap: wrap;
}

.modal-btn {
  min-width: 20rem;
  padding: 1rem 2.5rem;
  font-size: 3.5rem;
  border-radius: 999px;
  cursor: pointer;
  transition:
    transform 150ms ease,
    box-shadow 150ms ease;
      color: #dddc25;
  background-image: linear-gradient(to top, #244f53, #3b878f);
  border: none;
}
</style>
