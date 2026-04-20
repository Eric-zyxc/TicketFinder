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
import Header from "@/components/homepage/Header.vue";
import FeatureMenu from "@/components/homepage/FeatureMenu.vue";
import UserMenu from "@/components/homepage/UserMenu.vue";
import MainContent from "@/components/homepage/MainContent.vue";
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
  height: 100px;
  border-bottom: 1px solid #ccc;
  background-color: rgba(232, 251, 248, 0.748);
}
.main_area {
  flex: 1;
  margin-block: 5px;
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
  width: 15%;
  background-color: rgb(198, 249, 247);
  border-radius: 20px;
  border: 2px solid #ccc;
}
</style>
