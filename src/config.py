from pydantic import BaseSettings


class Settings(BaseSettings):
    transformer_path: str
    classifier_path: str

    class Config:
        env_file = ".env"