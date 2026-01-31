<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const handleNext = () => {
    router.push('/end-page')
}
</script>

<template>
  <div>
    <h1>DescriptonB</h1>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped>

</style>
