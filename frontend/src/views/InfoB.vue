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
  <div class="info-page-wanita">
    <div class="info-greeting">
      <h1>"Hi {{ wanita }} wanita"</h1>
      <h1>lihatlah pasanganmu disana!</h1>
    </div>
    <div class="info-msg">
      <h1>Dia mungkin terlihat kuat,</h1>
      <h1>tapi kesehatannya perlu di jaga</h1>
    </div>
    <div class="action-button">
      <button class="btn" @click="handleNext">NEXT</button>
    </div>
  </div>
</template>

<style scoped>
.info-page-wanita{
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-infob.png);
  padding-bottom: 12rem;
  gap: 0.5rem;
}
</style>
