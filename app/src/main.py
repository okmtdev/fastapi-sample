from fastapi import FastAPI
from src.views.v1.pet import router as pet_router


app = FastAPI(title="sample-app", version="0.0.1", debug=True)

app.include_router(pet_router)
