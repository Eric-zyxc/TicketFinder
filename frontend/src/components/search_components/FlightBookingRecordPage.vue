<template>
  <div class="flight_booking_page">
    <h2 class="page_title">My Flight Bookings</h2>

    <div v-if="message" class="message">
      {{ message }}
    </div>

    <div v-if="flightBookings.length === 0" class="empty_text">
      No flight booking found.
    </div>

    <div v-else class="booking_list">
      <div
        v-for="item in flightBookings"
        :key="item.booking.id"
        class="booking_card"
      >
        <img
          class="airline_logo"
          :src="item.flight.airline_logo"
          :alt="item.flight.airline_name"
        />

        <div class="booking_content">
          <div class="booking_header">
            <div>
              <h3>
                {{ item.flight.departure_airport }}
                →
                {{ item.flight.arrival_airport }}
              </h3>
              <p class="flight_subtitle">
                {{ item.flight.airline_name }} ({{ item.flight.airline_code }})
              </p>
            </div>

            <span class="booking_state">
              {{ item.booking.state }}
            </span>
          </div>

          <div class="booking_info">
            <p>
              Route:
              {{ item.flight.departure_city }}
              →
              {{ item.flight.arrival_city }}
            </p>

            <p>Departure: {{ formatDateTime(item.flight.departure_time) }}</p>
            <p>Arrival: {{ formatDateTime(item.flight.arrival_time) }}</p>
            <p>Duration: {{ formatDuration(item.flight.duration_seconds) }}</p>
            <p>Stops: {{ item.flight.stops }}</p>
            <p>Cabin: {{ item.booking.cabin_class }}</p>
            <p>Adults: {{ item.booking.adult }}</p>
            <p>Children: {{ item.booking.children }}</p>
            <p>Agent ID: {{ item.booking.agent_id }}</p>

            <p>
              Price:
              {{ item.booking.currency }}
              {{ item.booking.price.toFixed(2) }}
            </p>

            <p>Booked At: {{ formatDateTime(item.booking.created_at) }}</p>
            <button
              class="cancel_button"
              @click="cancelFlightBooking(item.booking.id)"
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
import { ref, onMounted } from "vue";
import { travel_request } from "@/router/api_client";

interface FlightBookingRecord {
  id: number;
  flight_id: number;
  adult: number;
  price: number;
  state: string;
  agent_id: number;
  owner_id: number;
  cabin_class: string;
  children: string;
  currency: string;
  created_at: string;
}

interface FlightRecord {
  id: number;
  token: string;
  airline_name: string;
  airline_code: string;
  airline_logo: string;
  departure_airport: string;
  departure_city: string;
  arrival_airport: string;
  arrival_city: string;
  departure_time: string;
  arrival_time: string;
  duration_seconds: number;
  stops: number;
}

interface FlightBookingItem {
  booking: FlightBookingRecord;
  flight: FlightRecord;
}

interface FlightBookingResponse {
  state: "success" | "fail";
  result: FlightBookingItem[];
  message?: string;
}

const flightBookings = ref<FlightBookingItem[]>([]);
const message = ref<string>("");

onMounted(() => {
  getFlightBookings();
});

async function getFlightBookings(): Promise<void> {
  const userId = localStorage.getItem("user_id");

  if (userId === null) {
    message.value = "User id not found. Please log in again.";
    return;
  }

  const res = await fetch(
    travel_request(
      `book/get/flight_booking?user_id=${encodeURIComponent(userId)}`,
    ),
    {
      method: "GET",
    },
  );

  if (!res.ok) {
    message.value = `Failed to load flight bookings: ${res.status}`;
    return;
  }

  const data: FlightBookingResponse = await res.json();

  if (data.state === "success") {
    flightBookings.value = data.result;
  } else {
    message.value = data.message ?? "Failed to load flight bookings.";
  }
}

function formatDateTime(value: string): string {
  return value.replace("T", " ").slice(0, 19);
}

function formatDuration(seconds: number): string {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  return `${hours}h ${minutes}m`;
}

async function cancelFlightBooking(bookingId: number): Promise<void> {
  const confirmed = window.confirm(
    "Are you sure you want to cancel this booking?",
  );

  if (!confirmed) {
    return;
  }

  const res = await fetch(
    travel_request(
      `book/delete/flight_booking?booking_id=${encodeURIComponent(bookingId)}`,
    ),
    {
      method: "DELETE",
    },
  );

  if (!res.ok) {
    message.value = `Failed to cancel booking: ${res.status}`;
    return;
  }

  await getFlightBookings();
}
</script>

<style scoped>
.flight_booking_page {
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
  display: flex;
  gap: 18px;
  padding: 18px;
  border-radius: 14px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 1px solid rgba(160, 190, 205, 0.7);
}

.airline_logo {
  width: 130px;
  height: 130px;
  object-fit: contain;
  border-radius: 12px;
  background-color: white;
  flex-shrink: 0;
}

.booking_content {
  flex: 1;
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

.flight_subtitle {
  margin: 4px 0 0 0;
  font-size: 14px;
  color: #666;
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
