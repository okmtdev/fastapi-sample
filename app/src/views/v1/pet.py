from fastapi import APIRouter

router = APIRouter(prefix="/v1/pet")


@router.get("/{id}")
async def get_pet(id: int):
    print(id)
    return {"pet": {"id": 0, "name": "john", "age": 2, "species": "dog"}}


@router.get("s")
async def list_pets(
    name: str | None = None,
    age: int | None = None,
    species: str | None = None,
    limit: int = 10,
):
    return {
        "pets": [
            {"name": "John", "age": 2, "species": "dog"},
            {"name": "Party", "age": 2, "species": "parrot"},
            {"name": "Kenny", "age": 8, "species": "cat"},
        ]
    }


# @router.post("")
