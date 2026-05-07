<template>
  <div class="block">
    <div class="profile">
      <div class="user_initial">
        <h1 id="init_text">{{ userInitial }}</h1>
      </div>
      <p class="user_name">{{ nameOfUser }}</p>
    </div>

    <div class="selections">
      <button class="user_button" @click="emit('switch-view', 'profile')">
        👤 Profile
      </button>
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

const emit = defineEmits(["switch-view"]);

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
  if (res.status === 401) {
    alert("Session expired");
    localStorage.clear();
    router.push("/");
    return;
  }

  if (data.state === "success") {
    localStorage.removeItem("token");
    localStorage.removeItem("name");
    localStorage.removeItem("age");
    localStorage.removeItem("email");
    localStorage.removeItem("phone");
    localStorage.removeItem("address");
    localStorage.removeItem("user_id");
    localStorage.clear();
    router.push("/");
  }
  return;
}
</script>

<style lang="css">
.block {
  display: flex;
  flex-direction: column;
  gap: 18px;
  padding: 14px;
  box-sizing: border-box;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;
}

.profile {
  padding: 18px 12px;
  border-radius: 22px;
  background: linear-gradient(
    135deg,
    rgba(183, 229, 248, 0.95),
    rgba(208, 181, 243, 0.9)
  );
  border: 1px solid rgba(130, 170, 190, 0.45);
  box-shadow: 0 10px 24px rgba(40, 80, 110, 0.12);
}

.user_initial {
  width: 76px;
  height: 76px;
  margin: 0 auto 12px auto;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #adf499, #0a7ed1);
  border: 3px solid rgba(255, 255, 255, 0.9);
  box-shadow: 0 10px 22px rgba(64, 158, 255, 0.28);
}

#init_text {
  margin: 0;
  color: white;
  font-size: 30px;
  font-weight: 800;
}

.user_name {
  margin: 0;
  text-align: center;
  font-size: 15px;
  font-weight: 800;
  color: #1f2933;
  word-break: break-word;
}

.selections {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.user_button {
  min-height: 42px;
  padding: 0 14px;
  border: 1px solid rgba(120, 160, 180, 0.45);
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.72);
  color: #2e465d;
  font-size: 14px;
  font-weight: 750;
  text-align: left;
  cursor: pointer;
  box-shadow: 0 6px 14px rgba(40, 80, 110, 0.08);
  transition:
    transform 0.18s ease,
    background-color 0.18s ease,
    box-shadow 0.18s ease;
}

.user_button:hover {
  transform: translateY(-2px);
  background-color: #eef9ff;
}
</style>
