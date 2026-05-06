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
├── reqiurements           # pip requirements list
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

- After cloning the project to the local, both services need “.env” configuration files. 
1. Identity Service .env needs: 	
``` text
DATABASE_URL= {Your database url}  # database url
ACCESS_TOKEN_EXPIRE_MINUTES=60     # authentication expire time
AUTH_ALGORITHM=HS256               # password hashing algorithm
```
2. Travel Service .env needs:
``` text
DATABASE_URL=  {Your database url}  # database url
RAPIDAPI_KEY=  {RapidAPI Key}       # your RapidAPI key
```
- There is a database initializer located in the _initialization folder. You can initialize the database by running it. 
- By using the bash command “npm install requirement.txt”, you can install all backend dependencies.




