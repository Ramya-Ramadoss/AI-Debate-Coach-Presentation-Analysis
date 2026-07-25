from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from auth import router as auth_router
from database import init_db
from profile import router as profile_router
from roles import router as role_router

app = FastAPI(title="Debate Coach API")

init_db()

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(role_router)


frontend_dir = Path(__file__).resolve().parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_dir), name="static")


@app.get("/")
def home():
    return FileResponse(frontend_dir / "index.html")