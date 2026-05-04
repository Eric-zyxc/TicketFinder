<template>
  <div class="home_view_page">
    <div class="hero_card">
      <p class="eyebrow">TicketFinder Guide</p>

      <h1>Welcome back, Traveler.</h1>

      <p class="subtitle">
        Start by choosing what you want to explore. Use the left menu or the top
        navigation to search flights, hotels, or attractions. Once you find
        something you like, proceed to booking and manage everything in one
        place.
      </p>

      <div class="guide_steps">
        <div class="step">
          <span>🔍</span>
          <h3>Search</h3>
          <p>Pick Flight, Hotel, or Attraction and enter your destination.</p>
        </div>

        <div class="step">
          <span>📊</span>
          <h3>Compare</h3>
          <p>Browse results, check details, and find the best option.</p>
        </div>

        <div class="step">
          <span>✅</span>
          <h3>Book</h3>
          <p>Confirm your selection and manage it in Booking pages.</p>
        </div>
      </div>

      <div class="tips">
        <p>
          💡 Tip: Use the top navigation for quick access, or the side menu for
          detailed workflows.
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home_view_page {
  backdrop-filter: blur(0px);
  width: 100%;
  height: 450px;
  margin-top: 150px;
  display: flex;
  justify-content: center;
  box-sizing: border-box;
}

.hero_card {
  width: min(780px, 90%);
  border-radius: 26px;
  text-align: center;
  padding: 30px;
  background:
    radial-gradient(
      circle at top left,
      rgba(64, 158, 255, 0.25),
      transparent 35%
    ),
    linear-gradient(
      135deg,
      rgba(255, 255, 255, 0.92),
      rgba(225, 245, 255, 0.82)
    );

  border: 1px solid rgba(130, 170, 190, 0.45);

  box-shadow:
    0 20px 50px rgba(40, 80, 110, 0.18),
    inset 0 1px 0 rgba(255, 255, 255, 0.8);
}

.eyebrow {
  margin: 0 0 10px 0;
  color: #1677c8;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.hero_card h1 {
  margin: 0;
  color: #1f2933;
  font-size: 48px;
  font-weight: 900;
}

.subtitle {
  margin: 18px auto 26px auto;
  color: #4b5563;
  font-size: 16px;
  line-height: 1.6;
  max-width: 520px;
}

.guide_steps {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.step {
  padding: 16px;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.75);
  border: 1px solid rgba(150, 180, 200, 0.35);
  box-shadow: 0 10px 20px rgba(40, 80, 110, 0.1);
}

.step span {
  font-size: 28px;
}

.step h3 {
  margin: 8px 0 4px 0;
  font-size: 16px;
  color: #2e465d;
}

.step p {
  font-size: 13px;
  color: #555;
}

.tips {
  margin-top: 22px;
  font-size: 13px;
  color: #2f5f83;
}

@media (max-width: 760px) {
  .guide_steps {
    grid-template-columns: 1fr;
  }

  .hero_card h1 {
    font-size: 34px;
  }
}
</style>
