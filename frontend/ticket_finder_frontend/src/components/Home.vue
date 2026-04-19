<template>
  <div class="home_page">
    <div class="header">
      <Header />
    </div>

    <div class="main_area">
      <div class="left_menu">
        <FeatureMenu />
      </div>

      <div class="center_area">
        <MainContent />
      </div>

      <div class="right_menu">
        <UserMenu />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/Header.vue";
import FeatureMenu from "@/components/FeatureMenu.vue";
import UserMenu from "@/components/UserMenu.vue";
import MainContent from "@/components/MainContent.vue";
</script>

<style lang="css">
.home_page {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
.header {
  width: 100%;
  height: 40px;
  border-bottom: 1px solid #ccc;
  background-color: rgba(34, 140, 239, 0.748);
}
.main_area {
  flex: 1;
  margin-top: 30px;
  display: flex;
  width: 100%;
}
.left_menu {
  width: 20%;
  border: 2px solid #ccc;
  border-radius: 20px;
  background-color: azure;
}
.center_area {
  flex: 1;
  padding: 20px;
}
.right_menu {
  width: 20%;
  background-color: antiquewhite;
  border-radius: 20px;
  border: 2px solid #ccc;
}
</style>
