import argparse
import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_depth", type=int, default=5)
    parser.add_argument("--n_estimators", type=int, default=100)
    args = parser.parse_args()

    train_dir = os.environ["SM_CHANNEL_TRAIN"]
    train_data = pd.read_csv(os.path.join(train_dir, "iris_train.csv"))
    features = train_data.drop(columns="target").to_numpy()
    labels = train_data["target"].astype(int)

    classifier = RandomForestClassifier(
        max_depth=args.max_depth,
        n_estimators=args.n_estimators,
        random_state=42,
    )
    classifier.fit(features, labels)

    model_dir = os.environ["SM_MODEL_DIR"]
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(classifier, os.path.join(model_dir, "model.joblib"))


if __name__ == "__main__":
    main()
