<script setup>
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";
import axios from "axios";
import { useCountdown } from "../composable/useCountdown";

const BASE_URL = import.meta.env.VITE_API_URL;

const router = useRouter();
const { countdown, start, reset } = useCountdown(5);

const relayNumber = [1];

const handleLamp = async () => {
  try {
    const result = await axios.get(BASE_URL + "relay-on/" + relayNumber);
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
};

const handleNext = () => {
  router.push("/info-a");
};

onMounted(() => {
  reset(5);
  start(async () => {
    await handleLamp();
    handleNext();
  });
});
</script>

<template>
  <div class="countdown-page">
    <div class="countdown-msg">
      <h1>Pasangan Wanita</h1>
      <h1>diPersilahkan masuk ke</h1>
      <h1>Box dalam....</h1>
    </div>
    <div class="countdown-wrapper">
      <h1 class="countdown-time">{{ countdown }}</h1>
    </div>
    <div class="action-button">
      <button class="btn">NEXT</button>
    </div>
  </div>
</template>

<style>
.countdown-page {
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-countdown-male.png);
  gap: 5rem;
  padding-bottom: 12rem;
}

.countdown-msg {
  font-size: 1.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--color-text);
}

.countdown-msg > h1 {
  font-family: var(--font-text);
}

.countdown-wrapper {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.countdown-time {
  background-color: none;
  font-size: 30rem;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 9999px;
  border: 10px solid var(--color-text);
  color: var(--color-text);
  font-family: var(--font-count);
  width: 45rem;
  height: 45rem;
}
</style>
