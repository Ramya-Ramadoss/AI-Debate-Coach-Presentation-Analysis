from typing import Literal
from pydantic import BaseModel, EmailStr, field_validator


class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Literal["Learner", "Coach", "Educator", "Admin"] = "Learner"

    @field_validator("name", "password")
    @classmethod
    def validate_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Value cannot be empty")
        return value.strip()

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value.strip()) < 8:
            raise ValueError("Password must be at least 8 characters")
        return value

    @field_validator("role")
    @classmethod
    def validate_role(cls, value: str) -> str:
        return value.strip().title()


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserProfile(BaseModel):
    name: str
    experience_level: str
    goals: str
    preferred_topics: str

    @field_validator("name", "experience_level", "goals", "preferred_topics")
    @classmethod
    def validate_non_empty(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Value cannot be empty")
        return value.strip()