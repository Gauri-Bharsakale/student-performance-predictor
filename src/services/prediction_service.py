from src.models.predict import predict_student

def run_prediction():

    print("\nRunning prediction...\n")

    studytime = 4
    failures = 0
    absences = 2

    result = predict_student(
        studytime,
        failures,
        absences
    )

    print(f"Predicted Grade: {result}")