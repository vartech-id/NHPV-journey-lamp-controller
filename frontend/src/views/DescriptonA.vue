<script setup>
import { useRouter } from "vue-router";

const router = useRouter();



const handleNext = () => {
  router.push("/switch-page");
};
</script>

<template>
  <div id="desc-man">
    <img @click="handleNext" class="img-content" src="../assets/desc-wanita.png" alt="wanita">
  </div>
</template>

<style>
  .img-content{ 
    max-width: 1080px;
  }
</style>
