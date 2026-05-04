<template>
  <div class="about_page">
    <div class="about_container">
      <h1 class="title">About TicketFinder</h1>

      <p class="intro">
        TicketFinder is a simple travel planning platform that helps users
        explore flights, hotels, and attractions in one place. It focuses on
        providing a clean and efficient experience for searching and booking
        travel services.
      </p>

      <div class="section">
        <h2>What We Do</h2>
        <p>
          We aggregate travel data from multiple sources and present it in a
          unified interface. Users can search destinations, compare options, and
          manage bookings with minimal friction.
        </p>
      </div>

      <div class="section">
        <h2>Features</h2>
        <ul>
          <li>Flight search and booking</li>
          <li>Hotel discovery and reservation</li>
          <li>Attraction browsing and scheduling</li>
          <li>Unified booking management</li>
        </ul>
      </div>

      <div class="section">
        <h2>Design Philosophy</h2>
        <p>
          The system is built with a focus on clarity, modularity, and
          maintainability. Each feature is designed to be simple, predictable,
          and easy to extend.
        </p>
      </div>

      <div class="section">
        <h2>Tech Stack</h2>
        <ul>
          <li>Frontend: Vue 3 + TypeScript</li>
          <li>Backend: FastAPI</li>
          <li>Database: PostgreSQL</li>
          <li>External APIs: RapidAPI integrations</li>
        </ul>
      </div>

      <div class="footer">
        <p>© 2026 TicketFinder. All rights reserved.</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.about_page {
  width: 100%;
  height: 100%;
  padding: 40px;
  box-sizing: border-box;
  display: flex;
  justify-content: center;
  overflow-y: auto;
}

.about_container {
  width: 800px;
  background: linear-gradient(
    135deg,
    rgba(240, 248, 255, 0.95),
    rgba(230, 240, 250, 0.92)
  );
  border-radius: 18px;
  padding: 36px;
  box-shadow: 0 18px 40px rgba(40, 80, 110, 0.15);
  border: 1px solid rgba(160, 190, 210, 0.4);
}

.title {
  margin: 0 0 20px 0;
  font-size: 32px;
  font-weight: 800;
  color: #1f2933;
  text-align: center;
}

.intro {
  font-size: 16px;
  color: #444;
  line-height: 1.6;
  text-align: center;
  margin-bottom: 28px;
}

.section {
  margin-top: 24px;
}

.section h2 {
  margin-bottom: 10px;
  font-size: 20px;
  color: #2f5f83;
}

.section p {
  font-size: 15px;
  line-height: 1.6;
  color: #333;
}

.section ul {
  padding-left: 18px;
  margin: 8px 0;
}

.section li {
  margin-bottom: 6px;
  font-size: 15px;
  color: #333;
}

.footer {
  margin-top: 36px;
  text-align: center;
  font-size: 13px;
  color: #777;
}
</style>
