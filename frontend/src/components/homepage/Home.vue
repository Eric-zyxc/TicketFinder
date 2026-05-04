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
        <MainContent
          :current-view="currentView"
          :hotel-results="hotelResults"
          :hotel-search-results="hotelSearchResults"
          @switch-view="switchView"
          @show-result="showResult"
          @show-hotel-search-result="showHotelSearchResult"
        />
      </div>

      <div class="right_menu">
        <UserMenu @switch-view="switchView" />
      </div>
    </div>
    <div class="footer">
      <p>
        © 2026 TicketFinder. Built for travel search, booking, and trip
        management.
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import Header from "@/components/contents/Header.vue";
import FeatureMenu from "@/components/homepage/FeatureMenu.vue";
import UserMenu from "@/components/homepage/UserMenu.vue";
import MainContent from "@/components/homepage/MainContent.vue";
import type { HotelDestResult } from "@/types/hotelDestResult";
import type { HotelSearchResult } from "@/types/hotelSearchResult";

type ViewType =
  | "home"
  | "profile"
  | "change_pwd"
  | "search_flight"
  | "search_hotel"
  | "hotel_result"
  | "hotel_search_result"
  | "hotel_booking_record_page"
  | "airport_search"
  | "flight_booking_record_page"
  | "attraction_search_page"
  | "attraction_booking_record_page"
  | "about_page";

const currentView = ref<ViewType>("home");
const hotelResults = ref<HotelDestResult[]>([]);
const hotelSearchResults = ref<HotelSearchResult[]>([]);

function switchView(view: ViewType): void {
  currentView.value = view;
}

function showResult(data: HotelDestResult[]): void {
  hotelResults.value = data;
  currentView.value = "hotel_result";
}
function showHotelSearchResult(data: HotelSearchResult[]): void {
  hotelSearchResults.value = data;
  currentView.value = "hotel_search_result";
}
</script>

<style lang="css">
.home_page {
  width: 100%;
  height: 1600px;
  display: flex;
  flex-direction: column;
  background-color: rgb(212, 239, 252);
  background-repeat: no-repeat;
}

.header {
  width: 100%;
  height: 70px;
  flex-shrink: 0;
  background-color: rgba(232, 251, 248, 0.748);
}

.main_area {
  flex: 1;
  display: flex;
  width: 100%;
  min-height: 1030px;
}

.left_menu {
  width: 20%;
  background-color: rgb(202, 236, 245);
}

.center_area {
  flex: 1;
  background-image: url("/src/asset/picture/bk1.png");
  backdrop-filter: blur(6px);
  background-size: cover;
  background-position: center;
  overflow-y: auto;
}

.right_menu {
  width: 15%;
  background-color: rgb(198, 249, 247);
}

.footer {
  height: 100px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(
    135deg,
    rgba(230, 245, 255, 0.95),
    rgba(195, 230, 240, 0.92)
  );
  border-top: 1px solid rgba(120, 160, 180, 0.45);
  color: #2e465d;
  font-size: 14px;
  font-weight: 700;
}

.footer p {
  margin: 0;
}
</style>
