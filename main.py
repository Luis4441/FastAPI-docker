from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="Servicio de cédula")


@app.get("/obtenercedula")
def obtener_cedula() -> int:
    return random.randint(1_000_000_000, 9_999_999_999)


@app.get("/swagger.html", response_class=HTMLResponse)
def swagger_html():
    with open("swagger.html", "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
