import json
import os
from pathlib import Path

import joblib
import numpy as np


def init():
    global model
    model_path = Path(os.environ["AZUREML_MODEL_DIR"]) / "model.joblib"
    model = joblib.load(model_path)


def run(raw_data):
    request = json.loads(raw_data)
    if "data" not in request:
        raise ValueError("Request JSON must include a 'data' field.")

    features = np.asarray(request["data"], dtype=float)
    predictions = model.predict(features)
    return {"predictions": predictions.tolist()}
