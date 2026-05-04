<template>
  <div id="background">
    <div class="overlay">
      <div class="container">
        <div class="greeting">
          <p class="title">Hello traveler,</p>
          <p class="subtitle">Welcome back!</p>
        </div>

        <div class="login_window">
          <h3 class="form_title">Please Login</h3>

          <div class="input_box">
            <label>Username</label>
            <input v-model="username" placeholder="Enter username" />

            <label>Password</label>
            <input
              type="password"
              v-model="password"
              placeholder="Enter password"
            />
          </div>

          <div class="button_line">
            <button @click="login" class="btn primary">Login</button>
            <button @click="gotoSignupPage" class="btn secondary">
              Signup
            </button>
          </div>

          <p class="message" v-if="message">{{ message }}</p>
        </div>
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
const message = ref("");

async function login() {
  if (username.value === "" || password.value === "") {
    message.value = "Username and password cannot be empty";
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

  if (data.state === "success") {
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("name", data.name);
    localStorage.setItem("age", data.age);
    localStorage.setItem("email", data.email);
    localStorage.setItem("phone", data.phone);
    localStorage.setItem("address", data.address);
    localStorage.setItem("user_id", data.id);
    router.push("/home");
  } else {
    message.value = data.message;
  }
}

function gotoSignupPage() {
  router.push("/signup");
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

/* overlay for blur */
.overlay {
  width: 100%;
  height: 100%;
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  width: 100%;
  max-width: 900px;
  display: flex;
  align-items: center;
  gap: 40px;
}

/* greeting */
.greeting {
  color: #1f2933;
}

.title {
  font-size: 42px;
  font-weight: 900;
  margin: 0;
}

.subtitle {
  font-size: 28px;
  margin-top: 8px;
  color: #4b5563;
}

/* login card */
.login_window {
  width: 360px;
  padding: 30px;
  border-radius: 20px;

  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(12px);

  border: 1px solid rgba(150, 180, 200, 0.4);
  box-shadow: 0 18px 40px rgba(40, 80, 110, 0.2);

  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form_title {
  margin: 0;
  text-align: center;
  font-weight: 800;
  color: #2e465d;
}

/* inputs */
.input_box {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.input_box label {
  font-size: 13px;
  font-weight: 700;
  color: #2e465d;
}

.input_box input {
  padding: 10px 12px;
  border-radius: 10px;
  border: 1px solid #c7d3db;
  font-size: 14px;
  outline: none;
  transition: all 0.2s ease;
}

.input_box input:focus {
  border-color: #409eff;
  box-shadow: 0 0 0 3px rgba(64, 158, 255, 0.2);
}

/* buttons */
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

/* message */
.message {
  text-align: center;
  font-size: 13px;
  color: #b91c1c;
}
</style>
