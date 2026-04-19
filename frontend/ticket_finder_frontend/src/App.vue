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
  }
});
</script>

<style lang="css">
.background {
  background-color: rgba(168, 164, 164, 0.129);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-block: 200px;
}
</style>
