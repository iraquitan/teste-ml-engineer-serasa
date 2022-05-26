from fastapi import UploadFile
import pandas as pd
from src.data_model import Input, Inputs


def process_single_input(x:Input):
    df = pd.DataFrame([x.dict()])
    return df


def process_batch_input(X:Inputs):
    df = pd.DataFrame([xi.dict() for xi in X.inputs])
    return df


def process_file_input(file:UploadFile):
    try:
        df = pd.read_csv(
            file.file,
            sep=",",
            usecols=["feat1", "feat2", "feat3"],
            dtype={
                "feat1": float,
                "feat2": float,
                "feat3": float,
            })
    except (UnicodeDecodeError, ValueError) as err:
        msg = f"{err}"
        return {"error": msg}
    return df