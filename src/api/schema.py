from pydantic import BaseModel, Field

class StudentInput(BaseModel):

    studytime: int = Field(
        ...,
        ge=1,
        le=10,
        description="Study time"
    )

    failures: int = Field(
        ...,
        ge=0,
        le=10,
        description="Past failures"
    )

    absences: int = Field(
        ...,
        ge=0,
        le=100,
        description="Student absences"
    )
