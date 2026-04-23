# TicketFinder

A full-stack travel booking system with hotel search, booking services, and a modular microservices architecture.

---

## 🧱 Project Structure
```
TICKETFINDER/
│
├── frontend/             # Vue + Vite frontend
├── travel-service/       # Main travel backend (search + booking)
├── identity-service/     # Auth / user service
├── pip_reqirements/      # pip requirements list
└── README.md
```

---

## 🚀 Features

### ✅ Implemented
- 🔍 Hotel destination search (RapidAPI)
- 🏨 Hotel search by destination
- 🧾 Flight / hotel booking system (DB-backed)
- 🔐 Authentication (JWT-based)
- 🧱 Clean architecture:
  - router → service → client / dal

### 🔄 In Progress
- Frontend integration
- Flight search (API / mock)
- Caching layer
- UI improvements

---

## 🛠 Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite
- Pydantic

### Frontend
- Vue 3
- Vite
- TypeScript

### External API
- RapidAPI (Booking.com provider)

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/TicketFinder.git
cd TicketFinder
```

### 2. Setup backend (travel-service)
```bash
cd travel-service
pip install -r requirements.txt
```
Create .env:
```env
RAPIDAPI_KEY=your_key_here
DATABASE_URL=sqlite:///./travel_booking.db
SECRET_KEY=your_secret
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
Run server:
```bash
uvicorn app.main:travel_service --reload
```
Swagger:
```code
http://127.0.0.1:8000/docs
```
---
### 3. Setup frontend
```bash
cd frontend
npm install ./pip_requirements/requirements.txt
npm run dev
```
App:
```code
http://localhost:5173
```



