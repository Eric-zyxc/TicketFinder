<template>
  <div class="attraction_booking_page">
    <h2 class="page_title">My Attraction Bookings</h2>

    <div v-if="message" class="message">
      {{ message }}
    </div>

    <div v-if="attractionBookings.length === 0" class="empty_text">
      No attraction booking found.
    </div>

    <div v-else class="booking_list">
      <div
        v-for="item in attractionBookings"
        :key="item.booking.id"
        class="booking_card"
      >
        <img
          class="attraction_image"
          :src="item.attraction.primary_photo"
          :alt="item.attraction.name"
        />

        <div class="booking_content">
          <div class="booking_header">
            <div>
              <h3>{{ item.attraction.name }}</h3>
              <p class="booking_subtitle">
                Attraction Booking #{{ item.booking.id }}
              </p>
            </div>

            <span class="booking_state">
              {{ item.booking.state }}
            </span>
          </div>

          <div class="booking_info">
            <p>City: {{ item.attraction.city }}</p>
            <p>Operator: {{ item.attraction.operator }}</p>
            <p>Agent ID: {{ item.booking.agent_id }}</p>
            <p>Language: {{ item.booking.language }}</p>
            <p>Start Time: {{ formatDateTime(item.booking.start_time) }}</p>
            <p>
              Price:
              {{ item.booking.currency }}
              {{ item.booking.price.toFixed(2) }}
            </p>
            <p>
              Free Cancellation:
              {{ item.attraction.free_cancellation ? "Yes" : "No" }}
            </p>
            <p>Booked At: {{ formatDateTime(item.booking.created_at) }}</p>
          </div>

          <p class="short_description">
            {{ item.attraction.short_description }}
          </p>

          <button
            class="cancel_button"
            @click="cancelAttractionBooking(item.booking.id)"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { travel_request } from "@/router/api_client";

interface AttractionBookingRecord {
  id: number;
  owner_id: number;
  attraction_id: number;
  agent_id: number;
  time_slot_id: string;
  offer_id: string;
  offer_item_id: string;
  start_time: string;
  language: string;
  price: number;
  currency: string;
  state: string;
  created_at: string;
}

interface AttractionRecord {
  id: number;
  third_party_id: string;
  slug: string;
  name: string;
  description: string;
  short_description: string;
  operator: string;
  city: string;
  departure_address: string;
  arrival_address: string;
  primary_photo: string;
  free_cancellation: boolean;
  sub_photo_1: string;
  sub_photo_2: string;
  sub_photo_3: string;
  languages: string;
  whats_included: string;
  not_included: string;
}

interface AttractionBookingItem {
  booking: AttractionBookingRecord;
  attraction: AttractionRecord;
}

interface AttractionBookingResponse {
  state: "success" | "fail";
  result: AttractionBookingItem[];
  message?: string;
}

interface DeleteBookingResponse {
  state: "success" | "fail";
  message?: string;
}

const attractionBookings = ref<AttractionBookingItem[]>([]);
const message = ref<string>("");

onMounted(() => {
  getAttractionBookings();
});

async function getAttractionBookings(): Promise<void> {
  const userId = localStorage.getItem("user_id");

  if (userId === null) {
    message.value = "User id not found. Please log in again.";
    return;
  }

  const res = await fetch(
    travel_request(
      `book/get/attraction_booking?user_id=${encodeURIComponent(userId)}`,
    ),
    {
      method: "GET",
    },
  );

  if (!res.ok) {
    message.value = `Failed to load attraction bookings: ${res.status}`;
    return;
  }

  const data: AttractionBookingResponse = await res.json();

  if (data.state === "success") {
    attractionBookings.value = data.result;
    message.value = "";
  } else {
    message.value = data.message ?? "Failed to load attraction bookings.";
  }
}

async function cancelAttractionBooking(bookingId: number): Promise<void> {
  const confirmed = window.confirm(
    "Are you sure you want to cancel this attraction booking?",
  );

  if (!confirmed) {
    return;
  }

  const res = await fetch(
    travel_request(
      `book/delete/attraction_booking?booking_id=${encodeURIComponent(
        bookingId,
      )}`,
    ),
    {
      method: "DELETE",
    },
  );

  if (!res.ok) {
    alert(`Cancel attraction booking failed: ${res.status}`);
    return;
  }

  const data: DeleteBookingResponse = await res.json();

  if (data.state === "success") {
    alert("Attraction booking cancelled successfully.");
    await getAttractionBookings();
  } else {
    alert(data.message ?? "Cancel attraction booking failed.");
  }
}

function formatDateTime(value: string | null | undefined): string {
  if (!value) {
    return "N/A";
  }

  return value.replace("T", " ").slice(0, 19);
}
</script>

<style scoped>
.attraction_booking_page {
  width: 100%;
  height: 100%;
  padding: 24px;
  box-sizing: border-box;
  overflow-y: auto;
}

.page_title {
  margin: 0 0 20px 0;
  font-size: 24px;
  font-weight: 800;
  color: #1f2933;
}

.message {
  margin-bottom: 16px;
  color: #b91c1c;
  font-weight: 700;
}

.empty_text {
  text-align: center;
  margin-top: 40px;
  font-size: 18px;
  color: #555;
}

.booking_list {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.booking_card {
  display: flex;
  gap: 18px;
  padding: 18px;
  border-radius: 16px;
  background-color: rgba(238, 248, 252, 0.92);
  border: 1px solid rgba(160, 190, 205, 0.7);
  box-shadow: 0 10px 22px rgba(41, 82, 112, 0.1);
}

.attraction_image {
  width: 170px;
  height: 170px;
  object-fit: cover;
  border-radius: 14px;
  flex-shrink: 0;
  background-color: white;
}

.booking_content {
  flex: 1;
}

.booking_header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 10px;
}

.booking_header h3 {
  margin: 0;
  font-size: 21px;
  color: #1f2933;
}

.booking_subtitle {
  margin: 5px 0 0 0;
  font-size: 14px;
  color: #666;
}

.booking_state {
  padding: 6px 13px;
  border-radius: 999px;
  background-color: #d1fae5;
  color: #065f46;
  font-size: 14px;
  font-weight: 800;
  flex-shrink: 0;
}

.booking_info {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 4px 18px;
}

.booking_info p {
  margin: 4px 0;
  font-size: 15px;
  color: #333;
}

.short_description {
  margin: 12px 0 0 0;
  color: #4b5563;
  line-height: 1.45;
}

.cancel_button {
  margin-top: 14px;
  width: 120px;
  height: 36px;
  border: none;
  border-radius: 8px;
  background-color: #ef4444;
  color: white;
  font-weight: 700;
  cursor: pointer;
}

.cancel_button:hover {
  background-color: #dc2626;
}
</style>
