<script setup>
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import { ref } from "vue";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL;

const router = useRouter();
const lampCommand = ref("relay-off");

const relayNumbers = [2, 3, 4, 5, 6, 7, 8]; //center off

const handleAllLamp = async () => {
  try {
    const result = await axios.post(BASE_URL + lampCommand.value, {
      relays: relayNumbers,
    });
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
};

const handleNext = () => {
  router.push("/register");
};

onMounted(() => {
  handleAllLamp();
});
</script>

<template>
  <div id="welcome-page">
    <div class="welcome-msg">
      <h1>Hai! Selamat datang di aktivitas</h1>
      <h1>Ngobrolin HPV Yuk mulai perjalanan</h1>
      <h1>seru ini bareng kami!</h1>
    </div>

    <div class="action-button">
      <button class="next btn" @click="handleNext">NEXT</button>
    </div>
  </div>
</template>

<style>
#welcome-page {
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-welcome.png);
  gap: 5rem;
  padding-bottom: 40rem;
}

.welcome-msg {
  font-size: 1.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--color-text);
}

.welcome-msg > h1 {
  font-family: var(--font-text);
}

.action-button {
  width: 100%;
  display: flex;
  justify-content: center;
}
</style>
