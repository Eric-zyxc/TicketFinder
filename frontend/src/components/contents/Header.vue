<template>
  <div class="header">
    <img src="@/asset/picture/logo.png" class="logo" />

    <nav class="nav_bar">
      <button class="menu_element" @click="emit('switch-view', 'home')">
        Home
      </button>

      <button class="menu_element" @click="emit('switch-view', 'profile')">
        User
      </button>

      <!-- Search Dropdown -->
      <div class="dropdown">
        <button class="menu_element dropdown_button">Search ▾</button>

        <div class="dropdown_menu">
          <button @click="emit('switch-view', 'search_hotel')">Hotel</button>
          <button @click="emit('switch-view', 'airport_search')">Flight</button>
          <button @click="emit('switch-view', 'attraction_search_page')">
            Attraction
          </button>
        </div>
      </div>

      <!-- Booking Dropdown -->
      <div class="dropdown">
        <button class="menu_element dropdown_button">Booking ▾</button>

        <div class="dropdown_menu">
          <button @click="emit('switch-view', 'hotel_booking_record_page')">
            Hotel Booking
          </button>
          <button @click="emit('switch-view', 'flight_booking_record_page')">
            Flight Booking
          </button>
          <button
            @click="emit('switch-view', 'attraction_booking_record_page')"
          >
            Attraction Booking
          </button>
        </div>
      </div>

      <button class="menu_element" @click="emit('switch-view', 'about_page')">
        About
      </button>
    </nav>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits(["switch-view"]);
</script>

<style scoped>
/* ===== HEADER BASE ===== */
.header {
  position: sticky;
  top: 0;
  z-index: 1000;

  height: 70px;
  padding: 0 30px;

  display: flex;
  align-items: center;

  backdrop-filter: blur(12px);
  background: linear-gradient(
    135deg,
    rgba(214, 235, 241, 0.85),
    rgba(0, 79, 248, 0.75)
  );

  border-bottom: 1px solid rgba(150, 180, 200, 0.4);

  box-shadow: 0 8px 25px rgba(40, 80, 110, 0.12);
}

/* ===== LOGO ===== */
.logo {
  height: 65px;
  margin-right: 40px;
  border-radius: 50px;
}

/* ===== NAV ===== */
.nav_bar {
  display: flex;
  align-items: center;
  gap: 26px;
}

/* ===== MENU ELEMENT ===== */
.menu_element {
  font-size: 15px;
  font-weight: 700;
  color: #2e465d;

  background: none;
  border: none;
  cursor: pointer;

  padding: 8px 10px;
  border-radius: 10px;

  transition: all 0.25s ease;
}

.menu_element:hover {
  color: #1677c8;
  background-color: rgba(255, 255, 255, 0.5);
}

/* ===== DROPDOWN ===== */
.dropdown {
  position: relative;
}

/* dropdown animation */
.dropdown_menu {
  position: absolute;
  top: 120%;
  left: 0;

  min-width: 200px;

  display: flex;
  flex-direction: column;

  padding: 10px;
  border-radius: 14px;

  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(10px);

  border: 1px solid rgba(180, 200, 220, 0.5);

  box-shadow: 0 12px 30px rgba(40, 80, 110, 0.18);

  opacity: 0;
  transform: translateY(-10px);
  pointer-events: none;

  transition: all 0.25s ease;
}

/* hover trigger */
.dropdown:hover .dropdown_menu {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

/* dropdown items */
.dropdown_menu button {
  padding: 10px 12px;
  border-radius: 10px;

  background: transparent;
  border: none;

  text-align: left;
  font-size: 15px;
  font-weight: 600;
  color: #2e465d;

  cursor: pointer;
  transition: all 0.2s ease;
}

.dropdown_menu button:hover {
  background-color: #e6f4ff;
  color: #1677c8;
}

/* ===== SMALL POLISH ===== */
.dropdown_button {
  display: flex;
  align-items: center;
  gap: 6px;
}
</style>
