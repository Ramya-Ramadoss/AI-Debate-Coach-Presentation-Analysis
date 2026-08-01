# Agentic AI Debate Coach & Presentation Analysis Platform

An AI-powered coaching and evaluation platform that assists users in improving their debate strategy, public speaking, argumentation structure, and logical consistency.

This repository holds the **Week 1 Foundation Architecture** (Monorepo), containing the complete database schema, user registration, JWT authentication session handlers, user experience profiles, and debate scheduling CRUD modules.

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** (Python 3.12/3.13)
- **SQLAlchemy ORM**
- **Alembic** (Database Migrations)
- **PostgreSQL** (Primary database)
- **JWT & Password Hashing** (PyJWT + Passlib + Bcrypt)
- **Pydantic v2** (Data Validation)

### Frontend
- **React 19**
- **Vite**
- **Tailwind CSS v4**
- **React Router Dom v6**
- **Axios** (With automatic Authorization & Token Refresh interceptors)
- **React Hook Form** (Form validation)
- **Framer Motion** (Animations)
- **Lucide Icons**

### DevOps
- **Docker & Docker Compose**

---

## 📂 Folder Structure

```
debate-coach/
├── backend/                  # FastAPI Backend Service
│   ├── app/
│   │   ├── api/              # Routers (auth, profile, debates, roles)
│   │   ├── core/             # Configuration & Security (JWT, dependencies)
│   │   ├── database/         # Database sessions (db.py)
│   │   ├── middlewares/      # Global Exception handlers
│   │   ├── models/           # SQLAlchemy database schemas
│   │   ├── schemas/          # Pydantic v2 schemas
│   │   └── main.py           # Entrypoint
│   ├── alembic/              # Database migration versions
│   ├── tests/                # Automated pytest unit tests
│   └── requirements.txt      # Python dependencies
├── frontend/                 # React Frontend Service (Vite + Tailwind v4)
│   ├── src/
│   │   ├── components/       # Reusable components (Navbar, Sidebar)
│   │   ├── context/          # State providers (AuthContext)
│   │   ├── layouts/          # Page Wrappers (DashboardLayout)
│   │   ├── pages/            # View Pages (Landing, Login, Register, Dashboard, Profile, CreateDebate, MyDebates)
│   │   ├── routes/           # React Router config (AppRoutes)
│   │   ├── services/         # API clients (api.js)
│   │   └── App.jsx           # App entrypoint
│   └── Dockerfile            # Frontend production container configuration
├── docker-compose.yml        # Docker Multi-container Orchestrator
├── .env.example              # Environment variables template
└── README.md                 # Project Documentation
```

---

## ⚙️ Installation & Running Locally

### Prerequisites
- Python 3.12+ (tested on Python 3.13)
- Node.js 18+ (tested on Node.js 24)
- PostgreSQL (or local SQLite fallback)

### Option 1: Docker (Recommended)
Build and run the entire stack (PostgreSQL + Backend + Frontend) using Docker:
```bash
docker-compose up --build
```
- Frontend will serve on: `http://localhost:3000`
- Backend API will serve on: `http://localhost:8000`
- Database runs on: `http://localhost:5432`

### Option 2: Running Services Individually

#### 1. Setup Backend
1. Initialize virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # On Windows
   source venv/bin/activate    # On Unix/macOS
   ```
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Set environment variables in a `.env` file (see `.env.example`). By default, if PostgreSQL is not found, the app automatically falls back to an SQLite database `test.db` to facilitate development.
4. Run the API server:
   ```bash
   uvicorn backend.app.main:app --reload
   ```

#### 2. Setup Frontend
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Launch development server:
   ```bash
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

## 🚦 Running Automated Tests

Run backend unit tests verifying user registration, login JWT token exchanges, profile CRUD, debate creation permissions, and role restrictions:
```bash
python -m pytest backend/tests/
```

---

## 🔌 API Documentation

Detailed interactive API endpoints docs are available locally at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Core Endpoints:
- **Authentication**:
  - `POST /register`: Registers a new user and auto-creates their speaking profile.
  - `POST /login`: Receives form username/password, returns access token + refresh token.
  - `POST /login/json`: Receives JSON login credentials, returns tokens.
  - `POST /refresh`: Accepts refresh token, returns new access token.
  - `POST /logout`: Revokes the refresh token.
- **Profiles**:
  - `GET /profile`: Fetch profile of the logged-in user.
  - `PUT /profile`: Update profile fields.
  - `DELETE /profile`: Delete user account (cascades database deletion).
- **Debate Sessions**:
  - `POST /debates`: Create and schedule a debate session.
  - `GET /debates`: List debate sessions (Learners see their own; Admins/Coaches/Educators see all).
  - `GET /debates/{id}`: Retrieve specific debate session details.
  - `PUT /debates/{id}`: Update debate details.
  - `DELETE /debates/{id}`: Delete debate session.

---

## 🚀 Week 2 Roadmap: AI Integration & Analysis

With the foundation built, Week 2 will integrate the following AI modules:
1. **AI Debate Simulation Engine**: Real-time cross-examinations and AI opponent generation using LangGraph/LangChain.
2. **Logical Fallacy Detection**: Pipeline evaluating statements for circular reasoning, ad hominem, straw man, etc.
3. **Speech & Presentation Analytics**: Whisper-powered speech-to-text with speech pace evaluation and filler word audits.
4. **Coaching Recommendation System**: Automated generation of personalized learning paths based on performance scores.
