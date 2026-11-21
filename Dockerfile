
FROM python:3.12.8-slim

WORKDIR /app

# Instalar dependencias primero para aprovechar la caché
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Crear usuario sin privilegios
RUN useradd --create-home appuser

# Copiar el código y los datos de ejemplo
COPY app/ ./app/

# Crear directorios de entrada y salida
RUN mkdir -p /app/data /app/output \
    && chown -R appuser:appuser /app

# Ejecutar sin privilegios
USER appuser

# Permitir configurar las rutas desde el exterior
ENV INPUT_FILE=/app/data/entrada.csv
ENV OUTPUT_FILE=/app/output/resultado.csv

CMD ["python", "app/procesar.py"]
