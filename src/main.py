from functools import lru_cache

import pandas as pd
from fastapi import FastAPI, UploadFile
from joblib import load

from src.preprocess import process_batch_input, process_file_input, process_single_input

from . import (api_contact_info, api_description, api_license_info,
               api_tags_metadata, api_terms_of_service, api_title, api_version,
               config)
from .data_model import Input, Inputs

app = FastAPI(
    title=api_title,
    description=api_description,
    openapi_tags=api_tags_metadata,
    version=api_version,
    terms_of_service=api_terms_of_service,
    contact=api_contact_info,
    license_info=api_license_info,
)

pipeline = {}


@lru_cache()
def get_settings():
    return config.Settings()


def run_pipeline(df:pd.DataFrame):
    x = pipeline["tfm"].transform(df.to_numpy())
    out = pipeline["clf"].predict(x)
    if out.shape[0] == 1:
        out = out[0]
    return out.tolist()


@app.on_event("startup")
async def startup_event():
    settings = get_settings()
    pipeline["tfm"] = load(settings.transformer_path)
    pipeline["clf"] = load(settings.classifier_path)
    # pipeline["tfm"] = load(r"C:\Users\iraqu\Developer\ml_engineering_serasa\transform[84].joblib")
    # pipeline["clf"] = load(r"C:\Users\iraqu\Developer\ml_engineering_serasa\classifier[27].joblib")


@app.get("/")
def read_root():
    return {
        "API_name": "Machine Learning API - Serasa",
        "endpoints": [
            {
                "/predict-single": "Predicts a single input with features (feat1, feat2, feat3)"
            },
            {
                "/predict-batch": "Predicts a batch of inputs with features (feat1, feat2, feat3)"
            },
            {
                "/predict-file": "Predicts a single CSV file with columns/features (feat1, feat2, feat3)"
            },
        ]
    }


@app.post("/predict-single", tags=["predict-single"])
def predict_single(x:Input):
    df = process_single_input(x)
    out = run_pipeline(df)
    return dict(prediction=out)


@app.post("/predict-batch", tags=["predict-batch"])
def predict_batch(X:Inputs):
    df = process_batch_input(X)
    out = run_pipeline(df)
    return dict(prediction=out)


@app.post("/predict-file", tags=["predict-file"])
def predict_file(file:UploadFile):
    df = process_file_input(file)
    if (df.empty):
        return {"error": "CSV file is empty"}
    out = run_pipeline(df)
    return dict(prediction=out)
