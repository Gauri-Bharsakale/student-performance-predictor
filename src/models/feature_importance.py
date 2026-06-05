
import pandas as pd

def show_feature_importance(
    model,
    X
):

    importance = pd.DataFrame(
        {
            "Feature": X.columns,
            "Importance": model.feature_importances_
        }
    )

    importance = importance.sort_values(
        "Importance",
        ascending=False
    )

    print(
        "\nTop Important Features:\n"
    )

    print(
        importance.head(10)
    )
