
from fastapi import FastAPI, HTTPException

from src.api.schema import StudentInput
from src.api.logger import logger

from src.models.predict import predict_student

app = FastAPI(
    title="Student Intelligence API",
    version="1.0"
)

@app.get("/")
def home():

    return {
        "message":
        "Student Intelligence API Running"
    }

@app.get("/health")
def health():

    return {
        "status":
        "healthy"
    }

@app.post("/predict")
def predict(
    student: StudentInput
):

    try:

        prediction = predict_student(
            student.studytime,
            student.failures,
            student.absences
        )

        logger.info(
            f"Prediction generated: {prediction}"
        )

        return {
            "predicted_grade":
            prediction
        }

    except Exception as e:

        logger.error(str(e))

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
