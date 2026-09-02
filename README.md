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

## Requisitos

- Docker
- Docker Compose

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
- [Dockerfile](Dockerfile) — imagen del contenedor
- [docker-compose.yml](docker-compose.yml) — configuración de ejecución
- [requirements.txt](requirements.txt) — dependencias

## Ejemplo de request en Postman

- Método: GET
- URL: `http://localhost:8000/obtenercedula`
- Body: vacío

## Nota

La app está diseñada para ejecutarse en un contenedor y puede ser accesada desde el puerto 8000 del host.
