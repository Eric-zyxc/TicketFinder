# Ticket Finder Frontend

This is the frontend of the Ticket Finder project, built with Vue 3 + Vite.

---

## 🚀 Getting Started

### 1. Install dependencies

Make sure you have Node.js installed:

node -v
npm -v

Then install dependencies:

npm install

---

### 2. Run development server

npm run dev

Open in browser:

http://localhost:5173

---

## 🧩 Project Structure

src/
  components/      # reusable components (Header, Login, etc.)
  views/           # pages (LoginPage, HomePage)
  router/          # vue-router config
  api/             # API wrapper (fetch client)
  assets/          # images, styles

---

## 🔗 Backend Connection

Frontend connects to FastAPI backend:

http://127.0.0.1:8000

Make sure backend service is running.

---

## 🔐 Authentication

- Login API returns a JWT token
- Token is stored in:

localStorage

- Authenticated requests include:

Authorization: Bearer <token>

---

## 📦 Dependencies

Main dependencies:

vue
vue-router
vite

Install manually if needed:

npm install vue vue-router

---

## 🛠 Development Notes

- Uses Vue 3 Composition API
- Routing handled by vue-router
- API calls are wrapped in /src/api/
- Layout includes:
  - Header
  - Left Menu
  - Center Content
  - Right Menu

---

## ⚠️ Common Issues

### CORS error

Make sure backend enables CORS:

allow_origins = ["http://localhost:5173"]

---

### Token not working

Check in browser:

DevTools → Application → Local Storage

---

## 🧠 Future Improvements

- Add state management (Pinia)
- Improve UI design
- Add loading & error handling
- Role-based routing (admin/user)

---

## 👨‍💻 Author

Jesse Yang
