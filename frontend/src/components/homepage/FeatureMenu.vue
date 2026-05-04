<template>
  <div class="block">
    <div class="section">
      <p>Search</p>

      <button
        class="feature_button"
        @click="emit('switch-view', 'airport_search')"
      >
        Search Flight
      </button>
      <button
        class="feature_button"
        @click="emit('switch-view', 'search_hotel')"
      >
        Search Hotel
      </button>
      <button
        class="feature_button"
        @click="emit('switch-view', 'attraction_search_page')"
      >
        Search Attraction
      </button>
    </div>
    <div class="section">
      <p>Booking</p>
      <button
        class="feature_button"
        @click="emit('switch-view', 'flight_booking_record_page')"
      >
        My Flight Booking
      </button>
      <button
        class="feature_button"
        @click="emit('switch-view', 'hotel_booking_record_page')"
      >
        My Hotel Booking
      </button>
      <button
        class="feature_button"
        @click="emit('switch-view', 'attraction_booking_record_page')"
      >
        My Attraction Booking
      </button>
    </div>
    <div class="section">
      <p>More Service</p>
      <button class="feature_button">Car Rental</button>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits(["switch-view"]);
</script>

<style lang="css">
.block {
  display: flex;
  flex-direction: column;
  gap: 16px;
  padding: 14px;
  box-sizing: border-box;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif;

  background-image: url("/src/asset/picture/light.jpg");
  backdrop-filter: blur(6px);
  background-size: cover;
  overflow-y: auto;
  height: 1430px;
}

.section {
  display: flex;
  flex-direction: column;
  padding: 14px 12px;
  border-radius: 18px;
  background: linear-gradient(
    135deg,
    rgba(235, 249, 255, 0.94),
    rgba(193, 232, 238, 0.88)
  );
  border: 1px solid rgba(120, 160, 180, 0.45);
  box-shadow: 0 10px 24px rgba(40, 80, 110, 0.12);
}

.section p {
  margin: 0 0 12px 0;
  align-self: center;
  color: #1f2933;
  font-size: 16px;
  font-weight: 850;
  letter-spacing: 0.02em;
}

.feature_button {
  min-height: 42px;
  margin: 6px 0;
  padding: 0 14px;
  border: 1px solid rgba(120, 160, 180, 0.45);
  border-radius: 14px;
  background: rgba(255, 255, 255, 0.72);
  color: #2e465d;
  font-size: 14px;
  font-weight: 750;
  cursor: pointer;
  text-align: left;
  box-shadow: 0 6px 14px rgba(40, 80, 110, 0.08);
  transition:
    transform 0.18s ease,
    background-color 0.18s ease,
    box-shadow 0.18s ease;
}

.feature_button:hover {
  transform: translateY(-2px);
  background-color: #eef9ff;
  box-shadow: 0 10px 20px rgba(40, 80, 110, 0.14);
}
</style>
