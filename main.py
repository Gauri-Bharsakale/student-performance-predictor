
from pipelines.train_pipeline import main as train_main
from pipelines.predict_pipeline import main as predict_main


def main():

    print("\n🎓 Student Intelligence System")
    print("\n1. Train Model")
    print("2. Test Prediction")

    choice = input("\nSelect option: ")

    if choice == "1":
        train_main()

    elif choice == "2":
        predict_main()

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
