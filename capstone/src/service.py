# capstone/src/service.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Dict, Any

# Import the mock ML pipeline functions
from .ml_pipeline import infer

# Initialize the FastAPI app
app = FastAPI(
    title="Privacy-aware Intelligent Service",
    description="A service that provides personalized recommendations.",
    version="1.0.0",
)

# --- Pydantic Models for Request and Response ---
# These models are based on the OpenAPI specification.

class RecommendationRequest(BaseModel):
    user_id: str = Field(..., example="user-123", description="The ID of the user.")
    context: Dict[str, Any] = Field({}, example={"device": "mobile"}, description="Additional context for the request.")

class RecommendationResponse(BaseModel):
    user_id: str = Field(..., example="user-123")
    recommendations: List[str] = Field(..., example=["item_42", "item_99"])
    confidence: float = Field(..., example=0.95)

class HealthResponse(BaseModel):
    status: str = Field(..., example="ok")

# --- API Endpoints ---

@app.post("/recommendations", response_model=RecommendationResponse)
async def get_recommendations(request: RecommendationRequest):
    """
    Receives a user ID and context, and returns personalized recommendations.
    This endpoint integrates with the mock ML pipeline's infer function.
    """
    if not request.user_id:
        raise HTTPException(status_code=400, detail="user_id is required")

    try:
        # Call the mock ML inference function
        inference_data = {"user_id": request.user_id, "context": request.context}
        result = infer(inference_data)

        # Ensure the response from the ML pipeline matches our contract
        response = RecommendationResponse(**result)
        return response
    except Exception as e:
        # In a real app, you'd have more specific error handling
        raise HTTPException(status_code=500, detail=f"An internal error occurred: {e}")

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    A simple health check endpoint to confirm the service is running.
    """
    return HealthResponse(status="ok")

# To run this service locally:
# uvicorn capstone.src.service:app --reload
