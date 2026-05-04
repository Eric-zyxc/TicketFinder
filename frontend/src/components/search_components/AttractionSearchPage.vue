<template>
  <div class="attraction_page">
    <div class="search_panel" v-if="showSearchPanel">
      <h2>Search Attraction Location</h2>

      <div class="form_row">
        <label>Location:</label>
        <input v-model="location" placeholder="Example: San Jose CA" />
      </div>

      <button class="search_button" @click="searchAttractionLocation">
        Search Location
      </button>
    </div>

    <p v-if="message" class="message">{{ message }}</p>

    <div v-if="showLocationResult">
      <div v-if="locationResults.length > 0" class="location_result_list">
        <div
          v-for="item in locationResults"
          :key="item.id"
          class="location_card"
        >
          <div class="location_info">
            <h3>{{ item.cityName }}</h3>
            <p>Country: {{ item.countryCode.toUpperCase() }}</p>
            <p>City UFI: {{ item.cityUfi }}</p>
          </div>

          <div class="location_action">
            <input v-model="item.searchDate" type="date" />

            <button class="action_button" @click="searchThisLocation(item)">
              Search this location
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showAttractionResult" class="attraction_list_panel">
      <h2>Attraction Results</h2>

      <div v-if="attractionList.length === 0" class="empty_text">
        Select a location and date to search attractions.
      </div>

      <div v-else class="attraction_result_list">
        <div
          v-for="attraction in attractionList"
          :key="attraction.id"
          class="attraction_card"
        >
          <img
            class="attraction_image"
            :src="attraction.photo"
            :alt="attraction.name"
          />

          <div class="attraction_info">
            <h3>{{ attraction.name }}</h3>

            <p class="description">
              {{ attraction.short_description }}
            </p>

            <p>City: {{ attraction.city }}</p>

            <p>
              Price:
              {{ attraction.currency }}
              {{
                attraction.price == null ? "N/A" : attraction.price.toFixed(2)
              }}
            </p>

            <p>
              Review:
              {{ attraction.review_average ?? "N/A" }}
              ({{ attraction.review_total ?? 0 }})
            </p>

            <p>
              Free Cancellation:
              {{ attraction.free_cancellation ? "Yes" : "No" }}
            </p>
          </div>

          <div class="attraction_buttons">
            <input v-model="attraction.checkDate" type="date" />

            <button
              class="availability_button"
              @click="checkAttractionAvailability(attraction)"
            >
              Check Availability
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showAttractionDetail" class="detail_panel">
      <button class="back_button" @click="backToAttractionList">Back</button>

      <div v-if="selectedDetail" class="detail_card">
        <div class="detail_top">
          <img
            class="detail_main_photo"
            :src="selectedDetail.primary_photo"
            :alt="selectedDetail.name"
          />

          <div class="detail_summary">
            <h2>{{ selectedDetail.name }}</h2>

            <p class="operator">
              Operator: {{ selectedDetail.operator ?? "N/A" }}
            </p>

            <p>City: {{ selectedDetail.location.city }}</p>

            <p>
              Price:
              {{ selectedDetail.price.currency }}
              {{ selectedDetail.price.amount }}
            </p>

            <p>
              Free Cancellation:
              {{ selectedDetail.cancellation.free ? "Yes" : "No" }}
            </p>

            <p>
              Languages:
              {{
                selectedDetail.languages.length > 0
                  ? selectedDetail.languages.join(", ")
                  : "N/A"
              }}
            </p>

            <div class="booking_controls">
              <label>Agent:</label>

              <select v-model="selectedAgentId">
                <option disabled value="">Select agent</option>
                <option
                  v-for="agent in agents"
                  :key="agent.id"
                  :value="agent.id"
                >
                  {{ agent.name }}
                </option>
              </select>
            </div>
          </div>
        </div>

        <div class="detail_section">
          <h3>Description</h3>
          <p class="long_text">{{ selectedDetail.description }}</p>
        </div>

        <div class="detail_grid">
          <div class="detail_section">
            <h3>What's Included</h3>
            <ul>
              <li v-for="item in selectedDetail.whatsIncluded" :key="item">
                {{ item }}
              </li>
            </ul>
          </div>

          <div class="detail_section">
            <h3>Not Included</h3>
            <ul>
              <li v-for="item in selectedDetail.notIncluded" :key="item">
                {{ item }}
              </li>
            </ul>
          </div>
        </div>

        <div class="photo_strip" v-if="selectedDetail.photos.length > 0">
          <img
            v-for="photo in selectedDetail.photos.slice(0, 8)"
            :key="photo"
            :src="photo"
            class="detail_photo"
          />
        </div>
      </div>

      <div class="availability_panel">
        <h2>Availability</h2>

        <div v-if="availabilitySlots.length === 0" class="empty_text">
          No availability found.
        </div>

        <div v-else class="slot_list">
          <div
            v-for="slot in availabilitySlots"
            :key="slot.time_slot_id"
            class="slot_card"
          >
            <h3>{{ formatDateTime(slot.start) }}</h3>
            <p>Full Day: {{ slot.full_day ? "Yes" : "No" }}</p>

            <div
              v-for="offer in slot.offers"
              :key="offer.offer_id"
              class="offer_card"
            >
              <h4>{{ offer.label }}</h4>
              <p>{{ offer.description }}</p>

              <div
                v-for="item in offer.items"
                :key="item.item_id"
                class="availability_item"
              >
                <p>Type: {{ item.type }}</p>
                <p>Language: {{ item.language ?? "N/A" }}</p>
                <p>Price: {{ item.currency }} {{ item.price }}</p>
                <p>Tickets Available: {{ item.tickets_available }}</p>
                <p>Max Group Size: {{ item.max_group_size }}</p>
                <p>
                  Free Cancellation:
                  {{ item.free_cancellation ? "Yes" : "No" }}
                </p>

                <button
                  class="book_button"
                  :class="{ booked: item.booked }"
                  :disabled="item.booked"
                  @click="bookAttraction(slot, offer, item)"
                >
                  {{ item.booked ? "Booked" : "Book" }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { travel_request } from "@/router/api_client";

interface RawAttractionLocationResult {
  id: string;
  __typename: string;
  title: string;
  productId: string;
  productSlug: string;
  taxonomySlug: string;
  cityUfi: number;
  cityName: string;
  countryCode: string;
}

interface AttractionLocationItem {
  id: string;
  cityName: string;
  countryCode: string;
  cityUfi: number;
  searchDate: string;
}

interface AttractionLocationResponse {
  state: "success" | "fail";
  result: RawAttractionLocationResult[];
  message?: string;
}

interface AttractionListItem {
  id: string;
  name: string;
  slug: string;
  short_description: string;
  price: number | null;
  currency: string;
  photo: string;
  city: string;
  ufi: number;
  free_cancellation: boolean;
  review_average: number | null;
  review_total: number | null;
  checkDate: string;
}

interface AttractionListResponse {
  state: "success" | "fail";
  result: Omit<AttractionListItem, "checkDate">[];
  message?: string;
}

interface AttractionDetail {
  id: string;
  name: string;
  description: string;
  price: {
    amount: number;
    currency: string;
  };
  location: {
    city: string;
    departure: string | null;
    arrival: string | null;
  };
  cancellation: {
    free: boolean;
  };
  offers: {
    id: string;
    availability_type: string;
  }[];
  whatsIncluded: string[];
  notIncluded: string[];
  languages: string[];
  operator: string | null;
  primary_photo: string;
  photos: string[];
  reviews: unknown[];
}

interface AttractionDetailResponse {
  state: "success" | "fail";
  result: AttractionDetail;
  message?: string;
}

interface AvailabilityItem {
  item_id: string;
  offer_item_id: string;
  type: string;
  label: string;
  language: string | null;
  price: number;
  currency: string;
  free_cancellation: boolean;
  cancellation_period: string | null;
  max_group_size: number | null;
  traveler_count_required: boolean;
  tickets_available: number;
  max_per_reservation: number;
  min_per_reservation: number;
  booked?: boolean; // 👈 new
}

interface AvailabilityOffer {
  offer_id: string;
  label: string;
  description: string;
  items: AvailabilityItem[];
}

interface AvailabilitySlot {
  time_slot_id: string;
  start: string | null;
  full_day: boolean;
  offers: AvailabilityOffer[];
}

interface AvailabilityResponse {
  state: "success" | "fail";
  time_slots: AvailabilitySlot[];
  message?: string;
}

interface Agent {
  id: number;
  name: string;
}

interface AttractionBookingPayload {
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
  languages: string[];
  whats_included: string[];
  not_included: string[];
  owner_id: number;
  agent_id: number;
  time_slot_id: string;
  offer_id: string;
  offer_item_id: string;
  start_time: string;
  language: string;
  price: number;
  currency: string;
}

interface AttractionBookingResponse {
  state: "success" | "fail";
  result?: unknown;
  message?: string;
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
const location = ref<string>("San Jose CA");
const message = ref<string>("");

const showSearchPanel = ref<boolean>(true);
const showLocationResult = ref<boolean>(false);
const showAttractionResult = ref<boolean>(false);
const showAttractionDetail = ref<boolean>(false);

const locationResults = ref<AttractionLocationItem[]>([]);
const attractionList = ref<AttractionListItem[]>([]);
const selectedDetail = ref<AttractionDetail | null>(null);
const availabilitySlots = ref<AvailabilitySlot[]>([]);

const selectedAttractionSlug = ref<string>("");
const selectedAttractionShortDescription = ref<string>("");

async function searchAttractionLocation(): Promise<void> {
  if (location.value.trim() === "") {
    message.value = "Location cannot be empty.";
    return;
  }

  const res = await fetch(
    travel_request(
      `search/attraction/location?location=${encodeURIComponent(location.value)}`,
    ),
    {
      method: "POST",
    },
  );

  if (!res.ok) {
    message.value = `Search location failed: ${res.status}`;
    return;
  }

  const data: AttractionLocationResponse = await res.json();

  if (data.state === "success") {
    locationResults.value = getUniqueLocations(data.result);
    attractionList.value = [];
    selectedDetail.value = null;
    availabilitySlots.value = [];
    selectedAttractionSlug.value = "";
    selectedAttractionShortDescription.value = "";

    showSearchPanel.value = false;
    showLocationResult.value = true;
    showAttractionResult.value = false;
    showAttractionDetail.value = false;

    message.value = "";
  } else {
    message.value = data.message ?? "Search location failed.";
  }
}

function getUniqueLocations(
  items: RawAttractionLocationResult[],
): AttractionLocationItem[] {
  const map = new Map<string, AttractionLocationItem>();

  for (const item of items) {
    if (!map.has(item.id)) {
      map.set(item.id, {
        id: item.id,
        cityName: item.cityName,
        countryCode: item.countryCode,
        cityUfi: item.cityUfi,
        searchDate: "",
      });
    }
  }

  return Array.from(map.values());
}

async function searchThisLocation(item: AttractionLocationItem): Promise<void> {
  if (item.searchDate === "") {
    message.value = "Please select a date.";
    return;
  }

  const res = await fetch(
    travel_request(
      `search/attraction_list?location_id=${encodeURIComponent(
        item.id,
      )}&date=${encodeURIComponent(item.searchDate)}`,
    ),
    {
      method: "POST",
    },
  );

  if (!res.ok) {
    message.value = `Search attractions failed: ${res.status}`;
    return;
  }

  const data: AttractionListResponse = await res.json();

  if (data.state === "success") {
    attractionList.value = data.result.map((item) => ({
      ...item,
      checkDate: "",
    }));

    showLocationResult.value = false;
    showAttractionResult.value = true;
    showAttractionDetail.value = false;

    message.value = "";
  } else {
    message.value = data.message ?? "Search attractions failed.";
  }
}

async function checkAttractionAvailability(
  attraction: AttractionListItem,
): Promise<void> {
  if (attraction.checkDate === "") {
    message.value = "Please select a date for this attraction.";
    return;
  }

  selectedAttractionSlug.value = attraction.slug;
  selectedAttractionShortDescription.value = attraction.short_description;

  const detailRes = await fetch(
    travel_request(
      `search/attraction/details?attraction_slug=${encodeURIComponent(
        attraction.slug,
      )}`,
    ),
    {
      method: "POST",
    },
  );

  if (!detailRes.ok) {
    message.value = `Search attraction details failed: ${detailRes.status}`;
    return;
  }

  const availabilityRes = await fetch(
    travel_request(
      `search/attraction/availabilities?attraction_slug=${encodeURIComponent(
        attraction.slug,
      )}&date=${encodeURIComponent(attraction.checkDate)}`,
    ),
    {
      method: "POST",
    },
  );

  if (!availabilityRes.ok) {
    message.value = `Search availability failed: ${availabilityRes.status}`;
    return;
  }

  const detailData: AttractionDetailResponse = await detailRes.json();
  const availabilityData: AvailabilityResponse = await availabilityRes.json();

  if (detailData.state !== "success") {
    message.value = detailData.message ?? "Search attraction details failed.";
    return;
  }

  if (availabilityData.state !== "success") {
    message.value = availabilityData.message ?? "Search availability failed.";
    return;
  }

  selectedDetail.value = detailData.result;
  availabilitySlots.value = availabilityData.time_slots;
  availabilitySlots.value = availabilityData.time_slots.map((slot) => ({
    ...slot,
    offers: slot.offers.map((offer) => ({
      ...offer,
      items: offer.items.map((item) => ({
        ...item,
        booked: false,
      })),
    })),
  }));

  showAttractionResult.value = false;
  showAttractionDetail.value = true;

  message.value = "";
}

function backToAttractionList(): void {
  showAttractionDetail.value = false;
  showAttractionResult.value = true;
  selectedDetail.value = null;
  availabilitySlots.value = [];
  selectedAttractionSlug.value = "";
  selectedAttractionShortDescription.value = "";
  message.value = "";
}

async function bookAttraction(
  slot: AvailabilitySlot,
  offer: AvailabilityOffer,
  item: AvailabilityItem,
): Promise<void> {
  if (selectedAgentId.value === "") {
    alert("Please select an agent first.");
    return;
  }

  const userId = Number(localStorage.getItem("user_id"));

  if (!userId) {
    alert("User not logged in.");
    return;
  }

  const detail = selectedDetail.value;

  if (!detail) {
    alert("Missing detail info.");
    return;
  }

  const payload: AttractionBookingPayload = {
    third_party_id: detail.id,
    slug: selectedAttractionSlug.value,
    name: detail.name,
    description: detail.description,
    short_description: selectedAttractionShortDescription.value,
    operator: detail.operator ?? "",
    city: detail.location.city ?? "",
    departure_address: detail.location.departure ?? "",
    arrival_address: detail.location.arrival ?? "",
    primary_photo: detail.primary_photo ?? "",
    free_cancellation: detail.cancellation.free,
    sub_photo_1: detail.photos[0] ?? "",
    sub_photo_2: detail.photos[1] ?? "",
    sub_photo_3: detail.photos[2] ?? "",
    languages: detail.languages,
    whats_included: detail.whatsIncluded,
    not_included: detail.notIncluded,
    owner_id: userId,
    agent_id: Number(selectedAgentId.value),
    time_slot_id: slot.time_slot_id,
    offer_id: offer.offer_id,
    offer_item_id: item.offer_item_id,
    start_time: slot.start ?? "",
    language: item.language ?? "",
    price: item.price,
    currency: item.currency,
  };

  const res = await fetch(travel_request("book/attraction"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    alert("Booking failed");
    return;
  }

  const data: AttractionBookingResponse = await res.json();

  if (data.state === "success") {
    alert("Booked successfully!");

    // 👇 mark booked
    item.booked = true;
  } else {
    alert(data.message ?? "Booking failed");
  }
}
function formatDateTime(value: string | null | undefined): string {
  if (!value) {
    return "N/A";
  }

  return value.replace("T", " ").slice(0, 16);
}
</script>

<style scoped>
.attraction_page {
  width: 100%;
  height: 100%;
  padding: 24px;
  box-sizing: border-box;
  overflow-y: auto;
}

.search_panel {
  width: 60%;
  margin: 10%;
  padding: 24px;
  border-radius: 16px;
  background: rgba(198, 221, 234, 0.72);
  box-shadow: 0 12px 28px rgba(41, 82, 112, 0.14);
}

.search_panel h2,
.attraction_list_panel h2,
.detail_panel h2 {
  margin: 0 0 20px 0;
  color: #1f2933;
}

.form_row {
  display: grid;
  grid-template-columns: 120px 1fr;
  align-items: center;
  gap: 12px;
}

.form_row label {
  font-weight: 700;
  color: #333;
}

.form_row input,
.attraction_buttons input,
.location_action input {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #b8c5cc;
  border-radius: 8px;
  font-size: 15px;
  outline: none;
  box-sizing: border-box;
}

.form_row input:focus,
.attraction_buttons input:focus,
.location_action input:focus {
  border-color: #409eff;
  background-color: beige;
}

.search_button,
.action_button,
.availability_button,
.back_button,
.book_button {
  min-width: 150px;
  height: 40px;
  border: none;
  border-radius: 10px;
  color: white;
  font-weight: 700;
  cursor: pointer;
}

.search_button,
.action_button,
.back_button {
  background-color: #409eff;
}

.availability_button {
  background-color: #10b981;
}

.book_button {
  background-color: #f59e0b;
  margin-top: 16px;
}

.search_button {
  margin-top: 20px;
}

.search_button:hover,
.action_button:hover,
.availability_button:hover,
.back_button:hover,
.book_button:hover {
  filter: brightness(0.94);
}

.message {
  width: 82%;
  margin: 12px auto;
  color: #b91c1c;
  font-weight: 700;
}

.location_result_list {
  width: 82%;
  max-height: 700px;
  margin: 20px auto;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.location_card {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 18px;
  padding: 18px;
  border-radius: 14px;
  background-color: rgba(238, 248, 252, 0.92);
  border: 1px solid rgba(160, 190, 205, 0.7);
}

.location_info {
  flex: 1;
}

.location_info h3 {
  margin: 0 0 8px 0;
  font-size: 20px;
  color: #1f2933;
}

.location_info p {
  margin: 4px 0;
  font-size: 14px;
  color: #333;
}

.location_action {
  width: 250px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.attraction_list_panel {
  width: 86%;
  height: 900px;
  margin: 24px auto;
  padding: 20px;
  border-radius: 16px;
  background-color: rgba(211, 243, 242, 0.85);
  border: 1px solid rgba(180, 165, 120, 0.45);
  box-sizing: border-box;
}

.empty_text {
  color: #666;
  font-size: 15px;
}

.attraction_result_list {
  max-height: 800px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.attraction_card {
  display: flex;
  gap: 16px;
  padding: 16px;
  border-radius: 14px;
  background-color: rgba(233, 228, 214, 0.82);
  border: 1px solid rgba(160, 190, 205, 0.55);
}

.attraction_image {
  width: 150px;
  height: 170px;
  object-fit: cover;
  border-radius: 12px;
  flex-shrink: 0;
}

.attraction_info {
  flex: 1;
}

.attraction_info h3 {
  margin: 0 0 8px 0;
  color: #1f2933;
}

.attraction_info p {
  margin: 5px 0;
  font-size: 14px;
  color: #333;
}

.description {
  line-height: 1.45;
  color: #4b5563;
}

.attraction_buttons {
  width: 210px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
  flex-shrink: 0;
}

.detail_panel {
  width: 1000px;
  margin: 20px;
  padding: 22px;
  border-radius: 18px;
  background: linear-gradient(
    135deg,
    rgba(239, 249, 255, 0.95),
    rgba(245, 240, 220, 0.92)
  );
  border: 1px solid rgba(130, 170, 190, 0.45);
  box-shadow: 0 18px 45px rgba(41, 82, 112, 0.15);
}

.detail_card {
  margin-top: 8px;
}

.detail_top {
  display: flex;
  gap: 22px;
  align-items: flex-start;
}

.detail_main_photo {
  width: 280px;
  height: 230px;
  object-fit: cover;
  border-radius: 16px;
  flex-shrink: 0;
}

.detail_summary {
  flex: 1;
}

.detail_summary h2 {
  margin-bottom: 12px;
}

.operator {
  font-weight: 700;
  color: #2f5f83;
}

.detail_section {
  margin-top: 12px;
  padding: 6px;
  border-radius: 14px;
  background-color: rgba(255, 255, 255, 0.7);
}

.detail_section h3 {
  margin: 0 0 10px 0;
}

.long_text {
  white-space: pre-line;
  line-height: 1.55;
  color: #374151;
}

.detail_grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  padding-left: 15px;
}

.photo_strip {
  margin-top: 12px;
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding-bottom: 8px;
}

.detail_photo {
  width: 280px;
  height: 220px;
  object-fit: cover;
  border-radius: 12px;
  flex-shrink: 0;
}

.availability_panel {
  margin-top: 26px;
}

.slot_list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.slot_card {
  padding: 16px;
  border-radius: 14px;
  background-color: rgba(238, 248, 252, 0.9);
  border: 1px solid rgba(160, 190, 205, 0.55);
}

.offer_card {
  margin-top: 12px;
  padding: 14px;
  border-radius: 12px;
  background-color: rgba(255, 255, 255, 0.8);
}

.availability_item {
  margin-top: 10px;
  padding: 12px;
  border-radius: 10px;
  background-color: rgba(235, 245, 240, 0.85);
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6px 14px;
}

.availability_item p {
  margin: 2px 0;
  font-size: 14px;
}

.booking_controls {
  margin-top: 16px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.booking_controls label {
  font-weight: 700;
  color: #333;
}

.booking_controls select {
  min-width: 180px;
  padding: 9px 10px;
  border: 1px solid #b8c5cc;
  border-radius: 8px;
  font-size: 14px;
}
.book_button.booked {
  background-color: #9ca3af; /* 灰色 */
  cursor: not-allowed;
}
</style>
