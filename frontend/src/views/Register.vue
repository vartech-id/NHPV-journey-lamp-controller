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

const handleUppercaseInput = (field, event) => {
  const value = event.target.value.toUpperCase();
  form.value[field] = value;
  event.target.value = value;
  logForm();
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
  <div id="register-page">
    <div class="register-msg">
      <h1>Silahkan Tuliskan Nama</h1>
      <h1>masing - masing</h1>
    </div>
    <div class="form-wrapper">
      <form @submit.prevent>
        <label for="">Nama pasangan (Pria)</label>
        <input
          type="text"
          id="pria"
          v-model="form.pria"
          @input="handleUppercaseInput('pria', $event)"
        />
        <label for="">Nama Pasangan (wanita)</label>
        <input
          type="text"
          id="wanita"
          v-model="form.wanita"
          @input="handleUppercaseInput('wanita', $event)"
        />
      </form>
    </div>
    <div class="action-button">
      <button class="btn" @click="handleSubmit">NEXT</button>
    </div>
    <!-- <button @click="handleNext">Next</button> -->
  </div>
</template>

<style>
#register-page {
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-register.png);
  gap: 8rem;
  padding-bottom: 28rem;
}

.register-msg {
  font-size: 1.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: var(--color-text);
}

.register-msg > h1 {
  font-family: var(--font-text);
}

.form-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  color: var(--color-text);
  font-family: var(--font-text);
  gap: 2.2rem; 
}


label {
  font-size: 2.8rem;
  margin-bottom: -1rem;
}

input {
  width: 60%;
  font-size: 3rem;
  font-family: var(--font-text);
  color: var(--color-text);
  text-align: center;

  background: transparent;        
  border: none;                   
  border-bottom: 4px solid var(--color-text); 
  padding: 1.2rem 0.8rem;         
  outline: none;
}

input:focus {
  border-bottom: 4px solid var(--color-text);
}


input::placeholder {
  color: rgba(0, 0, 0, 0.35);
}

#pria {
  margin-bottom: 2.8rem;
}

</style>
