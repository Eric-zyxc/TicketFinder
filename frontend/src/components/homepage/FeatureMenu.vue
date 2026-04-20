<template>
  <div class="block">
    <div class="section">
      <p>Search</p>
      <button class="feature_button">Search Flight</button>
      <button class="feature_button">Search Hotel</button>
      <button class="feature_button">Search History</button>
    </div>
    <div class="section">
      <p>Booking</p>
      <button class="feature_button">Booking Flight</button>
      <button class="feature_button">Booking Hotel</button>
      <button class="feature_button">My Bookings</button>
    </div>
    <div class="section">
      <p>More Service</p>
      <button class="feature_button">Car Rental</button>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>

<style lang="css">
.block {
  display: flex;
  flex-direction: column;
}

.section {
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  border: 1px solid rgb(88, 88, 88);
  margin: 10px;
  background-color: rgb(166, 232, 232);
}

p {
  align-self: center;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    "Open Sans",
    "Helvetica Neue",
    sans-serif;
  color: #1b1b1b;
}

.feature_button {
  margin: 10px;
  height: 40px;
  font-family:
    system-ui,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    Roboto,
    Oxygen,
    Ubuntu,
    Cantarell,
    "Open Sans",
    "Helvetica Neue",
    sans-serif;
  font-weight: bolder;
  font-size: larger;
  border-radius: 15px;
}
.feature_button:hover {
  scale: 103%;
  background-color: azure;
}
</style>
