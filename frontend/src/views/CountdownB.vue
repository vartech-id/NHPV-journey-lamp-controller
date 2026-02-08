<script setup>
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import { useCountdown } from "../composable/useCountdown";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL

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
  router.push("/info-b");
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
      <span>{{ error }}</span>
    </div>
    <div class="action-button">
      <button class="btn">NEXT</button>
    </div>
  </div>
</template>

<style>

</style>
