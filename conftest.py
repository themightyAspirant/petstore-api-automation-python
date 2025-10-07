import pytest
from dotenv import load_dotenv

# Load environment variables immediately when conftest.py is imported
load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Load environment variables from .env file."""
    load_dotenv()
