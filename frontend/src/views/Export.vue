<script setup>
import { useRouter } from "vue-router";
import { ref } from "vue";
import axios from "axios";

const BASE_URL = import.meta.env.VITE_API_URL;
const router = useRouter();
const isDownloadingDb = ref(false);
const isDownloadingExcel = ref(false);
const statusMessage = ref("");
const errorMessage = ref("");

const handleHome = () => {
  router.push("/");
};

const getFilenameFromHeader = (contentDisposition, fallbackFilename) => {
  if (!contentDisposition) return fallbackFilename;
  const utf8Match = contentDisposition.match(/filename\*=UTF-8''([^;]+)/i);
  if (utf8Match?.[1]) {
    return decodeURIComponent(utf8Match[1]);
  }
  const regularMatch = contentDisposition.match(/filename="?([^"]+)"?/i);
  return regularMatch?.[1] ?? fallbackFilename;
};

const downloadBlob = (blob, filename) => {
  const url = window.URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  document.body.appendChild(anchor);
  anchor.click();
  anchor.remove();
  window.URL.revokeObjectURL(url);
};

const downloadFile = async (endpoint, fallbackFilename) => {
  const response = await axios.get(BASE_URL + endpoint, {
    responseType: "blob",
  });
  const filename = getFilenameFromHeader(
    response.headers["content-disposition"],
    fallbackFilename
  );
  downloadBlob(response.data, filename);
  return filename;
};

const handleDownloadDatabase = async () => {
  isDownloadingDb.value = true;
  errorMessage.value = "";
  statusMessage.value = "";
  try {
    const filename = await downloadFile("export/database", "database.db");
    statusMessage.value = `File ${filename} berhasil diunduh.`;
  } catch (error) {
    console.error("Download database error:", error);
    errorMessage.value = "Gagal download file database.";
  } finally {
    isDownloadingDb.value = false;
  }
};

const handleExport = async () => {
  isDownloadingExcel.value = true;
  errorMessage.value = "";
  statusMessage.value = "";
  try {
    const filename = await downloadFile("export/couples.xlsx", "couples.xlsx");
    statusMessage.value = `File ${filename} berhasil diunduh.`;
  } catch (error) {
    console.error("Download Excel error:", error);
    errorMessage.value = "Gagal export database ke Excel.";
  } finally {
    isDownloadingExcel.value = false;
  }
};
</script>

<template>
  <div id="export-page">
    <button @click="handleDownloadDatabase" :disabled="isDownloadingDb">
      {{ isDownloadingDb ? "DOWNLOADING .DB..." : "DOWNLOAD .DB" }}
    </button>
    <button @click="handleExport" :disabled="isDownloadingExcel">
      {{ isDownloadingExcel ? "EXPORTING EXCEL..." : "EXPORT EXCEL" }}
    </button>
    <button @click="handleHome">HOME</button>
    <p v-if="statusMessage" class="status-msg">{{ statusMessage }}</p>
    <p v-if="errorMessage" class="error-msg">{{ errorMessage }}</p>
  </div>
</template>

<style>
#export-page {
  background-color: aqua;
  height: 100vh;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url(../assets/bg-welcome.png);
  gap: 2rem;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.status-msg {
  color: #2b7a2b;
  font-size: 1.3rem;
}

.error-msg {
  color: #c0392b;
  font-size: 1.3rem;
}
</style>
