import os
import json

from client.base_client import BaseClient
from logger.logger import get_logger


class PetstoreClient(BaseClient):
    def __init__(self):
        _base_url = os.environ["PETSTORE_API_BASEURL"] + "/" + os.environ["PETSTORE_API_VERSION"]
        self.logger = get_logger(__name__)
        super().__init__(_base_url)

    # PET ENDPOINTS
    def create_pet(self, payload: dict):
        return self.post("/pet", json=payload)

    def upload_pet_image(self, pet_id: int, additional_metadata: str, file_path: str):
        url = f"/pet/{pet_id}/uploadImage"

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Prepare form data
        files = {'file': open(file_path, 'rb')}
        data = {'additionalMetadata': additional_metadata}
        
        try:
            response = self.post(url, files=files, data=data)
            return response
        finally:
            # Close the file
            files['file'].close()

    def get_pet_by_id(self, pet_id: int):
        return self.get(f"/pet/{pet_id}")

    def get_pet_by_status(self, status: str):
        return self.get(f"/pet/findByStatus", params={"status": status})

    def update_pet(self, payload: dict):
        return self.put("/pet", json=payload)

    def update_pet_form_data(self, pet_id: int, payload: dict):
        return self.post(f"/pet/{pet_id}", data=payload)

    def delete_pet(self, pet_id: int):
        return self.delete(f"/pet/{pet_id}")

    