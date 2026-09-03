# Servicio FastAPI para obtener una cédula aleatoria

Este proyecto expone un servicio web en FastAPI con el endpoint:

- GET /obtenercedula

El servicio devuelve un número entero aleatorio de 10 dígitos, dentro del rango:

- Mínimo: 1000000000
- Máximo: 9999999999

El valor nunca inicia con cero.

## Endpoint

### Request

```http
GET /obtenercedula
```

### Payload

No requiere payload ni body en la petición, porque es un endpoint GET simple.

### Ejemplo de respuesta

```json
1234567890
```

Respuesta esperada en JSON:

```json
1234567890
```

## Swagger

FastAPI genera automáticamente la documentación Swagger en:

```text
http://localhost:8000/docs
```

También puedes consultar la especificación OpenAPI en:

```text
http://localhost:8000/openapi.json
```

Y además el proyecto incluye una vista personalizada en:

```text
http://localhost:8000/swagger.html
```

## Requisitos

- Python 3.12+
- Docker
- Docker Compose
- GitHub
- Cuenta en Render

## Ejecutar localmente con Python

Desde la raíz del proyecto:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Luego abre:

```text
http://localhost:8000/obtenercedula
```

## Levantar el servicio con Docker Compose

Desde la raíz del proyecto, ejecuta:

```bash
docker compose up --build
```

Esto construirá la imagen y levantará el contenedor.

Luego puedes abrir:

```text
http://localhost:8000/obtenercedula
```

## Verificar el servicio

Puedes probarlo con curl:

```bash
curl http://localhost:8000/obtenercedula
```

También puedes validar la página Swagger:

```bash
curl http://localhost:8000/swagger.html
```

## Detener el servicio

```bash
docker compose down
```

## Colección de Postman

Se incluye una colección lista para importar en Postman en el archivo:

- [postman_collection.json](postman_collection.json)

### Importar la colección

1. Abre Postman.
2. Haz clic en Import.
3. Selecciona [postman_collection.json](postman_collection.json).
4. Ejecuta la petición `GET /obtenercedula`.

## Estructura del proyecto

- [main.py](main.py) — aplicación FastAPI
- [swagger.html](swagger.html) — interfaz Swagger personalizada
- [Dockerfile](Dockerfile) — imagen del contenedor
- [docker-compose.yml](docker-compose.yml) — configuración de ejecución
- [requirements.txt](requirements.txt) — dependencias
- [.github/workflows/render-deploy.yml](.github/workflows/render-deploy.yml) — despliegue continuo con GitHub Actions hacia Render

## Despliegue continuo con GitHub Actions y Render

Este repositorio incluye un workflow de GitHub Actions para desplegar automáticamente en Render:

- Archivo: [.github/workflows/render-deploy.yml](.github/workflows/render-deploy.yml)

### Configuración necesaria

1. En Render, crea o selecciona tu servicio web.
2. Copia la URL del Deploy Hook.
3. En GitHub, ve a:
   - Settings → Secrets and variables → Actions
4. Crea el secreto:
   - `RENDER_DEPLOY_HOOK_URL`
5. Pega ahí el Deploy Hook de Render.

### Qué hace el workflow

- Se ejecuta en cada push a la rama `main`
- También puede ejecutarse manualmente con `workflow_dispatch`
- Llama al Deploy Hook de Render usando `curl` para disparar el despliegue

Ejemplo del workflow:

```yaml
name: Deploy to Render

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Render
        env:
          RENDER_DEPLOY_HOOK_URL: ${{ secrets.RENDER_DEPLOY_HOOK_URL }}
        run: |
          curl --fail --silent --show-error -X POST "$RENDER_DEPLOY_HOOK_URL"
```

## Ejemplo de request en Postman

- Método: GET
- URL: `http://localhost:8000/obtenercedula`
- Body: vacío

## Nota

La app está diseñada para ejecutarse en un contenedor y puede ser accesada desde el puerto 8000 del host. Además, incluye una automatización básica para despliegues continuos en Render usando GitHub Actions.
