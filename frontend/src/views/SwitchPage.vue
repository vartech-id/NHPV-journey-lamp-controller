<script setup>
import { useRouter } from 'vue-router'
import axios from 'axios';
import { onMounted } from 'vue';

const BASE_URL = import.meta.env.VITE_API_URL

const router = useRouter()

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
    router.push('/countdown-b')
}

onMounted(() => {
  handleOff()
})


</script>

<template>
  <div>
    <h1>SwicthPage</h1>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped>

</style>
