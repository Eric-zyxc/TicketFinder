<template>
  <div class="background">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { onMounted } from "vue";

const router = useRouter();

onMounted(() => {
  const token = localStorage.getItem("token");
  if (!token) {
    router.push("/login");
  } else {
    router.push("/home");
  }
});
</script>

<style lang="css">
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
button:hover {
  background-color: #aee4ee;
  scale: 105%;
  box-shadow: 0 10px 20px rgba(40, 80, 110, 0.14);
}
</style>
