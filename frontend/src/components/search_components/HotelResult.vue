<template>
  <div class="result_page">
    <div class="date_selection">
      <div class="date_row">
        <label>Check-in:</label>
        <input v-model="checkInDate" type="date" />
      </div>

      <div class="date_row">
        <label>Check-out:</label>
        <input v-model="checkOutDate" type="date" />
      </div>

      <div class="date_row">
        <label>Min Price:</label>
        <input v-model="min_price" />
      </div>
      <div class="date_row">
        <label>Max Price:</label>
        <input v-model="max_price" />
      </div>
    </div>

    <div v-if="hotelResults.length === 0" class="empty_text">
      No result found.
    </div>
    <div v-else class="result_list">
      <div
        v-for="item in props.hotelResults"
        :key="item.dest_id"
        class="result_card"
      >
        <img class="result_image" :src="item.image_url" :alt="item.name" />

        <div class="result_info">
          <h3 class="result_name">{{ item.name }}</h3>

          <p class="result_label">{{ item.label }}</p>

          <p class="result_text">Type: {{ item.search_type }}</p>

          <p class="result_text">Region: {{ item.region }}</p>

          <p class="result_text">Country: {{ item.country }}</p>

          <p class="result_text">Hotels: {{ item.nr_hotels }}</p>

          <button class="search_button" @click="search_hotel(item)">
            Search This Location
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import type { HotelDestResult } from "@/types/hotelDestResult";
import type { HotelSearchResult } from "@/types/hotelSearchResult";
import { travel_request } from "@/router/api_client";

const checkInDate = ref<string>("");
const checkOutDate = ref<string>("");
const max_price = ref<string>("");
const min_price = ref<string>("");

const emit = defineEmits<{
  (e: "show-hotel-search-result", data: HotelSearchResult[]): void;
}>();

const props = withDefaults(
  defineProps<{
    hotelResults?: HotelDestResult[];
  }>(),
  {
    hotelResults: () => [],
  },
);

async function search_hotel(item: HotelDestResult): Promise<void> {
  if (checkInDate.value === "" || checkOutDate.value === "") {
    alert("Please select check-in and check-out dates.");
    return;
  }

  if (checkOutDate.value < checkInDate.value) {
    alert("Check out date cannot be earlier than check in date!");
    return;
  }

  const body = {
    dest_id: item.dest_id,
    search_type: item.search_type,
    arrival_date: checkInDate.value,
    departure_date: checkOutDate.value,
    price_min: min_price.value === "" ? null : Number(min_price.value),
    price_max: max_price.value === "" ? null : Number(max_price.value),
  };

  const res = await fetch(travel_request("search/hotel"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    const errorText = await res.text();
    console.error("Search hotel failed:", res.status, errorText);
    alert(`Search hotel failed: ${res.status}`);
    return;
  }

  const data = await res.json();
  emit("show-hotel-search-result", data.result);
}
</script>

<style scoped>
.result_page {
  width: 100%;
  height: 100%;
  padding: 24px;
  box-sizing: border-box;
  overflow-y: auto;
}

.date_selection {
  background-color: rgb(211, 236, 243);
  padding: 20px;
  margin: 9px;
  width: 30%;
  border-radius: 10px;
}

.empty_text {
  text-align: center;
  font-size: 18px;
  color: #555;
  margin-top: 40px;
}

.result_list {
  display: flex;
  flex-direction: column;
  gap: 18px;
  height: 700px;
}

.result_card {
  display: flex;
  align-items: stretch;
  gap: 18px;
  padding: 16px;
  border-radius: 14px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 1px solid rgba(160, 190, 205, 0.7);
  box-sizing: border-box;
}

.result_image {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 12px;
  flex-shrink: 0;
}

.result_info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.result_name {
  margin: 0 0 6px 0;
  font-size: 22px;
  font-weight: 700;
  color: #1f2933;
}

.result_label {
  margin: 0 0 10px 0;
  font-size: 15px;
  color: #34495e;
}

.result_text {
  margin: 3px 0;
  font-size: 14px;
  color: #444;
}

.search_button {
  margin-top: auto;
  align-self: flex-start;
  min-width: 120px;
  height: 38px;
  padding: 0 18px;
  border: none;
  border-radius: 8px;
  background-color: #409eff;
  color: white;
  font-size: 15px;
  cursor: pointer;
}

.search_button:hover {
  background-color: #2f8ee5;
}
</style>
