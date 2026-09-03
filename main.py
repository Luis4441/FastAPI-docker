from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
from pathlib import Path

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
    return random.randint(1_000_000_000, 9_999_999_999)


@app.get("/numeroromano")
@app.get("/romano")
def obtener_numero_romano() -> str:
    numero = random.randint(50, 100)
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

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)