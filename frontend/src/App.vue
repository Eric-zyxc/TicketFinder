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
</style>
