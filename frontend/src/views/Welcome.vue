<script setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { ref } from 'vue'
import axios from 'axios'

const BASE_URL = import.meta.env.VITE_API_URL

const router = useRouter()
const lampCommand = ref("relay-off")

const relayNumbers = [1,2,3,4,5];

const handleAllLamp = async () => {
  try {
    const result = await axios.post(BASE_URL + lampCommand.value, {relays : relayNumbers});
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
};

const handleNext = () => {
    router.push('/register')
}

onMounted(()=>{
  handleAllLamp()
})

</script>

<template>
  <div>
    <h1>Welcome</h1>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped>

</style>
