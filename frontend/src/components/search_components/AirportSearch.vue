<template>
  <div class="page">
    <!-- Step 1: Search Form -->
    <div v-if="showSearchPanel" class="search_panel">
      <p class="title">Search Flight</p>

      <div class="form_row">
        <label>Fly From:</label>
        <input v-model="fromLocation" placeholder="Example: San Jose" />
      </div>

      <div class="form_row">
        <label>Fly To:</label>
        <input v-model="toLocation" placeholder="Example: Los Angeles" />
      </div>

      <div class="form_row">
        <label>Departure:</label>
        <input v-model="departureDate" type="date" />
      </div>

      <div class="form_row">
        <label>Adults:</label>
        <input v-model="adults" type="number" min="1" />
      </div>

      <div class="form_row">
        <label>Children:</label>
        <input v-model="children" placeholder="Example: 5,8 or empty" />
      </div>

      <div class="form_row">
        <label>Agent:</label>
        <select v-model="selectedAgentId">
          <option disabled value="">Select agent</option>
          <option v-for="agent in agents" :key="agent.id" :value="agent.id">
            {{ agent.name }}
          </option>
        </select>
      </div>

      <button class="search_button" @click="searchAirports">
        Search Airports
      </button>
    </div>

    <p v-if="message" class="message">{{ message }}</p>

    <!-- Step 2: Airport Selection -->
    <div v-if="showAirportSelection" class="airport_selection_area">
      <div class="airport_column">
        <h3>Fly From</h3>

        <div
          v-for="airport in fromAirportResults"
          :key="airport.id"
          :class="[
            'airport_card',
            { selected: selectedFromAirport?.id === airport.id },
          ]"
          @click="selectedFromAirport = airport"
        >
          <img
            class="airport_image"
            :src="airport.photoUri"
            :alt="airport.name"
          />

          <div class="airport_info">
            <h4>{{ airport.name }}</h4>
            <p>Code: {{ airport.code }}</p>
            <p>{{ airport.cityName }}, {{ airport.regionName }}</p>
            <p>{{ airport.countryName }}</p>
          </div>
        </div>
      </div>

      <div class="airport_column">
        <h3>Fly To</h3>

        <div
          v-for="airport in toAirportResults"
          :key="airport.id"
          :class="[
            'airport_card',
            { selected: selectedToAirport?.id === airport.id },
          ]"
          @click="selectedToAirport = airport"
        >
          <img
            class="airport_image"
            :src="airport.photoUri"
            :alt="airport.name"
          />

          <div class="airport_info">
            <h4>{{ airport.name }}</h4>
            <p>Code: {{ airport.code }}</p>
            <p>{{ airport.cityName }}, {{ airport.regionName }}</p>
            <p>{{ airport.countryName }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showAirportSelection" class="flight_action_bar">
      <button class="search_button" @click="searchFlights">
        Search Flight
      </button>
    </div>

    <!-- Step 3: Flight Results -->
    <div v-if="showFlightResults" class="flight_result_list">
      <button class="back_button" @click="resetSearch">New Search</button>

      <div
        v-for="flight in flightSearchList"
        :key="flight.token"
        class="flight_card"
      >
        <img
          class="airline_logo"
          :src="flight.airline_logo"
          :alt="flight.airline_name"
        />

        <div class="flight_info">
          <h3>{{ flight.airline_name }} ({{ flight.airline_code }})</h3>

          <p>
            From: {{ flight.departure_city }} ({{ flight.departure_airport }})
          </p>

          <p>To: {{ flight.arrival_city }} ({{ flight.arrival_airport }})</p>

          <p>Departure: {{ formatDateTime(flight.departure_time) }}</p>
          <p>Arrival: {{ formatDateTime(flight.arrival_time) }}</p>
          <p>Duration: {{ formatDuration(flight.duration_seconds) }}</p>
          <p>Stops: {{ flight.stops }}</p>

          <p class="flight_price">
            Price: {{ flight.currency }} {{ flight.price.toFixed(2) }}
          </p>
        </div>

        <button class="booking_button" @click="bookFlight(flight)">
          Booking
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { travel_request } from "@/router/api_client";

interface AirportResult {
  id: string;
  type: string;
  name: string;
  code: string;
  city: string;
  cityName: string;
  regionName: string;
  country: string;
  countryName: string;
  countryNameShort: string;
  photoUri: string;
  distanceToCity: {
    value: number;
    unit: string;
  };
  parent: string;
}

interface AirportSearchResponse {
  state: "success" | "fail";
  result: AirportResult[];
  message?: string;
}

interface FlightSearchResult {
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
  price: number;
  currency: string;
}

interface FlightSearchResponse {
  state: "success" | "fail";
  result: FlightSearchResult[];
  message?: string;
}

interface Agent {
  id: number;
  name: string;
}

interface FlightBookingPayload {
  owner_id: number;
  agent_id: number;
  cabin_class: string;
  adult: number;
  children: number;
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
  price: number;
  currency: string;
}

interface BookingResponse {
  state: "success" | "fail";
  message?: string;
}

const showSearchPanel = ref<boolean>(true);
const showAirportSelection = ref<boolean>(false);
const showFlightResults = ref<boolean>(false);
const fromLocation = ref<string>("San Jose");
const toLocation = ref<string>("Los Angeles");
const departureDate = ref<string>("");
const adults = ref<string>("1");
const children = ref<string>("");
const message = ref<string>("");
const fromAirportResults = ref<AirportResult[]>([]);
const toAirportResults = ref<AirportResult[]>([]);
const selectedFromAirport = ref<AirportResult | null>(null);
const selectedToAirport = ref<AirportResult | null>(null);
const flightSearchList = ref<FlightSearchResult[]>([]);
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

async function searchAirports(): Promise<void> {
  if (fromLocation.value === "" || toLocation.value === "") {
    message.value = "Fly from and fly to cannot be empty.";
    return;
  }

  if (departureDate.value === "") {
    message.value = "Please select departure date.";
    return;
  }

  const fromRes = await fetch(
    travel_request(
      `search/airports?location=${encodeURIComponent(fromLocation.value)}`,
    ),
    {
      method: "POST",
    },
  );

  const toRes = await fetch(
    travel_request(
      `search/airports?location=${encodeURIComponent(toLocation.value)}`,
    ),
    {
      method: "POST",
    },
  );

  if (!fromRes.ok || !toRes.ok) {
    message.value = "Airport search failed.";
    return;
  }

  const fromData: AirportSearchResponse = await fromRes.json();
  const toData: AirportSearchResponse = await toRes.json();

  if (fromData.state !== "success" || toData.state !== "success") {
    message.value = "Airport search failed.";
    return;
  }

  fromAirportResults.value = fromData.result;
  toAirportResults.value = toData.result;

  selectedFromAirport.value = null;
  selectedToAirport.value = null;

  showSearchPanel.value = false;
  showAirportSelection.value = true;
  showFlightResults.value = false;
  message.value = "";
}

async function searchFlights(): Promise<void> {
  if (selectedFromAirport.value === null || selectedToAirport.value === null) {
    message.value = "Please select both departure and arrival airports.";
    return;
  }

  const body = {
    from_id: selectedFromAirport.value.id,
    to_id: selectedToAirport.value.id,
    departure_date: departureDate.value,
    adults: Number(adults.value || 1),
    children: children.value,
  };

  const res = await fetch(travel_request("search/flights"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });

  if (!res.ok) {
    message.value = `Flight search failed: ${res.status}`;
    return;
  }

  const data: FlightSearchResponse = await res.json();

  if (data.state !== "success") {
    message.value = data.message ?? "Flight search failed.";
    return;
  }

  flightSearchList.value = data.result;

  showSearchPanel.value = false;
  showAirportSelection.value = false;
  showFlightResults.value = true;
  message.value = "";
}

async function bookFlight(flight: FlightSearchResult): Promise<void> {
  const userId = Number(localStorage.getItem("user_id"));

  if (!userId) {
    alert("User id not found. Please log in again.");
    return;
  }

  if (selectedAgentId.value === "") {
    alert("Please select an agent.");
    return;
  }

  const payload: FlightBookingPayload = {
    owner_id: userId,
    agent_id: selectedAgentId.value,
    cabin_class: "ECONOMY",
    adult: Number(adults.value || 1),
    children: Number(children.value || 0),
    token: flight.token,
    airline_name: flight.airline_name,
    airline_code: flight.airline_code,
    airline_logo: flight.airline_logo,
    departure_airport: flight.departure_airport,
    departure_city: flight.departure_city,
    arrival_airport: flight.arrival_airport,
    arrival_city: flight.arrival_city,
    departure_time: flight.departure_time,
    arrival_time: flight.arrival_time,
    duration_seconds: flight.duration_seconds,
    stops: flight.stops,
    price: flight.price,
    currency: flight.currency,
  };

  const res = await fetch(travel_request("book/flight"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    alert(`Flight booking failed: ${res.status}`);
    return;
  }

  const data: BookingResponse = await res.json();

  if (data.state === "success") {
    alert("Flight booking successful");
  } else {
    alert(data.message ?? "Flight booking failed");
  }
}

function resetSearch(): void {
  showSearchPanel.value = true;
  showAirportSelection.value = false;
  showFlightResults.value = false;

  fromAirportResults.value = [];
  toAirportResults.value = [];
  flightSearchList.value = [];
  selectedFromAirport.value = null;
  selectedToAirport.value = null;
  message.value = "";
}

function formatDateTime(value: string): string {
  return value.replace("T", " ").slice(0, 16);
}

function formatDuration(seconds: number): string {
  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  return `${hours}h ${minutes}m`;
}
</script>

<style scoped>
.page {
  width: 100%;
  height: 100%;
  overflow-y: auto;
}

.search_panel {
  background-color: rgba(198, 221, 234, 0.672);
  width: 80%;
  margin: 120px auto 20px auto;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 12px 28px rgba(41, 82, 112, 0.14);
}

.title {
  margin: 20px;
  font-size: large;
  font-weight: 700;
}

.form_row {
  display: grid;
  grid-template-columns: 120px 1fr;
  align-items: center;
  margin-bottom: 14px;
  padding-inline: 10%;
}

.form_row label {
  font-size: 14px;
  font-weight: 600;
  color: #333;
  margin: 10px;
}

.form_row input {
  width: 100%;
  padding: 8px 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
  outline: none;
  box-sizing: border-box;
}

.form_row input:focus {
  border-color: #409eff;
  background-color: beige;
}

.search_button {
  margin: 20px 10%;
  min-width: 150px;
  padding: 10px;
  border: none;
  border-radius: 8px;
  background-color: #409eff;
  color: white;
  cursor: pointer;
}

.message {
  width: 80%;
  margin: 10px auto;
  color: #b91c1c;
  font-weight: 600;
}

.airport_selection_area {
  width: 90%;
  margin: 20px auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.airport_column {
  height: 650px;
  overflow-y: auto;
  background-color: rgba(243, 237, 211, 0.9);
  padding: 16px;
  border-radius: 12px;
}

.airport_column h3 {
  margin-top: 0;
  text-align: center;
}

.airport_card {
  display: flex;
  align-items: center;
  gap: 14px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 2px solid transparent;
  border-radius: 12px;
  padding: 12px;
  margin-bottom: 12px;
  cursor: pointer;
}

.airport_card.selected {
  border-color: #409eff;
  background-color: #e8f4ff;
}

.airport_image {
  width: 90px;
  height: 90px;
  object-fit: cover;
  border-radius: 10px;
  flex-shrink: 0;
}

.airport_info {
  flex: 1;
}

.airport_info h4 {
  margin: 0 0 6px 0;
  font-size: 16px;
}

.airport_info p {
  margin: 3px 0;
  font-size: 13px;
}

.flight_action_bar {
  width: 90%;
  margin: 0 auto 20px auto;
  text-align: center;
}

.flight_result_list {
  width: 90%;
  margin: 20px auto;
  height: 760px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.flight_card {
  display: flex;
  align-items: center;
  gap: 18px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 1px solid rgba(160, 190, 205, 0.7);
  border-radius: 12px;
  padding: 16px;
}

.airline_logo {
  width: 90px;
  height: 90px;
  object-fit: contain;
  border-radius: 10px;
  background-color: white;
  flex-shrink: 0;
}

.flight_info {
  flex: 1;
}

.flight_info h3 {
  margin: 0 0 8px 0;
  font-size: 20px;
}

.flight_info p {
  margin: 4px 0;
  font-size: 14px;
  color: #333;
}

.flight_price {
  font-weight: 700;
  color: #1f2933;
}

.booking_button,
.back_button {
  min-width: 120px;
  height: 38px;
  border: none;
  border-radius: 8px;
  background-color: #409eff;
  color: white;
  cursor: pointer;
}

.back_button {
  align-self: flex-start;
}

.booking_button:hover,
.back_button:hover,
.search_button:hover {
  background-color: #2f8ee5;
}
</style>
