<template>
  <div id="profile_page">
    <div id="profile_information">
      <p id="profile_title_text">User Information:</p>

      <div class="form_row">
        <label>Name:</label>
        <input v-model="name" />
      </div>

      <div class="form_row">
        <label>Age:</label>
        <input v-model="age" />
      </div>

      <div class="form_row">
        <label>Email:</label>
        <input v-model="email" />
      </div>

      <div class="form_row">
        <label>Phone:</label>
        <input v-model="phone" />
      </div>

      <div class="form_row">
        <label>Address:</label>
        <textarea v-model="address"></textarea>
      </div>
      <button id="profile_button">Change</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { identity_request } from "@/router/api_client";

const name = localStorage.getItem("name");
const age = localStorage.getItem("age");
const email = localStorage.getItem("email");
const phone = localStorage.getItem("phone");
const address = localStorage.getItem("address");
</script>

<style lang="css">
#profile_page {
  height: 100%;
  width: 100%;
  #profile_information {
    background-color: rgba(198, 221, 234, 0.672);
    height: 80%;
    width: 80%;
    margin: 10%;
    border-radius: 10px;
    #profile_title_text {
      padding-top: 30px;
      font-size: 20px;
      font-weight: 600;
      margin-bottom: 20px;
      text-align: center;
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

    #profile_button {
      align-self: center;
    }
  }
}
</style>
