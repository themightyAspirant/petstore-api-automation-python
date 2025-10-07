from tkinter import NO
import pytest
from client.petstore_client import PetstoreClient
from helpers.pet_payload_generator import PetPayloadGenerator
from test_data.schemas import validate_pet_response
from waiting import wait

class TestPetPositive:
    petstore_client = PetstoreClient()
    pet_payload_generator = PetPayloadGenerator()

    @pytest.fixture(scope="class", autouse=True)
    def _cleanup_pet(self):
        yield
        if hasattr(self, "pet_id") and self.pet_id is not None:
            try:
                wait(
                    lambda: self.petstore_client.delete_pet(self.pet_id).status_code == 200,
                    timeout_seconds=10,
                    sleep_seconds=1.5,
                    waiting_for="Pet to be deleted."
                )
            except TimeoutError:
                pass

    def test_create_pet(self):
        payload = self.pet_payload_generator.generate_pet_payload()
        res = self.petstore_client.create_pet(payload)
        assert res.status_code == 200
        pet = validate_pet_response(res.json())
        self.pet_id = pet.id

    
    def test_upload_pet_image(self):
        image_path = "test_data/wolf.jpg"
        res = self.petstore_client.upload_pet_image(5376619, "test", image_path)
        assert res.status_code == 200