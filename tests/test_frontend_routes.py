import unittest

from fastapi.testclient import TestClient

from main import app


class FrontendRoutesTests(unittest.TestCase):
    def test_root_serves_frontend_html(self):
        client = TestClient(app)
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Debate Coach", response.text)


if __name__ == "__main__":
    unittest.main()
