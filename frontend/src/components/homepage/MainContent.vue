<template>
  <component :is="currentComponent" />
</template>

<script setup lang="ts">
import { computed } from "vue";

import ProfileView from "@/components/user_components/profile.vue";
import HomeView from "@/components/homepage/home_view.vue";

type ViewType = "home" | "profile";

const props = defineProps<{
  currentView: ViewType;
}>();

const viewMap: Record<ViewType, object> = {
  home: HomeView,
  profile: ProfileView,
};

const currentComponent = computed(() => {
  return viewMap[props.currentView];
});
</script>

<style lang="css">
html,
body {
  margin: 0;
  padding: 0;
}


</style>
