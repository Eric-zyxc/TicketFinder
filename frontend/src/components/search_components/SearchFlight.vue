<template>
  <div class="page">
    <div id="input_window">
      <p>Enter a keyword of location, city, airport, etc.</p>
      <div class="form_row">
        <label>Location:</label>
        <input v-model="key_word" />
      </div>

      <button id="search_button">Search the Keyword</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { travel_request } from "@/router/api_client";

const key_word = ref("");
</script>

<style lang="css">
#input_window {
  width: 300px;
  height: 100px;
  background-color: rgba(198, 221, 234, 0.672);
  height: 80%;
  width: 80%;
  margin: 10%;
  border-radius: 10px;
  align-content: center;
  margin-top: 200px;
  padding: 20px;
  p {
    margin: 20px;
    font-size: large;
  }
}
#search_button {
  margin: 30px;
  width: 150px;
  padding: 10px;
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
</style>
