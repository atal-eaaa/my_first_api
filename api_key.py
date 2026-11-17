import fastapi
import os
from dotenv import load_dotenv
import secrets
from fastapi import Security
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

load_dotenv()                      # læser .env ind i miljøet
API_KEY = os.environ["API_KEY"]    # crasher ved opstart hvis den mangler, og det er godt

def verify_api_key(api_key: str | None = Security(api_key_header)):
    if api_key is None or not secrets.compare_digest(api_key, API_KEY):
        raise fastapi.HTTPException(status_code=401, detail="Ugyldig API-nøgle")


