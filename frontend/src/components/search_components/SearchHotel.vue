<template>
  <div class="page">
    <div id="search_hotel_input_window">
      <p>Enter a keyword of location, city, airport, etc.</p>
      <div class="form_row">
        <label>Location:</label>
        <input v-model="key_word" />
      </div>

      <button id="search_button" @click="search_hotel_dest">
        Search the Keyword
      </button>
    </div>
    <p>{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { travel_request } from "@/router/api_client";
import type { HotelDestResult } from "@/types/hotelDestResult";

const emit = defineEmits<{
  (e: "show-result", data: HotelDestResult[]): void;
}>();

const key_word = ref<string>("San Jose");

const message = ref<string>("");

async function search_hotel_dest(): Promise<void> {
  if (key_word.value === "") {
    message.value = "Keyword cannot be empty";
    return;
  }

  const res = await fetch(
    travel_request(
      `search/hotel/dest?dest=${encodeURIComponent(key_word.value)}`,
    ),
    {
      method: "POST",
    },
  );

  const data = await res.json();
  emit("show-result", data.result);
}
</script>

<style lang="css">
#search_hotel_input_window {
  width: 600px;
  height: 300px;
  background-color: rgba(198, 221, 234, 0.672);
  margin: 10%;
  border-radius: 10px;
  align-content: center;
  padding: 20px;
  box-shadow: 0 12px 28px rgba(41, 82, 112, 0.14);
  p {
    margin: 20px;
    font-size: large;
  }
  .form_row {
    display: grid;
    grid-template-columns: 100px 1fr;
    align-items: center;
    margin-bottom: 14px;
    padding-inline: 10%;
  }
  .form_row label {
    font-size: 14px;
    font-weight: 600;
    color: #333;
    margin: 10px;
  }
  .form_row input,
  .form_row textarea {
    width: 100%;
    padding: 8px 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 14px;
    outline: none;
    box-sizing: border-box;
    transition: border 0.2s;
  }
  .form_row input:focus,
  .form_row textarea:focus {
    border-color: #409eff;
    background-color: beige;
  }
  .form_row textarea {
    min-height: 60px;
    resize: vertical;
  }
}
#search_button {
  margin: 30px;
  width: 150px;
  padding: 10px;
}
</style>
