
import joblib
import pandas as pd


MODEL_PATH = "models/best_student_model.pkl"


def load_model():

    model = joblib.load(
        MODEL_PATH
    )

    return model


def predict_student(
    studytime,
    failures,
    absences
):

    model = load_model()

    input_data = pd.DataFrame(
        {
            "studytime": [studytime],
            "failures": [failures],
            "absences": [absences]
        }
    )

    prediction = model.predict(
        input_data
    )[0]

    return round(
        prediction,
        2
    )
