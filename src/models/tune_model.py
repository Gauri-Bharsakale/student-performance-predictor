
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

def tune_model(
    X_train,
    y_train
):

    params = {
        "n_estimators": [100, 200],
        "max_depth": [5, 10, None]
    }

    model = RandomForestRegressor(
        random_state=42
    )

    grid = GridSearchCV(
        model,
        params,
        cv=3,
        scoring="r2",
        n_jobs=-1
    )

    grid.fit(
        X_train,
        y_train
    )

    return grid.best_estimator_
