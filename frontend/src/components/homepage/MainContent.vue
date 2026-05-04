<template>
  <component
    class="main_page"
    :is="currentComponent"
    :hotel-results="hotelResults"
    :hotel-search-results="hotelSearchResults"
    @switch-view="emit('switch-view', $event)"
    @show-result="emit('show-result', $event)"
    @show-hotel-search-result="emit('show-hotel-search-result', $event)"
  />
</template>

<script setup lang="ts">
import { computed, type Component } from "vue";

import ProfileView from "@/components/user_components/profile.vue";
import HomeView from "@/components/homepage/home_view.vue";
import ChangePwd from "@/components/user_components/change_pwd.vue";
import SearchFlight from "@/components/search_components/SearchFlight.vue";
import SearchHotel from "@/components/search_components/SearchHotel.vue";
import HotelResult from "@/components/search_components/HotelResult.vue";
import HotelBookingRecordPage from "@/components/search_components/HotelBookingRecordPage.vue";
import type { HotelDestResult } from "@/types/hotelDestResult";
import HotelSearchResultView from "@/components/search_components/HotelSearchResult.vue";
import type { HotelSearchResult } from "@/types/hotelSearchResult";
import AirportSearch from "@/components/search_components/AirportSearch.vue";
import FlightBookingRecordPage from "@/components/search_components/FlightBookingRecordPage.vue";
import AttractionSearchPage from "@/components/search_components/AttractionSearchPage.vue";
import AttractionBookingRecordPage from "@/components/search_components/AttractionBookingRecordPage.vue";
import AboutPage from "@/components/contents/AboutPage.vue";

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

const props = defineProps<{
  currentView: ViewType;
  hotelResults: HotelDestResult[];
  hotelSearchResults: HotelSearchResult[];
}>();

const emit = defineEmits<{
  (e: "switch-view", view: ViewType): void;
  (e: "show-result", data: HotelDestResult[]): void;
  (e: "show-hotel-search-result", data: HotelSearchResult[]): void;
}>();

const viewMap: Record<ViewType, Component> = {
  home: HomeView,
  profile: ProfileView,
  change_pwd: ChangePwd,
  search_flight: SearchFlight,
  search_hotel: SearchHotel,
  hotel_result: HotelResult,
  hotel_search_result: HotelSearchResultView,
  hotel_booking_record_page: HotelBookingRecordPage,
  airport_search: AirportSearch,
  flight_booking_record_page: FlightBookingRecordPage,
  attraction_search_page: AttractionSearchPage,
  attraction_booking_record_page: AttractionBookingRecordPage,
  about_page: AboutPage,
};

const currentComponent = computed(() => {
  return viewMap[props.currentView];
});
</script>

<style lang="css">
.main_page {
  backdrop-filter: blur(6px);
  background-position: center;
  overflow-y: auto;
  height: 100%;
}
</style>
