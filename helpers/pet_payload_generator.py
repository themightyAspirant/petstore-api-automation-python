import random
from typing import Dict, List, Optional
from faker import Faker

fake = Faker()


class PetPayloadGenerator:
    """Utility class to generate pet payloads for API testing."""
    
    # Pet statuses
    STATUSES = ["available", "pending", "sold"]
    
    # Common pet categories
    CATEGORIES = [
        {"id": 1, "name": "Dogs"},
        {"id": 2, "name": "Cats"},
        {"id": 3, "name": "Birds"},
        {"id": 4, "name": "Fish"},
        {"id": 5, "name": "Rabbits"},
        {"id": 6, "name": "Hamsters"},
        {"id": 7, "name": "Reptiles"},
        {"id": 8, "name": "Other"}
    ]
    
    # Common pet tags
    TAGS = [
        {"id": 1, "name": "friendly"},
        {"id": 2, "name": "playful"},
        {"id": 3, "name": "calm"},
        {"id": 4, "name": "energetic"},
        {"id": 5, "name": "cute"},
        {"id": 6, "name": "loyal"},
        {"id": 7, "name": "intelligent"},
        {"id": 8, "name": "gentle"},
        {"id": 9, "name": "active"},
        {"id": 10, "name": "quiet"}
    ]
    
    @classmethod
    def generate_pet_payload(
        cls,
        pet_id: Optional[int] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        category: Optional[Dict] = None,
        tags: Optional[List[Dict]] = None,
        photo_urls: Optional[List[str]] = None
    ) -> Dict:
        """
        Generate a pet payload with specified or random values.
        
        Args:
            pet_id: Pet ID (if None, generates random)
            name: Pet name (if None, generates random)
            status: Pet status (if None, generates random)
            category: Pet category (if None, generates random)
            tags: Pet tags (if None, generates random)
            photo_urls: Photo URLs (if None, generates random)
            
        Returns:
            Dict: Pet payload
        """
        return {
            "id": pet_id or random.randint(1000000, 9999999),
            "category": category or cls._generate_category(),
            "name": name or cls._generate_pet_name(),
            "photoUrls": photo_urls or cls._generate_photo_urls(),
            "tags": tags or cls._generate_tags(),
            "status": status or random.choice(cls.STATUSES)
        }
    
    @classmethod
    def generate_available_pet(cls, **kwargs) -> Dict:
        """Generate a pet with 'available' status."""
        return cls.generate_pet_payload(status="available", **kwargs)
    
    @classmethod
    def generate_pending_pet(cls, **kwargs) -> Dict:
        """Generate a pet with 'pending' status."""
        return cls.generate_pet_payload(status="pending", **kwargs)
    
    @classmethod
    def generate_sold_pet(cls, **kwargs) -> Dict:
        """Generate a pet with 'sold' status."""
        return cls.generate_pet_payload(status="sold", **kwargs)
    
    @classmethod
    def generate_dog_payload(cls, **kwargs) -> Dict:
        """Generate a dog payload."""
        return cls.generate_pet_payload(
            category={"id": 1, "name": "Dogs"},
            name=cls._generate_dog_name(),
            **kwargs
        )
    
    @classmethod
    def generate_cat_payload(cls, **kwargs) -> Dict:
        """Generate a cat payload."""
        return cls.generate_pet_payload(
            category={"id": 2, "name": "Cats"},
            name=cls._generate_cat_name(),
            **kwargs
        )
    
    @classmethod
    def _generate_category(cls) -> Dict:
        """Generate a random category."""
        return random.choice(cls.CATEGORIES)
    
    @classmethod
    def _generate_pet_name(cls) -> str:
        """Generate a random pet name using Faker."""
        return fake.first_name()
    
    @classmethod
    def _generate_dog_name(cls) -> str:
        """Generate a random dog name."""
        dog_names = [
            "Buddy", "Max", "Charlie", "Cooper", "Rocky", "Jack", "Bear",
            "Duke", "Tucker", "Zeus", "Bentley", "Jake", "Blue", "Rex"
        ]
        return random.choice(dog_names)
    
    @classmethod
    def _generate_cat_name(cls) -> str:
        """Generate a random cat name."""
        cat_names = [
            "Bella", "Lucy", "Luna", "Milo", "Sadie", "Molly", "Chloe",
            "Sophie", "Lola", "Mia", "Lily", "Nala", "Zoe", "Stella"
        ]
        return random.choice(cat_names)
    
    @classmethod
    def _generate_photo_urls(cls) -> List[str]:
        """Generate random photo URLs using Faker."""
        num_photos = fake.random_int(min=1, max=3)
        return [fake.image_url() for _ in range(num_photos)]
    
    @classmethod
    def _generate_tags(cls) -> List[Dict]:
        """Generate random tags."""
        num_tags = random.randint(1, 3)
        return random.sample(cls.TAGS, num_tags)
    
    @classmethod
    def get_available_statuses(cls) -> List[str]:
        """Get list of available pet statuses."""
        return cls.STATUSES.copy()
    
    @classmethod
    def get_available_categories(cls) -> List[Dict]:
        """Get list of available categories."""
        return cls.CATEGORIES.copy()
    
    @classmethod
    def get_available_tags(cls) -> List[Dict]:
        """Get list of available tags."""
        return cls.TAGS.copy()