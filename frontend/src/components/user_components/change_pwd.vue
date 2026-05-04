<template>
  <div class="change_pwd_page">
    <div id="change_pwd_window">
      <h2>Change Password</h2>
      <form class="change_pwd_form" @submit.prevent="submit">
        <label>
          Current Password
          <input v-model="currentPassword" type="password" />
        </label>

        <label>
          New Password
          <input v-model="newPassword" type="password" />
        </label>

        <label>
          Confirm New Password
          <input v-model="confirmPassword" type="password" />
        </label>
        <button type="submit" class="submit_button">Save</button>
      </form>
    </div>
    <p>{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { identity_request } from "@/router/api_client";

const router = useRouter();

const currentPassword = ref("");
const newPassword = ref("");
const confirmPassword = ref("");
const message = ref("");

async function submit(): Promise<void> {
  if (newPassword.value !== confirmPassword.value) {
    message.value = "Passwords do not match";
    return;
  }

  if (newPassword.value === "") {
    message.value = "New password cannot be empty";
    return;
  }

  const token = localStorage.getItem("token");

  if (!token) {
    message.value = "User not logged in";
    return;
  }

  const body = {
    current_password: currentPassword.value,
    new_password: newPassword.value,
  };

  const res = await fetch(identity_request("reset_password"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    message.value = `Request failed: ${res.status}`;
    return;
  }

  const data: {
    state: "success" | "fail";
    message?: string;
  } = await res.json();

  if (data.state === "success") {
    message.value = "Password changed successfully";
    localStorage.removeItem("token");
    setTimeout(() => {
      router.push("/");
    }, 1000);
  } else {
    message.value = data.message ?? "Change password failed";
  }
}
</script>

<style lang="css">
.change_pwd_page {
  width: 100%;
  height: 100%;
  padding: 24px;
  box-sizing: border-box;
}

.change_pwd_form {
  width: 360px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.change_pwd_form label {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-size: 14px;
}

.change_pwd_form input {
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
}

.submit_button {
  margin-top: 10px;
  padding: 10px 12px;
  border: none;
  border-radius: 8px;
  background-color: #409eff;
  color: white;
  font-weight: 700;
  cursor: pointer;
}

.submit_button:hover {
  background-color: #2f8ee5;
}

#change_pwd_window {
  margin-left: 15%;
  width: 500px;
  background-color: rgba(198, 221, 234, 0.672);
  padding: 40px;
  margin-top: 60px;
  border-radius: 10px;
}
</style>
