<template>
  <div id="profile_page">
    <div id="profile_information">
      <div class="profile_header">
        <div class="avatar_circle">
          {{ userInitial }}
        </div>

        <div>
          <p id="profile_title_text">User Information</p>
          <p class="profile_subtitle">Manage your personal account details</p>
        </div>
      </div>

      <div class="form_grid">
        <div class="form_row">
          <label>Name</label>
          <input v-model="name" />
        </div>

        <div class="form_row">
          <label>Age</label>
          <input v-model="age" type="number" />
        </div>

        <div class="form_row">
          <label>Email</label>
          <input v-model="email" type="email" />
        </div>

        <div class="form_row">
          <label>Phone</label>
          <input v-model="phone" type="tel" />
        </div>

        <div class="form_row full_width">
          <label>Address</label>
          <textarea v-model="address"></textarea>
        </div>
      </div>

      <div id="profile_button_div">
        <button class="profile_button primary" @click="save_profile_change">
          Save Changes
        </button>

        <button
          class="profile_button secondary"
          @click="emit('switch-view', 'change_pwd')"
        >
          Change Password
        </button>
      </div>

      <p v-if="message" class="message">
        {{ message }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import { identity_request } from "@/router/api_client";

const emit = defineEmits<{
  (e: "switch-view", view: "change_pwd"): void;
}>();

const message = ref<string>("");

const name = ref<string>(localStorage.getItem("name") || "");
const age = ref<string>(localStorage.getItem("age") || "");
const email = ref<string>(localStorage.getItem("email") || "");
const phone = ref<string>(localStorage.getItem("phone") || "");
const address = ref<string>(localStorage.getItem("address") || "");

const userInitial = computed<string>(() => {
  if (name.value.trim() === "") {
    return "?";
  }

  return name.value
    .trim()
    .split(" ")
    .map((word) => word[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();
});

async function save_profile_change(): Promise<void> {
  if (email.value.trim() === "") {
    message.value = "User email cannot be empty";
    return;
  }

  const ageNumber = Number(age.value);

  if (Number.isNaN(ageNumber)) {
    message.value = "Age must be a number";
    return;
  }

  const token = localStorage.getItem("token");

  if (!token) {
    message.value = "User not logged in";
    return;
  }

  const body = {
    name: name.value,
    age: ageNumber,
    email: email.value,
    phone: phone.value,
    address: address.value,
  };

  const res = await fetch(identity_request("set_my_info"), {
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
    localStorage.setItem("name", name.value);
    localStorage.setItem("age", age.value);
    localStorage.setItem("email", email.value);
    localStorage.setItem("phone", phone.value);
    localStorage.setItem("address", address.value);

    message.value = "Profile updated successfully";
  } else {
    message.value = data.message ?? "Update failed";
  }
}
</script>

<style scoped>
#profile_page {
  width: 100%;
  height: 100%;
  padding: 48px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

#profile_information {
  width: min(760px, 100%);
  padding: 32px;
  border-radius: 24px;
  background: linear-gradient(
    135deg,
    rgba(239, 249, 255, 0.92),
    rgba(214, 235, 248, 0.9)
  );
  border: 1px solid rgba(130, 170, 190, 0.35);
  box-shadow:
    0 18px 45px rgba(41, 82, 112, 0.18),
    inset 0 1px 0 rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
}

.profile_header {
  display: flex;
  align-items: center;
  gap: 18px;
  margin-bottom: 30px;
}

.avatar_circle {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #409eff, #7cc7ff);
  color: white;
  font-size: 26px;
  font-weight: 800;
  box-shadow: 0 10px 25px rgba(64, 158, 255, 0.35);
}

#profile_title_text {
  margin: 0;
  font-size: 26px;
  font-weight: 800;
  color: #1f2933;
}

.profile_subtitle {
  margin: 5px 0 0 0;
  color: #5f6f7a;
  font-size: 14px;
}

.form_grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px 22px;
}

.form_row {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form_row.full_width {
  grid-column: 1 / -1;
}

.form_row label {
  font-size: 13px;
  font-weight: 700;
  color: #34495e;
  letter-spacing: 0.02em;
}

.form_row input,
.form_row textarea {
  width: 100%;
  padding: 12px 14px;
  border: 1px solid rgba(120, 150, 170, 0.45);
  border-radius: 12px;
  font-size: 15px;
  color: #1f2933;
  outline: none;
  box-sizing: border-box;
  background-color: rgba(255, 255, 255, 0.85);
  transition:
    border-color 0.2s ease,
    box-shadow 0.2s ease,
    background-color 0.2s ease;
}

.form_row textarea {
  min-height: 90px;
  resize: vertical;
}

.form_row input:focus,
.form_row textarea:focus {
  border-color: #409eff;
  background-color: white;
  box-shadow: 0 0 0 4px rgba(64, 158, 255, 0.14);
}

#profile_button_div {
  display: flex;
  gap: 16px;
  justify-content: flex-end;
  margin-top: 28px;
}

.profile_button {
  min-width: 170px;
  height: 42px;
  padding: 0 18px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 700;
  transition:
    transform 0.18s ease,
    box-shadow 0.18s ease,
    background-color 0.18s ease;
}

.profile_button:hover {
  transform: translateY(-2px);
}

.profile_button.primary {
  background: linear-gradient(135deg, #409eff, #2f8ee5);
  color: white;
  box-shadow: 0 10px 22px rgba(64, 158, 255, 0.28);
}

.profile_button.secondary {
  background-color: rgba(255, 255, 255, 0.9);
  color: #2f5f83;
  border: 1px solid rgba(120, 150, 170, 0.45);
}

.profile_button.secondary:hover {
  background-color: white;
}

.message {
  margin: 20px 0 0 0;
  padding: 12px 14px;
  border-radius: 12px;
  background-color: rgba(255, 255, 255, 0.75);
  color: #245b7a;
  font-weight: 700;
  text-align: center;
}

@media (max-width: 760px) {
  #profile_page {
    padding: 24px;
  }

  .form_grid {
    grid-template-columns: 1fr;
  }

  #profile_button_div {
    flex-direction: column;
  }

  .profile_button {
    width: 100%;
  }
}
</style>
