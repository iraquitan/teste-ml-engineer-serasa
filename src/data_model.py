from typing import List
from pydantic import BaseModel


class Input(BaseModel):
    feat1: float
    feat2: float
    feat3: float


class Inputs(BaseModel):
    inputs: List[Input]