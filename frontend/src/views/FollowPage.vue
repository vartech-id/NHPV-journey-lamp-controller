<script setup>
import { useRouter } from "vue-router";
import { onMounted } from "vue";
import { ref } from "vue";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL;

const router = useRouter();

const lampCommand = ref("");
const isConfirmOpen = ref(false);

const relayNumbers = [1, 2, 3, 4, 5, 6, 7, 8];

const openConfirm = () => {
  isConfirmOpen.value = true;
};

const closeConfirm = () => {
  isConfirmOpen.value = false;
};

const handleAllLamp = async () => {
  try {
    const result = await axios.post(BASE_URL + lampCommand.value, {
      relays: relayNumbers,
    });
    console.log(result.data);
  } catch (error) {
    console.error(`API Error:`, error);
  }
};

const handleNext = async () => {
  isConfirmOpen.value = false;
  lampCommand.value = "relay-off";
  console.log("turning_off.....")
  await handleAllLamp();
  router.push("/");
};


</script>

<template>
  <div id="desc-man">
    <img
      @click="openConfirm"
      class="img-content"
      src="../assets/bg-follow.png"
      alt="wanita"
    />
    <div v-if="isConfirmOpen" class="modal-backdrop">
      <div class="modal">
        <h2>Kembali ke home ?</h2>
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
.img-content {
  max-width: 1080px;
}
</style>
