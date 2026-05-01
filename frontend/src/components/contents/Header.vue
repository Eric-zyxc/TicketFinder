<template>
  <div class="header">
    <img src="@/asset/picture/logo.png" class="logo" />
    <nav>
      <router-link to="/Home" class="menu_element" @click="emit('switch-view', 'home')">Home</router-link>
      <router-link to="/Home" class="menu_element">User</router-link>
      <router-link to="/Home" class="menu_element">Booking</router-link>
      <router-link to="/Home" class="menu_element">About</router-link>
      <router-link to="/" class="menu_element">Logout</router-link>
    </nav>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits(['switch-view'])


</script>

<style lang="css">

.logo {
  height: 100%;
}

.header {
  display: flex;
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
  font-size: 25px;
  & .menu_element {
    margin-inline: 25px;
    color: #2e465d;
    align-self: center;
  }
}
</style>
