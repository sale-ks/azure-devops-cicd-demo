import unittest
from src.app import get_status


class TestApplication(unittest.TestCase):

    def test_application_status(self):
        result = get_status()
        self.assertEqual(result["status"], "healthy")

    def test_application_name(self):
        result = get_status()
        self.assertEqual(
            result["application"],
            "Azure DevOps CI/CD Demo"
        )

    def test_environment(self):
        result = get_status()
        self.assertEqual(result["environment"], "development")

    def test_timestamp_exists(self):
        result = get_status()
        self.assertIsNotNone(result["timestamp"])


if __name__ == "__main__":
    unittest.main()
