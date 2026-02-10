<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isConfirmOpen = ref(false);

const openConfirm = () => {
  isConfirmOpen.value = true;
};

const closeConfirm = () => {
  isConfirmOpen.value = false;
};

const handleNext = () => {
  isConfirmOpen.value = false;
  router.push("/end-page");
};
</script>

<template>
  <div id="desc-wanita">
    <img @click="openConfirm" class="img-content" src="../assets/desc-male.png" alt="wanita" />
    <div v-if="isConfirmOpen" class="modal-backdrop">
      <div class="modal">
        <h2>Lanjut ke halaman selanjutnya ?</h2>
        <div class="modal-actions">
          <button type="button" class="modal-btn" @click="closeConfirm">NO</button>
          <button type="button" class="modal-btn" @click="handleNext">YES</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>
