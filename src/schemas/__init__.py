from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str = Field(..., example="Error message describing the issue.")

class PaginationRequest(BaseModel):
    page: int = Field(1, ge=1, description="Current page number")
    size: int = Field(10, ge=1, le=100, description="Number of items per page")


class PaginationResponse(PaginationRequest):
    total: int = Field(0, ge=0, description="Total number of items")
    total_pages: int = Field(0, ge=0, description="Total number of pages")
    has_next: bool = Field(False, description="Indicates if there is a next page")
    