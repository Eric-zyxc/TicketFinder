<template>
  <div id="page">
    <p class="title">User Information</p>

    <p class="text">Username <span class="start">*</span> :</p>
    <input class="input" v-model="username" />

    <p class="text">Password <span class="start">*</span>:</p>
    <input class="input" v-model="password" type="password" />

    <p class="text">Comfirm password <span class="start">*</span>:</p>
    <input class="input" v-model="confirmPassword" type="password" />

    <p class="text">Name:</p>
    <input class="input" v-model="name" />

    <p class="text">Age:</p>
    <input class="input" v-model="age" />

    <p class="text">Email:</p>
    <input class="input" v-model="email" />

    <p class="text">Phone:</p>
    <input class="input" v-model="phone" />

    <p class="text">Address:</p>
    <input class="input" v-model="address" />

    <button class="signup_button" @click="signup">Sign Up</button>
    <button class="back_button" @click="return_button">Back</button>

    <p class="return_message">{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { identity_request } from "@/router/api_client";

const router = useRouter();
const username = ref("");
const password = ref("");
const confirmPassword = ref("");
const name = ref("");
const age = ref<string | number>("");
const email = ref("");
const phone = ref("");
const address = ref("");
const message = ref("");

async function signup() {
  if (username.value == "") {
    message.value = "Username cannot be empty";
    return;
  }
  if (password.value != confirmPassword.value) {
    message.value = "Confirm password doesn't match";
    return;
  }

  const payload = {
    username: username.value,
    password: password.value,
    name: name.value,
    age: age.value === "" ? null : Number(age.value),
    email: email.value,
    phone: phone.value,
    address: address.value,
  };

  const res = await fetch(identity_request("sign_up"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data = await res.json();
  if (data.state == "success") {
    router.push("/login");
  } else if (data.state == "fail") {
    message.value = data.message;
  }
  return;
}

function return_button() {
  router.push("/");
}
</script>

<style lang="css">
.start {
  color: red;
}

#page {
  margin-inline: 30%;
  width: 40%;
  height: 850px;
  background-color: rgb(191, 249, 249);
  border-radius: 20px;
  .text {
    margin-top: 10px;
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
    font-size: large;
    margin-left: 20%;
  }
  .title {
    text-align: center;
    padding: 20px;
    font-size: 30px;
    font-family: Impact, Haettenschweiler, "Arial Narrow Bold", sans-serif;
  }

  .input {
    display: block;
    margin-left: 20%;
    width: 60%;
  }
  .signup_button {
    margin-left: 20%;
    margin-block: 20px;
    margin-right: 5%;
    width: 80px;
  }
  .back_button {
    margin-block: 20px;
    margin-right: 20%;
    width: 80px;
  }
  .signup_button:hover .back_button:hover {
    background-color: rgba(84, 83, 83, 0.628);
  }
  .return_message {
    font-family: monospace;
    margin-inline: 20%;
    margin-block: 20px;
    color: #605f5f;
  }
}
</style>
