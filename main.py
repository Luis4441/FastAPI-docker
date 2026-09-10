import os
import secrets
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Servicio de cédula")


def int_to_roman(number: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""
    for value, numeral in zip(values, numerals):
        while number >= value:
            roman += numeral
            number -= value
    return roman


@app.get("/obtenercedula")
def obtener_cedula() -> int:
    # Use a cryptographically secure PRNG for identifiers
    # Range: 1_000_000_000 .. 9_999_999_999 inclusive
    return secrets.randbelow(9_000_000_000) + 1_000_000_000


@app.get("/numeroromano")
@app.get("/romano")
def obtener_numero_romano() -> str:
    # Secure random integer between 50 and 100 inclusive
    numero = secrets.randbelow(51) + 50
    return int_to_roman(numero)


@app.get("/duplicar")
def duplicar_numero(numero: int) -> int:
    return numero * 2


@app.get("/swagger.html", response_class=HTMLResponse)
def swagger_html():
    ruta_swagger = Path(__file__).parent / "swagger.html"

    with open(ruta_swagger, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "127.0.0.1")
    uvicorn.run("main:app", host=host, port=8000, reload=True)