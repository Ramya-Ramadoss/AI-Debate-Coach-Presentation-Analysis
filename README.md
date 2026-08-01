# Agentic AI Debate Coach & Presentation Analysis Platform

An AI-powered coaching and evaluation platform that assists users in improving their debate strategy, public speaking, argumentation structure, and logical consistency.

This repository holds the complete monorepo implementation covering Week 1 Foundation, Week 2 Argument Analysis Engine, Week 3 Debate Simulation & Coaching, and Milestone 4 Presentation/Video Analytics.

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** (Python 3.12/3.13)
- **SQLAlchemy ORM** & **SQLite / PostgreSQL**
- **Alembic** (Database Migrations)
- **JWT & Password Hashing** (Bcrypt direct hashing)
- **LangChain & LangGraph** (AI Orchestrated workflows)
- **Pydantic v2** (Data Validation)
- **ReportLab** (PDF Report Generation)
- **Librosa / PyAV** (Speech & video analysis mocks)

### Frontend
- **React 19**
- **Vite**
- **Tailwind CSS v4**
- **React Router Dom v7**
- **Axios** (With automatic Authorization & Token Refresh interceptors)
- **Framer Motion** (Aesthetics & animations)
- **Lucide Icons**

### DevOps & CI/CD
- **Docker & Docker Compose**
- **Nginx** (Serving React production SPA build)
- **GitHub Actions** (CI pipeline checking Python tests, React builds, and Docker compiles)

---

## 📂 Folder Structure

```
debate-coach/
├── .github/
│   └── workflows/
│       └── ci.yml            # CI GitHub Actions
├── backend/                  # FastAPI Backend Service
│   ├── app/
│   │   ├── api/              # Routers (auth, profile, debates, analysis, debate, presentation)
│   │   ├── core/             # Configuration & Security (JWT, dependencies)
│   │   ├── database/         # Database sessions (db.py)
│   │   ├── models/           # SQLAlchemy database schemas
│   │   ├── schemas/          # Pydantic v2 schemas
│   │   ├── ai/               # AI Engine
│   │   │   ├── prompts/      # System prompts & structures
│   │   │   ├── models/       # Prompt schemas
│   │   │   ├── utils/        # LLM client & Mock fallback
│   │   │   ├── workflow/     # LangGraph state workflow graphs
│   │   │   ├── argument_analysis/  # Fallacies & extractor engines
│   │   │   └── presentation_analysis/ # Video & audio processors
│   │   └── main.py           # Entrypoint
│   ├── tests/                # Automated pytest unit/integration tests
│   └── requirements.txt      # Python dependencies
├── frontend/                 # React Frontend Service (Vite + Tailwind v4)
│   ├── src/
│   │   ├── components/       # Reusable UI elements (Navbar, Sidebar)
│   │   ├── pages/            # View Pages (Landing, Login, Register, Dashboard, DebateArena, ArgumentAnalysis, PresentationAnalysis, PerformanceDashboard, AdminDashboard)
│   │   ├── routes/           # React Router config (AppRoutes)
│   │   └── App.jsx           # App entrypoint
│   ├── Dockerfile            # Frontend production container configuration
│   └── nginx.conf            # Nginx config serving SPA
├── docker-compose.yml        # Docker Multi-container Orchestrator
└── README.md                 # Project Documentation
```

---

## ⚙️ Installation & Running Locally

### Prerequisites
- Python 3.12+ (tested on Python 3.13)
- Node.js 18+ (tested on Node.js 24)
- Docker & Docker Compose (optional for container launch)

### Option 1: Docker (Recommended)
Build and run the entire stack (PostgreSQL + Backend + Frontend) using Docker:
```bash
docker compose up --build
```
- Frontend: `http://localhost:3000`
- Backend API Docs: `http://localhost:8000/docs`

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
3. Run the API server:
   ```bash
   $env:PYTHONPATH="."          # Windows PowerShell
   python backend/app/main.py
   ```

#### 2. Setup Frontend
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies & run:
   ```bash
   npm install
   npm run dev
   ```
   Open `http://localhost:5173` in your browser.

---

## 🚦 Running Automated Tests

Run backend unit and integration tests verifying AI services, LangGraph workflows, and API endpoints:
```bash
$env:PYTHONPATH="."
python -m pytest backend/tests/test_all_milestones.py
```

---

## 🔌 API Documentation

### 1. Argument Analysis:
- `POST /analyze`: Extracts claims, premises, evidence, and evaluates reasoning/fallacies.
- `POST /export/pdf`: Exports argument analysis details to a PDF file.
- `POST /export/csv`: Exports metrics to CSV file.
- `POST /export/json`: Exports analysis to JSON format.

### 2. Debate Simulation:
- `POST /debate/start`: Starts a session and generates the AI opponent's opening statement.
- `POST /debate/respond`: Submits user rebuttal and returns AI counter-rebuttal, scores, and coaching tips.
- `POST /debate/end`: Ends the debate and returns closing statements.
- `GET /debate/performance`: Returns performance analytics and progress trends.
- `POST /debate/learning-plan`: Generates a personalized 7/14/30 days checklist.

### 3. Presentation & Speech/Video:
- `POST /presentation/upload`: Accepts MP4/WAV file uploads, returning local path and mock transcript.
- `POST /presentation/analyze`: Performs vocal pacing, pauses, filler words check, and pose/eye contact tracking.
- `GET /presentation/report/{id}`: Exports PDF/JSON presentation summary.
