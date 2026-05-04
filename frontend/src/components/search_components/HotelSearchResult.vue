<template>
  <div class="hotel_result_page">
    <div class="agent_drop_down">
      <label>Purchase from:</label>

      <select v-model="selectedAgentId">
        <option disabled value="">Select an agent</option>

        <option v-for="agent in agents" :key="agent.id" :value="agent.id">
          {{ agent.name }}
        </option>
      </select>
    </div>

    <div v-if="hotelSearchResults.length === 0" class="empty_text">
      No hotel found.
    </div>

    <div v-else class="hotel_result_list">
      <div
        v-for="item in hotelSearchResults"
        :key="item.hotel_id"
        class="hotel_card"
      >
        <img class="hotel_image" :src="item.main_photo" :alt="item.name" />

        <div class="hotel_info">
          <h3 class="hotel_name">{{ item.name }}</h3>

          <p class="hotel_text">
            Review: {{ item.review_score }} / 10 - {{ item.review_score_word }}
          </p>

          <p class="hotel_text">Reviews: {{ item.review_count }}</p>

          <p class="hotel_text">Class: {{ item.property_class }} stars</p>

          <p class="hotel_text">
            Check-in: {{ item.checkin_date }} {{ item.checkin_from_time }} -
            {{ item.checkin_until_time }}
          </p>

          <p class="hotel_text">
            Check-out: {{ item.checkout_date }} {{ item.checkout_from_time }} -
            {{ item.checkout_until_time }}
          </p>

          <p class="hotel_price">Price: ${{ item.gross_price.toFixed(2) }}</p>

          <p class="hotel_text">
            Extra Fees: ${{ item.excluded_price.toFixed(2) }}
          </p>

          <button class="booking_button" @click="booking(item)">Booking</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { HotelSearchResult } from "@/types/hotelSearchResult";
import type { HotelBookingPayload } from "@/types/hotelBooking";
import { travel_request } from "@/router/api_client";

import { ref } from "vue";

interface Agent {
  id: number;
  name: string;
}

const agents = ref<Agent[]>([
  { id: 1, name: "Expedia" },
  { id: 2, name: "Booking.com" },
  { id: 3, name: "TripAdvisor" },
  { id: 4, name: "Kayak" },
  { id: 5, name: "Priceline" },
  { id: 6, name: "Agoda" },
  { id: 7, name: "Travelocity" },
  { id: 8, name: "Orbitz" },
  { id: 9, name: "CheapTickets" },
  { id: 10, name: "Hotwire" },
  { id: 11, name: "Airbnb" },
  { id: 12, name: "Turo" },
  { id: 13, name: "Hopper" },
  { id: 14, name: "Skyscanner" },
  { id: 15, name: "Trivago" },
  { id: 16, name: "MakeMyTrip" },
  { id: 17, name: "Ctrip" },
  { id: 18, name: "Traveloka" },
  { id: 19, name: "Lastminute" },
  { id: 20, name: "Cleartrip" },
]);

const selectedAgentId = ref<number | "">("");
defineProps<{
  hotelSearchResults: HotelSearchResult[];
}>();

interface BookingResponse {
  state: "success" | "fail";
  message?: string;
}
async function booking(item: HotelSearchResult): Promise<void> {
  console.log(item);
  const userId = Number(localStorage.getItem("user_id"));

  if (!userId) {
    alert("User id not found. Please log in again.");
    return;
  }
  if (!selectedAgentId.value) {
    alert("Please select an agent");
    return;
  }
  const payload: HotelBookingPayload = {
    third_party_id: item.hotel_id,
    name: item.name,
    latitude: item.latitude,
    longitude: item.longitude,
    main_photo: item.main_photo,
    sub_photo_1: item.photo_urls[0] ?? "",
    sub_photo_2: item.photo_urls[1] ?? "",
    sub_photo_3: item.photo_urls[2] ?? "",
    review_score: item.review_score,
    review_score_word: item.review_score_word,
    review_count: item.review_count,
    property_class: item.property_class,
    owner_id: userId,
    agent_id: selectedAgentId.value,
    checkin_date: item.checkin_date,
    checkout_date: item.checkout_date,
    price: item.gross_price,
    currency: "USD",
    excluded_price: item.excluded_price,
  };

  const res = await fetch(travel_request("book/hotel"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data: BookingResponse = await res.json();

  if (data.state === "success") {
    alert("Booking successful");
  } else {
    alert(data.message ?? "Booking failed");
  }

  
}
</script>

<style scoped>
.hotel_result_page {
  width: 100%;
  height: 100%;
  padding: 24px;
  box-sizing: border-box;
  overflow-y: auto;
}

.empty_text {
  text-align: center;
  font-size: 18px;
  color: #555;
  margin-top: 40px;
}

.hotel_result_list {
  display: flex;
  flex-direction: column;
  gap: 18px;
  height: 800px;
}

.hotel_card {
  display: flex;
  gap: 18px;
  padding: 16px;
  border-radius: 14px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 1px solid rgba(160, 190, 205, 0.7);
  box-sizing: border-box;
}

.hotel_image {
  width: 170px;
  height: 170px;
  object-fit: cover;
  border-radius: 12px;
  flex-shrink: 0;
}

.hotel_info {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.hotel_name {
  margin: 0 0 8px 0;
  font-size: 22px;
  font-weight: 700;
  color: #1f2933;
}

.hotel_text {
  margin: 3px 0;
  font-size: 14px;
  color: #444;
}

.hotel_price {
  margin: 8px 0 3px 0;
  font-size: 16px;
  font-weight: 700;
  color: #1f2933;
}

.booking_button {
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

.booking_button:hover {
  background-color: #2f8ee5;
}

.agent_drop_down {
  margin-top: 12px;
  display: flex;
  gap: 10px;
  align-items: center;
}

.agent_drop_down select {
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
}
</style>
