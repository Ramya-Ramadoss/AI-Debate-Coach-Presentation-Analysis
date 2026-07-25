from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, default="")
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column("password", String, nullable=False)
    role = Column(String, nullable=False, default="Learner")

    experience = Column(String, default="")
    experience_level = Column(String, default="")
    goals = Column(String, default="")
    preferred_topics = Column(String, default="")
    presentation_domain = Column(String, default="")
    coaching_preference = Column(String, default="")
    debate_history = Column(Integer, default=0)
    presentations_given = Column(Integer, default=0)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, value):
        self.hashed_password = value
