from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class GreetingResponse(BaseModel):
    """Schema for greeting responses"""
    message: str
    timestamp: str
    status: Optional[str] = None
    version: Optional[str] = None

class InfoResponse(BaseModel):
    """Schema for API information response"""
    api_name: str
    description: str
    version: str
    endpoints: List[str]
    timestamp: str
