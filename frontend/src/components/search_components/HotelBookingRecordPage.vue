<template>
  <div class="hotel_booking_page">
    <h2 class="page_title">My Hotel Bookings</h2>

    <div v-if="message" class="message">
      {{ message }}
    </div>

    <div v-if="hotelBookings.length === 0" class="empty_text">
      No hotel booking found.
    </div>

    <div v-else class="booking_list">
      <div
        v-for="item in hotelBookings"
        :key="item.booking.id"
        class="booking_card"
      >
        <img
          class="hotel_image"
          :src="item.hotel.main_photo"
          :alt="item.hotel.name"
        />

        <div class="booking_content">
          <div class="booking_header">
            <div>
              <h3>{{ item.hotel.name }}</h3>
              <p class="hotel_subtitle">Hotel Booking #{{ item.booking.id }}</p>
            </div>

            <span class="booking_state">
              {{ item.booking.state }}
            </span>
          </div>

          <div class="booking_info">
            <p>
              Review: {{ item.hotel.review_score }} / 10 -
              {{ item.hotel.review_score_word }}
            </p>
            <p>Review Count: {{ item.hotel.review_count }}</p>
            <p>Class: {{ item.hotel.property_class }} stars</p>
            <p>Agent ID: {{ item.booking.agent_id }}</p>
            <p>Check-in: {{ item.booking.checkin_date }}</p>
            <p>Check-out: {{ item.booking.checkout_date }}</p>
            <p>
              Price:
              {{ item.booking.currency }}
              {{ item.booking.price.toFixed(2) }}
            </p>
            <p>Booked At: {{ formatDateTime(item.booking.created_at) }}</p>
            <button
              class="cancel_button"
              @click="cancelHotelBooking(item.booking.id)"
            >
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { travel_request } from "@/router/api_client";
import { onMounted } from "vue";
interface HotelBookingRecord {
  id: number;
  owner_id: number;
  hotel_id: number;
  agent_id: number;
  checkin_date: string;
  checkout_date: string;
  price: number;
  currency: string;
  state: string;
  created_at: string;
}

interface HotelRecord {
  id: number;
  third_party_id: number;
  name: string;
  review_score: number;
  review_score_word: string;
  review_count: number;
  property_class: number;
  latitude: number;
  longitude: number;
  main_photo: string;
  sub_photo_1: string;
  sub_photo_2: string;
  sub_photo_3: string;
}

interface HotelBookingItem {
  booking: HotelBookingRecord;
  hotel: HotelRecord;
}

interface BookingResponse {
  state: "success" | "fail";
  result: HotelBookingItem[];
  message?: string;
}

const hotelBookings = ref<HotelBookingItem[]>([]);
const message = ref<string>("");

onMounted(() => {
  getHotelBookings();
});

function formatDateTime(value: string): string {
  return value.replace("T", " ").slice(0, 19);
}

async function getHotelBookings(): Promise<void> {
  const userId = localStorage.getItem("user_id");

  if (userId === null) {
    message.value = "User id not found. Please log in again.";
    return;
  }

  const res = await fetch(
    travel_request(
      `book/get/hotel_booking?user_id=${encodeURIComponent(userId)}`,
    ),
    {
      method: "GET",
    },
  );

  if (!res.ok) {
    message.value = `Failed to load bookings: ${res.status}`;
    return;
  }

  const data: BookingResponse = await res.json();

  if (data.state === "success") {
    hotelBookings.value = data.result;
  } else {
    message.value = data.message ?? "Failed to load bookings.";
  }
}

async function cancelHotelBooking(bookingId: number): Promise<void> {
  const confirmed = window.confirm(
    "Are you sure you want to cancel this hotel booking?",
  );

  if (!confirmed) {
    return;
  }

  const res = await fetch(
    travel_request(
      `book/delete/hotel_booking?booking_id=${encodeURIComponent(bookingId)}`,
    ),
    {
      method: "DELETE",
    },
  );

  if (!res.ok) {
    message.value = `Failed to cancel booking: ${res.status}`;
    return;
  }

  await getHotelBookings();
}
</script>

<style scoped>
.hotel_booking_page {
  width: 100%;
  height: 100%;
  padding: 24px;
  box-sizing: border-box;
  overflow-y: auto;
}

.page_title {
  margin: 0 0 20px 0;
  font-size: 24px;
  font-weight: 700;
  color: #1f2933;
  text-align: center;
}

.message {
  margin-bottom: 16px;
  color: #b91c1c;
  font-weight: 600;
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
  gap: 16px;
}

.booking_card {
  padding: 18px;
  border-radius: 14px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 1px solid rgba(160, 190, 205, 0.7);
}

.booking_header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.booking_header h3 {
  margin: 0;
  font-size: 20px;
}

.booking_state {
  padding: 5px 12px;
  border-radius: 999px;
  background-color: #d1fae5;
  color: #065f46;
  font-size: 14px;
  font-weight: 700;
}

.booking_info p {
  margin: 5px 0;
  font-size: 15px;
  color: #333;
}
.booking_card {
  display: flex;
  gap: 18px;
  padding: 18px;
  border-radius: 14px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 1px solid rgba(160, 190, 205, 0.7);
}

.hotel_image {
  width: 160px;
  height: 160px;
  object-fit: cover;
  border-radius: 12px;
  flex-shrink: 0;
}

.booking_content {
  flex: 1;
}

.hotel_subtitle {
  margin: 4px 0 0 0;
  font-size: 14px;
  color: #666;
}

.cancel_button {
  margin-top: 12px;
  width: 120px;
  height: 36px;
  border: none;
  border-radius: 8px;
  background-color: #ef4444;
  color: white;
  cursor: pointer;
}

.cancel_button:hover {
  background-color: #dc2626;
}
</style>
