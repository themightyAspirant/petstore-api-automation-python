import pytest
from client.petstore_client import PetstoreClient
from helpers import PetPayloadGenerator
from test_data.schemas import validate_pet_response
from waiting import wait


class TestPetPositive:
    petstore_client = PetstoreClient()
    pet_payload_generator = PetPayloadGenerator()

    @pytest.fixture(scope="class", autouse=True)
    def cleanup_pet(self):
        yield
        if hasattr(self, "pet_id") and self.pet_id is not None:
            try:
                self.petstore_client.logger.info(f"Cleaning up pet with ID: {self.pet_id}")
                wait(
                    lambda: self.petstore_client.delete_pet(self.pet_id).status_code == 200,
                    timeout_seconds=30,
                    sleep_seconds=3,
                    waiting_for="Pet to be deleted."
                )
                self.petstore_client.logger.info(f"Successfully deleted pet with ID: {self.pet_id}")
            except TimeoutError:
                self.petstore_client.logger.warning(f"Timeout while deleting pet with ID: {self.pet_id}")
            except Exception as e:
                self.petstore_client.logger.error(f"Error deleting pet with ID {self.pet_id}: {str(e)}")


    def test_create_pet(self):
        payload = self.pet_payload_generator.generate_pet_payload()
        res = self.petstore_client.create_pet(payload)
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}. Response: {res.text}"
        pet = validate_pet_response(res.json())
        self.__class__.pet_id = pet.id
        self.petstore_client.logger.info(f"Created pet with ID: {self.pet_id}")


    def test_upload_pet_image(self, get_pet_id):
        image_path = "test_data/wolf.jpg"
        res = self.petstore_client.upload_pet_image(get_pet_id, "test", image_path)
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}. Response: {res.text}"


    def test_update_pet(self, get_pet_id):
        pet_details = self.petstore_client.get_pet_by_id(get_pet_id).json()
        pet_details["status"] = "sold"
        res = self.petstore_client.update_pet(pet_details)
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}. Response: {res.text}"
        pet = validate_pet_response(res.json())
        assert pet.status == "sold", f"Expected status {pet.status}, but got {pet.status}"


    def test_update_pet_form_data(self, get_pet_id):
        # For form data updates, only include name and status
        payload = {
            "name": self.pet_payload_generator._generate_pet_name(),
            "status": "sold"
        }
        res = self.petstore_client.update_pet_form_data(get_pet_id, payload)
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}. Response: {res.text}"

        updated_pet = self.petstore_client.get_pet_by_id(get_pet_id).json()
        assert updated_pet["name"] == payload["name"], f"Expected name {payload['name']}, but got {updated_pet['name']}"
        assert updated_pet["status"] == payload["status"], f"Expected status {payload['status']}, but got {updated_pet['status']}"


    def test_find_pet_by_id(self, get_pet_id):
        res = self.petstore_client.get_pet_by_id(get_pet_id)
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}. Response: {res.text}"


    @pytest.mark.parametrize("status", ["available", "pending", "sold"])
    def test_find_pet_by_status(self, status):
        res = self.petstore_client.get_pet_by_status(status)
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}. Response: {res.text}"
        
        for pet in res.json():
            assert pet["status"] == status, f"Expected status {status}, but got {pet['status']}"


    def test_delete_pet(self, get_pet_id):
        res = self.petstore_client.delete_pet(get_pet_id)
        assert res.status_code == 200, f"Expected status code 200, but got {res.status_code}. Response: {res.text}"
