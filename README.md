<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=250&color=0:134E5E,50:2ECC71,100:A8E063&text=AI%20DEBATE%20&%20PRESENTATION%20COACH&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=40"/>
</p>

# 🎤 Agentic AI Debate Coach and Presentation Analysis Platform

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](LICENSE)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-19.0.0-61DAFB.svg?style=flat-square&logo=react)](https://react.dev)
[![Docker](https://img.shields.io/badge/Docker-Orchestrated-2496ED.svg?style=flat-square&logo=docker)](https://www.docker.com)

An AI-powered coaching and evaluation platform that assists users in improving their debate strategy, public speaking, argumentation structure, and logical consistency.

This repository holds the complete monorepo implementation covering:
* **Week 1 Foundation Architecture**: DB schemas, JWT authentication, user experience profiles, and session CRUD.
* **Week 2 Argument Analysis Engine**: Claims/premises extraction, fallacy classifications, and AI rewrite optimizer.
* **Week 3 Debate Simulation & Coaching**: Multi-round interactive arenas, AI stance generation, and coaching recommendations.
* **Milestone 4 Presentation & Speech/Video Analytics**: Vocal pacing (WPM), speech pause metrics, posture tracking, and PDF/CSV reports export.

---

## 🛠️ Tech Stack & Architecture

### Backend Core
- **FastAPI**: Python high-performance API server.
- **SQLAlchemy ORM**: Seamless PostgreSQL database management.
- **LangChain & LangGraph**: Agentic workflow orchestration.
- **Bcrypt**: Standard, direct hashing.
- **ReportLab**: PDF report generation streams.

### Frontend Dashboard
- **React 19 & Vite**: Hot-reloading module bundler.
- **Tailwind CSS v4**: Ultra-modern component styling.
- **Framer Motion**: Smooth animations.
- **Lucide Icons**: Clean, scalable icons.

### DevOps & CI/CD
- **Docker Compose**: Multi-container stack orchestration.
- **Nginx**: Serving compiled React Single Page Application.
- **GitHub Actions**: Automated validation pipelines on check-in.

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
│   │   ├── database/         # Database sessions & SQLite fallbacks
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
│   │   ├── pages/            # View Pages (Landing, Login, Register, DebateArena, ArgumentAnalysis, PresentationAnalysis, PerformanceDashboard, AdminDashboard)
│   │   ├── routes/           # React Router config (AppRoutes)
│   │   └── App.jsx           # App entrypoint
│   ├── Dockerfile            # Frontend production container configuration
│   └── nginx.conf            # Nginx config serving SPA
├── docker-compose.yml        # Docker Multi-container Orchestrator
└── README.md                 # Project Documentation
```

---

## ⚙️ Installation & Running Locally

### Option 1: Docker (Recommended)
Build and run the entire stack (PostgreSQL + Backend + Frontend) using Docker:
```bash
docker compose up --build
```
* **Frontend**: `http://localhost:3000`
* **Backend API Docs**: `http://localhost:8000/docs`

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
   * *Note*: If no local PostgreSQL is active on port `5432`, the server automatically falls back to an SQLite database `test.db` for development ease.

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

## 🔌 API Reference & Endpoints

### 1. Argument Analysis
#### `POST /analyze`
Extracts claims, premises, evidence, and evaluates logical fallacies.
* **Request Body**:
  ```json
  {
    "text": "Universal Basic Income is necessary because automation reduces standard job counts.",
    "debate_session_id": 1
  }
  ```
* **Response Output**:
  ```json
  {
    "argument_id": 12,
    "scores": {
      "clarity": 85,
      "relevance": 90,
      "evidence_strength": 75,
      "logical_consistency": 80,
      "persuasiveness": 82
    },
    "claims": {
      "main_claim": "Universal Basic Income is necessary",
      "supporting_claims": ["Automation reduces standard job counts"]
    },
    "fallacies": [],
    "improved": {
      "improved_argument": "As automation displaces standard employment sectors, implementing a Universal Basic Income becomes vital to stabilize consumer spending and support structural career transitions.",
      "wording_tips": "Avoid absolute terms like 'always'; use 'becomes vital'."
    }
  }
  ```

### 2. Interactive Debate Simulation
* `POST /debate/start`: Generates the AI opponent's opening statement based on selected format and difficulty.
* `POST /debate/respond`: Submits user rebuttal and returns the AI counter-argument, scores, and coaching tips.
* `POST /debate/end`: Ends the debate round and returns closing statements.
* `GET /debate/performance`: Returns performance analytics and progress trends.
* `POST /debate/learning-plan`: Generates a personalized 7/14/30 days learning plan.

### 3. Presentation Analytics
* `POST /presentation/upload`: Accepts MP4/WAV file uploads, returning local path and mock transcript.
* `POST /presentation/analyze`: Performs vocal pacing, pauses index, filler words check, and pose/eye contact tracking.
* `GET /presentation/report/{id}`: Exports PDF/JSON presentation summary.
