<script setup>
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import { ref } from "vue";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL;

const router = useRouter();

const lampCommand = ref("");

const relayNumbers = [1, 2, 3, 4, 5, 6, 7, 8];

const handleNext = async () => {
  lampCommand.value = "relay-off";
  await handleAllLamp();
  router.push("/");
};

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

onMounted(async () => {
  lampCommand.value = "relay-on";
  await handleAllLamp();
});
</script>

<template>
  <div id="end-page">
    <div class="end-msg">
      <h1>Kini, masuklah bersama</h1>
    </div>
    <div class="sub-msg">
      <p>kalian sudah sampai di titik ini,</p>
      <p>berdirilah berdampingan abadikan</p>
      <p>momen ini dengan melakukan foto</p>
      <p>bersama pasanganmu</p>
    </div>
    <div class="action-button">
      <button class="btn" @click="handleNext">DONE</button>
    </div>
  </div>
</template>

<style>
#end-page {
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-countdown-male.png);
}

.end-msg{ 
  font-size: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.end-msg > h1 {
  font-family: var(--font-count);
  color: var(--color-text);
  font-weight: 500;
}


</style>
