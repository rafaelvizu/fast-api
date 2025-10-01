from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str = Field(..., example="Error message describing the issue.")