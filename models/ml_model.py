import os
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

def train_dummy_model():
    X = np.array([[1],[2],[3],[4]])
    y = np.array([3,5,7,9])
    model = LinearRegression().fit(X,y)

    input_example = [[5]]

    with mlflow.start_run() as run:
        mlflow.log_param("model_type","LinearRegression")
        mlflow.log_metric("r2",model.score(X,y))
        mlflow.sklearn.log_model(
            sk_model = model,
            artifact_path = "model",
            input_example = input_example,
            signature = mlflow.models.signature.infer_signature(X,y)
        )
    return run.info.run_id

def predict_dummy(input_data):
    return sum(input_data.values())


#train_dummy_model()
