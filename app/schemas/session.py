from pydantic import BaseModel
from datetime import datetime


class SessionResponse(BaseModel):
    session_token: str
    expires_at: datetime