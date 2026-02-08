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
  <div class="info-page">
    <div class="info-greeting">
      <h1>"Hi {{ pria }} Pria"</h1>
      <h1>lihatlah pasanganmu disana!</h1>
    </div>
    <div class="info-msg">
      <h1>Dia adalah seorang yang kamu jaga hari ini,</h1>
      <h1>dan esok dan seterusnya</h1>
    </div>
    <div class="action-button">
      <button class="btn" @click="handleNext">NEXT</button>
    </div>
  </div>
</template>

<style>
.info-page {
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-countdown-male.png);
  padding-bottom: 12rem;
  gap: 0.5rem;
}

.info-greeting {
  font-size: 1.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.info-greeting > h1 {
  font-family: var(--font-count);
  color: var(--color-text);
}

.info-msg {
  font-size: 1.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--color-text);
  font-family: var(--font-text);
  padding-bottom: 5rem;
}
</style>
