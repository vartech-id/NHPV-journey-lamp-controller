<script setup>
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import { ref } from "vue";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL;
const LAMP_API_TIMEOUT_MS = 5000;

const router = useRouter();

const lampCommand = ref("");
const isConfirmOpen = ref(false);

const relayNumbers = [2, 3, 4, 5, 6, 7, 8]; //center off

const openConfirm = () => {
  isConfirmOpen.value = true;
};

const closeConfirm = () => {
  isConfirmOpen.value = false;
};

const handleNext = async () => {
  isConfirmOpen.value = false;
  router.push("/follow-page");
};

const handleMainLamp = async () => {
  try {
    const result = await axios.post(BASE_URL + lampCommand.value, {
      relays: relayNumbers,
    }, {
      timeout: LAMP_API_TIMEOUT_MS,
    });
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
};

const handleCentralLamp = async () => {
  try {
    const result = await axios.post(BASE_URL + "relay-off", {
      relays: [1],
    }, {
      timeout: LAMP_API_TIMEOUT_MS,
    });
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
}

onMounted(async () => {
  lampCommand.value = "relay-on";
  await handleCentralLamp()
  await handleMainLamp();
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
      <button class="btn" @click="openConfirm">DONE</button>
    </div>
    <div v-if="isConfirmOpen" class="modal-backdrop">
      <div class="modal">
        <h2>Apakah sudah berfoto?</h2>
        <div class="modal-actions">
          <button type="button" class="modal-btn" @click="closeConfirm">
            NO
          </button>
          <button type="button" class="modal-btn" @click="handleNext">
            YES
          </button>
        </div>
      </div>
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

.end-msg {
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
