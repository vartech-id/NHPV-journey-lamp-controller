<script setup>
import { useRouter } from "vue-router";
import axios from "axios";
import { onMounted } from "vue";

const BASE_URL = import.meta.env.VITE_API_URL;

const router = useRouter();

const relayNumber = [1];

const handleOff = async () => {
  try {
    const result = await axios.get(BASE_URL + "relay-off/" + relayNumber);
    console.log(result.data);
  } catch (error) {
    console.log("Failed Turned Off", error);
  }
};

const handleNext = () => {
  router.push("/countdown-b");
};

onMounted(() => {
  handleOff();
});
</script>

<template>
  <div id="switch-page">
    <div class="switch-msg">
      <h1>Sekarang Waktunya</h1>
      <h1>Bertukar peran</h1>
      <div class="sub-msg">
        <p>Pasanganmu silahkan keluar dan kamu</p>
        <p>masuk ke dalam Box</p>
      </div>
    </div>
    <div class="action-button">
      <button class="btn" @click="handleNext">NEXT</button>
    </div>
  </div>
</template>

<style>
#switch-page {
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-countdown-male.png);
}

.switch-msg {
  font-size: 2.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.switch-msg > h1 {
  font-family: var(--font-count);
  color: var(--color-text);
  font-weight: 500;
}

.sub-msg {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-bottom: 5rem;
}

.sub-msg > p {
  font-size: 2.8rem;
  font-family: var(--font-count);
  color: var(--color-text);
  font-weight: 500;
}

</style>
