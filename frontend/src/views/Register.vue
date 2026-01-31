<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL;
const router = useRouter();

const form = ref({
  pria: "",
  wanita: "",
});

const logForm = () => {
  console.log("FORM NOW:", { ...form.value });
};

const handleSubmit = async () => {
  try {
    const result = await axios.post(BASE_URL + "users", form.value);
    console.log(result.data);
    const payload = result?.data ?? form.value;
    localStorage.setItem("couple", JSON.stringify(payload));
    form.value = { wanita: "", pria: "" };
    handleNext();
  } catch (error) {
    console.error(`Error submitting form:`, error);
  }
};

const handleNext = () => {
  router.push("/countdown-a");
};
</script>

<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent>
      <label for="">Nama pasangan (Pria)</label>
      <br />
      <input type="text" id="pria" v-model="form.pria" @input="logForm" />
      <br />
      <label for="">Nama Pasangan (wanita)</label>
      <br />
      <input type="text" id="wanita" v-model="form.wanita" @input="logForm" />
      <br />
      <button @click="handleSubmit">SUBMIT</button>
    </form>
    <button @click="handleNext">Next</button>
  </div>
</template>

<style scoped></style>
