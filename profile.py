from fastapi import APIRouter, Depends, status

from database import SessionLocal
from dependencies import get_current_user
from models import User
from schemas import UserProfile

router = APIRouter()


@router.post("/profile", status_code=status.HTTP_200_OK)
def create_profile(profile: UserProfile, current_user=Depends(get_current_user)):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == current_user.id).first()
        if not user:
            raise RuntimeError("User not found")

        user.name = profile.name
        user.experience_level = profile.experience_level
        user.goals = profile.goals
        user.preferred_topics = profile.preferred_topics
        db.commit()
        db.refresh(user)
        return {
            "message": "Profile Created Successfully",
            "profile": {
                "name": user.name,
                "experience_level": user.experience_level,
                "goals": user.goals,
                "preferred_topics": user.preferred_topics,
            },
        }
    finally:
        db.close()


@router.get("/profile")
def get_profile(current_user=Depends(get_current_user)):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == current_user.id).first()
        if not user:
            raise RuntimeError("User not found")
        return {
            "name": user.name,
            "experience_level": user.experience_level,
            "goals": user.goals,
            "preferred_topics": user.preferred_topics,
        }
    finally:
        db.close()


@router.put("/profile")
def update_profile(profile: UserProfile, current_user=Depends(get_current_user)):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == current_user.id).first()
        if not user:
            raise RuntimeError("User not found")

        user.name = profile.name
        user.experience_level = profile.experience_level
        user.goals = profile.goals
        user.preferred_topics = profile.preferred_topics

        db.commit()
        db.refresh(user)

        return {"message": "Profile Updated Successfully"}
    finally:
        db.close()
