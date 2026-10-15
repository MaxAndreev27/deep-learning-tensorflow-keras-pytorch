import argparse
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--training-data", required=True)
    parser.add_argument("--model-output", required=True)
    parser.add_argument("--C", type=float, default=1.0)
    parser.add_argument("--max-iter", type=int, default=100)
    args = parser.parse_args()

    data = pd.read_csv(args.training_data)
    features = data.drop(columns="target")
    labels = data["target"].astype(int)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter)
    model.fit(features, labels)

    output_dir = Path(args.model_output)
    output_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_dir / "model.joblib")


if __name__ == "__main__":
    main()
