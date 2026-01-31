<script setup>
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";
import axios from "axios";
import { useCountdown } from "../composable/useCountdown";

const BASE_URL = import.meta.env.VITE_API_URL

const router = useRouter();
const { countdown, start, reset } = useCountdown(10);

const relayNumber = [1]

const handleLamp = async () => {
  try {
    const result = await axios.get(BASE_URL + "relay-on/" + relayNumber );
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
};

const handleNext = () => {
  router.push("/info-a");
};

onMounted(() => {
//   reset(10);

//   start(async () => {
//     await handleLamp();
//     handleNext();
//   });
handleLamp()
});
</script>

<template>
  <div>
    <h1>CountdownA</h1>
    <p>{{ countdown }}</p>

    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped></style>
