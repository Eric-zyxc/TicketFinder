<template>
  <div class="header">
    <img src="@/asset/picture/logo.png" class="logo" />
    <nav>
      <router-link to="/Home" class="menu_element">Home</router-link>
      <router-link to="/Home" class="menu_element">User</router-link>
      <router-link to="/Home" class="menu_element">Booking</router-link>
      <router-link to="/Home" class="menu_element">About</router-link>
      <router-link to="/" class="menu_element">Logout</router-link>
    </nav>
  </div>
</template>

<script setup lang="ts"></script>

<style lang="css">
.logo {
  height: 60px;
}
.header {
  display: flex;
  padding: 10px;
  font-family: Georgia, 'Times New Roman', Times, serif;
  font-size: 15px;
  .menu_element {
    margin-left: 10px;
    padding: 5%;
    color: #feffff;
  }
}
</style>
