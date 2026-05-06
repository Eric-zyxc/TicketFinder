# TicketFinder

A full-stack travel booking system with hotel search, booking services, and a modular microservices architecture.

---

## 🧱 Project Structure
```
TICKETFINDER/
│
├── _initialization/      # Database set up
├── frontend/             # Vue + Vite frontend
├── travel-service/       # Main travel backend (search + booking)
├── identity-service/     # Auth / user service
├── reqirements           # pip requirements list
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

### 2. Setup backend (both-service)
For Mac:
```bash
brew install postgresql
brew services start postgresql
createdb travel_app
psql -d travel_app -f _initialization/init_db.sql
psql -d travel_app
SELECT current_user;
ALTER USER eric WITH PASSWORD '123456';
quit
```
Only use that PASSWORD line if needed, if you know you have one, skip it
The output of "current_user" will used as USERNAME in .env below
Then move to next step:
```bash
pip install -r requirements.txt
cd travel-service
```
Create .env:
```env
RAPIDAPI_KEY=your_key_here
DATABASE_URL=postgresql+psycopg://USERNAME:123456@localhost:5432/travel_app
MAX_CHEAPEST_HOTELS=10
```
Run server:
```bash
uvicorn app.main:travel_service --reload --port 8001
```
Swagger:
```code
http://127.0.0.1:8001/docs
```
In new terminal:
```bash
cd TicketFinder
cd identity-service
```
Create .env:
```env
DATABASE_URL=postgresql+psycopg://USERNAME:123456@localhost:5432/travel_app
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
Run server:
```bash
uvicorn app.main:travel_service --reload --port 8000
```
Swagger:
```code
http://127.0.0.1:8000/docs
```
---
### 3. Setup frontend
```bash
cd frontend
npm install ./requirements.txt
npm run dev
```
App:
```code
http://localhost:5173
```



