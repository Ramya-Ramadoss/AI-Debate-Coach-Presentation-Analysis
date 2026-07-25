import os
import unittest
from uuid import uuid4
from fastapi.testclient import TestClient

from main import app
from database import SessionLocal
from models import User


class AuthFlowTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        self.email = f"test-{uuid4().hex[:8]}@example.com"

    def tearDown(self):
        self.db.query(User).filter(User.email == self.email).delete()
        self.db.commit()
        self.db.close()

    def test_register_login_and_profile_flow(self):
        register_response = self.client.post(
            "/register",
            json={
                "name": "Test User",
                "email": self.email,
                "password": "StrongPass123!",
                "role": "Learner",
            },
        )
        self.assertEqual(register_response.status_code, 200)

        login_response = self.client.post(
            "/login",
            data={"username": self.email, "password": "StrongPass123!"},
        )
        self.assertEqual(login_response.status_code, 200)
        token = login_response.json()["access_token"]
        self.assertTrue(token)

        headers = {"Authorization": f"Bearer {token}"}

        profile_create_response = self.client.post(
            "/profile",
            json={
                "name": "Test User",
                "experience_level": "Intermediate",
                "goals": "Improve public speaking",
                "preferred_topics": "AI, ethics",
            },
            headers=headers,
        )
        self.assertEqual(profile_create_response.status_code, 200)

        profile_get_response = self.client.get("/profile", headers=headers)
        self.assertEqual(profile_get_response.status_code, 200)
        self.assertEqual(profile_get_response.json()["name"], "Test User")

        profile_update_response = self.client.put(
            "/profile",
            json={
                "name": "Test User",
                "experience_level": "Advanced",
                "goals": "Lead debates",
                "preferred_topics": "Policy, current affairs",
            },
            headers=headers,
        )
        self.assertEqual(profile_update_response.status_code, 200)

    def test_role_restriction(self):
        register_response = self.client.post(
            "/register",
            json={
                "name": "Coach User",
                "email": f"coach-{uuid4().hex[:8]}@example.com",
                "password": "StrongPass123!",
                "role": "Coach",
            },
        )
        self.assertEqual(register_response.status_code, 200)

        login_response = self.client.post(
            "/login",
            data={"username": register_response.json().get("email") if register_response.json().get("email") else None, "password": "StrongPass123!"},
        )
        self.assertEqual(login_response.status_code, 200)

        token = login_response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        learner_response = self.client.get("/learner", headers=headers)
        self.assertEqual(learner_response.status_code, 403)

        coach_response = self.client.get("/coach", headers=headers)
        self.assertEqual(coach_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
