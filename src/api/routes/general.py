from fastapi import APIRouter
from datetime import datetime
from typing import Dict, Any, List
from src.api.schemas.general import GreetingResponse, InfoResponse

router = APIRouter(
    tags=["general"],
)

@router.get("/", response_model=GreetingResponse)
def root() -> Dict[str, Any]:
    """
    Root endpoint with generic greeting.
    """
    return {
        "message": "Welcome to the Generic API",
        "status": "active",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

@router.get("/hello/{name}", response_model=GreetingResponse)
def hello(name: str) -> Dict[str, str]:
    """
    Personalized greeting endpoint.
    """
    return {
        "message": f"Hello, {name}!",
        "timestamp": datetime.now().isoformat()
    }

@router.get("/info", response_model=InfoResponse)
def get_info() -> Dict[str, Any]:
    """
    General information about the API.
    """
    return {
        "api_name": "Generic API",
        "description": "A simple and generic API for basic operations",
        "version": "1.0.0",
        "endpoints": ["/", "/health", "/hello/{name}", "/info"],
        "timestamp": datetime.now().isoformat()
    }
