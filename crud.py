from sqlalchemy.orm import Session
from models import User
from security import hash_password


def create_user(db: Session, user):
    db_user = User(
        name=user.name.strip(),
        email=str(user.email).lower(),
        password=hash_password(user.password),
        role=user.role,
        experience="Beginner",
        experience_level="",
        goals="",
        preferred_topics="",
        presentation_domain="",
        coaching_preference="",
        debate_history=0,
        presentations_given=0,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):
    normalized_email = str(email).strip().lower()
    return db.query(User).filter(User.email == normalized_email).first()