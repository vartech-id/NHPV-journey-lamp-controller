<script setup>
import { useRouter } from "vue-router";

const router = useRouter();



const handleNext = () => {
  router.push("/switch-page");
};
</script>

<template>
  <div>
    <h1>DescriptonA</h1>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped></style>
