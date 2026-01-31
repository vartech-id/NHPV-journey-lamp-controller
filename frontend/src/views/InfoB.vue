<script setup>
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";

const router = useRouter();
const wanita = ref("");

const handleNext = () => {
  router.push("/description-b");
};

onMounted(() => {
  const raw = localStorage.getItem("couple");
  if (!raw) return;
  try {
    const data = JSON.parse(raw);
    wanita.value = data?.wanita ?? "";
  } catch {
    wanita.value = "";
  }
});
</script>

<template>
  <div>
    <h1>InfoB</h1>
    <h2>{{ wanita }}</h2>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped>

</style>
