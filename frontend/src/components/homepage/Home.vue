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
        <router-view />
      </div>

      <div class="right_menu">
        <UserMenu />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Header from "@/components/contents/Header.vue";
import FeatureMenu from "@/components/homepage/FeatureMenu.vue";
import UserMenu from "@/components/homepage/UserMenu.vue";
import MainContent from "@/components/homepage/MainContent.vue";
</script>

<style lang="css">

.home_page {
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: rgb(212, 239, 252);
  background-image: url("/src/asset/picture/bk1.png");
  background-repeat: no-repeat;
}
.header {
  width: 100%;
  height: 50px;
  background-color: rgba(232, 251, 248, 0.748);
}
.main_area {
  flex: 1;
  display: flex;
  width: 100%;
  height: 850px;
}
.left_menu {
  width: 20%;
  background-color: rgb(202, 236, 245);
  height: 850px;
}
.center_area {
  flex: 1;
}
.right_menu {
  width: 15%;
  background-color: rgb(198, 249, 247);
  height: 850px;
}
</style>
