<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const handleNext = () => {
    router.push('/end-page')
}
</script>

<template>
  <div id="desc-wanita">
    <img @click="handleNext" class="img-content" src="../assets/desc-male.png" alt="wanita">
  </div>
</template>

<style scoped>

</style>
