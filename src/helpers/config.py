from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    CHROMA_API_KEY: str
    CHROMA_TENANT: str
    CHROMA_DATABASE: str
    GEMINI_API_KEY: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
