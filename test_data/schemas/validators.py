from test_data.schemas.pet_models import PetResponse

def validate_pet_response(data: dict) -> PetResponse:
    """Validate pet response using model_validate."""
    return PetResponse.model_validate(data)
