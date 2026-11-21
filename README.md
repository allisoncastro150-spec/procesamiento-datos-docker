
# Procesamiento de Datos con Python y Docker

## Descripción

Este proyecto permite procesar archivos CSV mediante Python y pandas dentro de un contenedor Docker.

El programa elimina registros duplicados, elimina filas con valores vacíos y calcula estadísticas básicas de los datos.

## Tecnologías utilizadas

- Python 3.12.8
- Pandas 2.2.3
- Docker
- Docker Hub

## Imagen publicada

La imagen está disponible en Docker Hub:

https://hub.docker.com/r/almict/procesamiento-datos

Versión: 1.0

## Estructura del proyecto

```text
procesamiento-datos-docker/
├── app/
│   └── procesar.py
├── data/
│   └── entrada.csv
├── output/
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Construcción de la imagen

```bash
docker build -t procesamiento-datos:1.0 .
```

## Ejecución del contenedor

En PowerShell:

```powershell
docker run --rm `
  -v "${PWD}\data:/app/data" `
  -v "${PWD}\output:/app/output" `
  almict/procesamiento-datos:1.0
```

## Variables de entorno

| Variable | Descripción | Valor predeterminado |
|---|---|---|
| INPUT_FILE | Ruta del CSV de entrada | /app/data/entrada.csv |
| OUTPUT_FILE | Ruta del CSV de salida | /app/output/resultado.csv |

Se pueden personalizar las rutas mediante las opciones -e de Docker.

## Volúmenes

| Volumen | Función |
|---|---|
| /app/data | Contiene los archivos CSV de entrada |
| /app/output | Almacena los resultados procesados |

## Resultado esperado

El archivo de ejemplo contiene 7 registros originales.

Después del procesamiento:
- Se eliminan los registros duplicados.
- Se conservan 6 registros.
- Se calcula la edad promedio: 30.00.
- Se calcula el salario promedio: 816.67.

El resultado se guarda en:

`output/resultado.csv`

## Descargar la imagen publicada

```bash
docker pull almict/procesamiento-datos:1.0
```

## Tecnologías y buenas prácticas

- Imagen base Python Slim con versión fija.
- Dependencias con versiones definidas.
- Instalación de dependencias antes de copiar el código.
- Usuario sin privilegios.
- Rutas configurables mediante variables de entorno.
- Uso de volúmenes para entrada y salida.
- Exclusión de archivos innecesarios mediante .dockerignore.
