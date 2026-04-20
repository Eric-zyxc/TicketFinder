<template>
  <div class="login_window">
    <label>Hellow travaler!</label>
    <label>Welcome to Ticket Finder!</label>

    <div class="input_box">
      <h4>Please Login</h4>
      <label>Username: </label>
      <input v-model="username" />
      <label>Password: </label>
      <input type="password" v-model="password" />
    </div>

    <div class="button_line">
      <button @click="login" class="btns">Login</button>
      <button @click="gotoSignupPage" class="btns">Signup</button>
    </div>
    <p class="message">{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { identity_request } from "@/router/api_client";

const router = useRouter();
const username = ref("");
const password = ref("");
const message = ref("");

async function login() {
  if (username.value == "") {
    message.value = "User name and password cannot to be empty";
    return;
  }

  const body = new URLSearchParams();
  body.append("username", username.value);
  body.append("password", password.value);

  const res = await fetch(identity_request("login"), {
    method: "POST",
    body,
  });

  const data = await res.json();
  if (data.state == "success") {
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("name", data.name);
    localStorage.setItem("age", data.age);
    localStorage.setItem("email", data.email);
    localStorage.setItem("phone", data.phone);
    localStorage.setItem("address", data.address);
    router.push("/home");
  } else {
    message.value = data.message;
  }
}

async function gotoSignupPage() {
  router.push("/signup");
}
</script>

<style lang="css">
.login_window {
  margin-top: 200px;
  justify-self: center;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    "Open Sans",
    "Helvetica Neue",
    sans-serif;
  font-style: bold;
  align-items: center;
  background-color: rgb(191, 249, 249);
  width: 30%;
  padding-block: 50px;
  display: flex;
  justify-content: center;
  border-radius: 20px;
  flex-direction: column;
}

.input_box {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.button_line {
  margin: 15px;
  display: flex;
  justify-self: center;
  gap: 20px;
  .btns:hover {
    background-color: rgba(226, 226, 226, 1);
  }
}
</style>
