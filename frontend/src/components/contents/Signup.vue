<template>
  <div id="background">
    <div class="signup_overlay">
      <div class="signup_window">
        <h2 class="title">Create Account</h2>

        <div class="form">
          <label>Username <span class="star">*</span></label>
          <input v-model="username" />

          <label>Password <span class="star">*</span></label>
          <input v-model="password" type="password" />

          <label>Confirm Password <span class="star">*</span></label>
          <input v-model="confirmPassword" type="password" />

          <label>Name</label>
          <input v-model="name" />

          <label>Age</label>
          <input v-model="age" type="number" />

          <label>Email</label>
          <input v-model="email" />

          <label>Phone</label>
          <input v-model="phone" />

          <label>Address</label>
          <input v-model="address" />
        </div>

        <div class="button_line">
          <button class="btn primary" @click="signup">Sign Up</button>
          <button class="btn secondary" @click="return_button">Back</button>
        </div>

        <p class="message">{{ message }}</p>
      </div>
    </div>
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
  if (username.value === "") {
    message.value = "Username cannot be empty";
    return;
  }

  if (password.value !== confirmPassword.value) {
    message.value = "Passwords do not match";
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

  if (data.state === "success") {
    router.push("/login");
  } else {
    message.value = data.message;
  }
}

function return_button() {
  router.push("/");
}
</script>

<style scoped>
#background {
  height: 100vh;
  width: 100%;
  background-image: url("/src/asset/picture/bk1.png");
  background-size: cover;
  background-position: center;
}

.signup_overlay {
  width: 100%;
  height: 100%;
  backdrop-filter: blur(6px);
  display: flex;
  justify-content: center;
  align-items: center;
}

.signup_window {
  width: 420px;
  padding: 30px;
  border-radius: 22px;

  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(12px);

  border: 1px solid rgba(150, 180, 200, 0.4);
  box-shadow: 0 18px 40px rgba(40, 80, 110, 0.2);

  display: flex;
  flex-direction: column;
  gap: 18px;
}

.title {
  text-align: center;
  margin: 0;
  font-size: 24px;
  font-weight: 800;
  color: #2e465d;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form label {
  font-size: 13px;
  font-weight: 700;
  color: #2e465d;
}

.form input {
  padding: 10px 12px;
  border-radius: 10px;
  border: 1px solid #c7d3db;
  font-size: 14px;
  outline: none;
  transition: all 0.2s ease;
}

.form input:focus {
  border-color: #409eff;
  box-shadow: 0 0 0 3px rgba(64, 158, 255, 0.2);
}

.button_line {
  display: flex;
  gap: 12px;
}

.btn {
  flex: 1;
  height: 40px;
  border-radius: 10px;
  border: none;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.2s ease;
}

.primary {
  background: linear-gradient(135deg, #409eff, #2f8ee5);
  color: white;
}

.primary:hover {
  filter: brightness(0.95);
}

.secondary {
  background: #eef6fb;
  color: #2e465d;
}

.secondary:hover {
  background: #dbeef9;
}

.message {
  text-align: center;
  font-size: 13px;
  color: #b91c1c;
}

.star {
  color: red;
}
</style>
