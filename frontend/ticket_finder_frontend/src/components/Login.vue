<template>
  <div class="login_window">
    <label>Hellow travaler!</label>
    <label>Welcome to Ticket Finder!</label>

    <div class="input_box">
      <h4>Please Login</h4>
      <label>Username: </label> <input /> <label>Password: </label>
      <input type="password" />
    </div>

    <div class="button_line">
      <button @click="login">Login</button>
      <button>Clear</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

async function login() {

    // login api call
    
  router.push("/home");
}
</script>

<style lang="css">
.login_window {
  align-items: center;
  background-color: rgb(220, 244, 245);
  width: 30%;
  height: 400px;
  display: flex;
  justify-content: center;
  border-radius: 20px;
  flex-direction: column;
}

.input_box {
  font-family: Georgia, "Times New Roman", Times, serif;
  color: #11a390;
  font-style: bold;
  display: flex;
  flex-direction: column;
}

.button_line {
  margin: 15px;
  display: flex;
  justify-self: center;
  gap: 10px;
  button {
    align-items: center;
  }
  button:hover {
    background-color: rgba(84, 83, 83, 0.628);
  }
}
</style>
