<script setup>
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";

const router = useRouter();
const pria = ref("");

const handleNext = () => {
  router.push("/description-a");
};

onMounted(() => {
  const raw = localStorage.getItem("couple");
  if (!raw) return;
  try {
    const data = JSON.parse(raw);
    pria.value = data?.pria ?? "";
  } catch {
    pria.value = "";
  }
});
</script>

<template>
  <div>
    <h1>InfoA</h1>
    <h2>{{ pria }}</h2>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped>

</style>
