from pydantic import BaseModel, Field

class MessageSch(BaseModel):
    chat_id: int
    text: str
    priority: int = Field(default=1, ge=0, le=10)