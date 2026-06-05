
import joblib

from sklearn.ensemble import RandomForestRegressor

def train_best_model(
    X_train,
    y_train
):

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    joblib.dump(
        model,
        "models/best_student_model.pkl"
    )

    return model
