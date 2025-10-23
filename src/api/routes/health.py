from fastapi import APIRouter
from datetime import datetime
from typing import Dict, Any

router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("/")
def health_check() -> Dict[str, Any]:
    """
    Health check endpoint that returns API status.
    """
    return {
        "status": "healthy",
        "service": "Generic API",
        "timestamp": datetime.now().isoformat(),
        "uptime": "running",
        "version": "1.0.0"
    }
