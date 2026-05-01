<template>
  <div class="home_page">
    <div class="header">
      <Header @switch-view="switchView" />
    </div>

    <div class="main_area">
      <div class="left_menu">
        <FeatureMenu @switch-view="switchView" />
      </div>

      <div class="center_area">
        <MainContent :current-view="currentView" />
      </div>

      <div class="right_menu">
        <UserMenu @switch-view="switchView" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Header from "@/components/contents/Header.vue";
import FeatureMenu from "@/components/homepage/FeatureMenu.vue";
import UserMenu from "@/components/homepage/UserMenu.vue";
import MainContent from "@/components/homepage/MainContent.vue";
type ViewType = "home" | "profile";
const currentView = ref<ViewType>("home");
const switchView = (view: ViewType) => {
  currentView.value = view;
};
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
  height: 950px;
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
