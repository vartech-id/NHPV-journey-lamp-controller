<script setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { ref } from 'vue';
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL

const router = useRouter()

const lampCommand = ref("")

const handleNext = async () => {
  lampCommand.value = "relay-off"
  await handleAllLamp()
    router.push('/')
}

const relayNumbers = [1,2,3,4,5];

const handleAllLamp = async () => {
  try {
    const result = await axios.post(BASE_URL + lampCommand.value, {relays : relayNumbers});
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
};

onMounted( async () => {
  lampCommand.value = "relay-on"
  await handleAllLamp()
})



</script>

<template>
  <div>
    <h1>EndPage</h1>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped>

</style>
