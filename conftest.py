import pytest
import random
from dotenv import load_dotenv
from client.petstore_client import PetstoreClient
from logger.logger import get_logger

# Load environment variables immediately when conftest.py is imported
load_dotenv()

logger = get_logger(__name__)


@pytest.fixture(scope="session", autouse=True)
def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

@pytest.fixture(scope="class")
def get_pet_id():
    petstore_client = PetstoreClient()
    try:
        logger.info("Fetching available pets to get random pet ID")
        response = petstore_client.get_pet_by_status("available")
        
        if response.status_code != 200:
            raise RuntimeError(f"Failed to fetch pets. Status code: {response.status_code}")
        
        pets = response.json()
        
        if not pets:
            raise RuntimeError("No available pets found in the system")
        
        # Select a random pet
        selected_pet = random.choice(pets)
        pet_id = selected_pet["id"]
        
        logger.info(f"Selected pet ID: {pet_id} from {len(pets)} available pets")
        return pet_id
        
    except Exception as e:
        logger.error(f"Error getting pet ID: {str(e)}")
        raise RuntimeError(f"Failed to get pet ID: {str(e)}") from e