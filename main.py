import secrets
import string
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Generador de contraseñas")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class PasswordOptions(BaseModel):
    length: int = Field(default=16, ge=4, le=128)
    lowercase: bool = True
    uppercase: bool = True
    numbers: bool = True
    symbols: bool = True


def generate_password(options: PasswordOptions) -> str:
    groups = []
    if options.lowercase:
        groups.append(string.ascii_lowercase)
    if options.uppercase:
        groups.append(string.ascii_uppercase)
    if options.numbers:
        groups.append(string.digits)
    if options.symbols:
        groups.append("!@#$%^&*()-_=+[]{};:,.?/|~")

    if not groups:
        raise ValueError("Selecciona al menos un tipo de carácter.")

    alphabet = "".join(groups)
    password = [secrets.choice(group) for group in groups]
    password.extend(
        secrets.choice(alphabet) for _ in range(options.length - len(password))
    )
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


@app.get("/", include_in_schema=False)
def home() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/generate")
def create_password(options: PasswordOptions) -> dict[str, str]:
    try:
        password = generate_password(options)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
    return {"password": password}
