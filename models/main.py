from fastapi import FastAPI, Request
from models.ml_model import train_dummy_model, predict_dummy
import uvicorn

app = FastAPI()

@app.post("/train")
def train_model():
    run_id = train_dummy_model()
    return {"status":"trained","ml_flow_runid":run_id}

@app.post("/predict")
def predict(input_data:dict):
    result = predict_dummy(input_data)
    return {"prediction" : result}

if __name__ == "__main__":
    uvicorn(app,host="0.0.0.0",port = 8080)
