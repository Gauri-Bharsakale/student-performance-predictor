
import streamlit as st

from src.models.predict import (
    predict_student
)

st.set_page_config(
    page_title="Student Intelligence System",
    layout="centered"
)

st.title(
    "🎓 Student Intelligence System"
)

st.write(
    "Predict Student Final Grade"
)

studytime = st.slider(
    "Study Time",
    min_value=1,
    max_value=10,
    value=4
)

failures = st.slider(
    "Failures",
    min_value=0,
    max_value=10,
    value=0
)

absences = st.slider(
    "Absences",
    min_value=0,
    max_value=50,
    value=2
)

if st.button(
    "Predict Grade"
):

    prediction = predict_student(
        studytime,
        failures,
        absences
    )

    st.success(
        f"Predicted Grade: {prediction}"
    )
