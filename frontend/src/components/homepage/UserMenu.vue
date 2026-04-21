<template>
  <div class="block">
    <div class="profile">
      <div class="user_initial">
        <h1 id="init_text">{{ userInitial }}</h1>
      </div>
      <p class="user_name">{{ nameOfUser }}</p>
    </div>

    <div class="selections">
      <button class="user_button">👤 Profile</button>
      <button class="user_button">✈️ Flight History</button>
      <button class="user_button">🏨 Hotel History</button>
      <button class="user_button">🎁 Rewards & Gifts</button>
      <button class="user_button">⚙️ Setting</button>
      <button class="user_button" @click="logout">❌ Logout</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { identity_request } from "@/router/api_client";

const router = useRouter();

const nameOfUser = localStorage.getItem("name");
let userInitial = nameOfUser == null ? "" : get_init(nameOfUser);

function get_init(name: string) {
  let res = "";
  res += name[0];
  for (let i = 1; i < name.length; i++) {
    if (name.at(i) == " ") {
      res += name.at(i + 1);
    }
  }
  return res.toUpperCase();
}

async function logout() {
  const token = localStorage.getItem("token");

  const res = await fetch(identity_request("logout"), {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  const data = await res.json();
  if (data.state === "success") {
    localStorage.removeItem("token");
    localStorage.removeItem("name");
    localStorage.removeItem("age");
    localStorage.removeItem("email");
    localStorage.removeItem("phone");
    localStorage.removeItem("address");
    router.push("/");
  }
  return;
}
</script>

<style lang="css">
.block {
  display: flex;
  flex-direction: column;
  .profile {
    background-color: rgb(170, 233, 251);
    margin-block: 5%;
    margin-inline: 10%;
    border: 2px solid rgb(177, 181, 183);
    border-radius: 30px;

    #init_text {
      text-align: center;
      font-size: 40px;
      padding-top:13px;
    }
    .user_initial {
      background-color: rgb(181, 216, 243);
      height: 80px;
      width: 80px;
      justify-self: center;
      margin-block: 10px;
      border: 2px solid rgb(251, 250, 250);
      border-radius: 80px;
    }
    .user_name {
      text-align: center;
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
      font-size: 15px;
      font-weight: bold;
    }
    padding-bottom: 10px;
  }
  .selections {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-inline: 5px;
    .user_button {
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
      font-size: medium;
      border-radius: 20px;
    }
    .user_button:hover {
      scale: 103%;
      background-color: azure;
    }
  }
}
</style>
