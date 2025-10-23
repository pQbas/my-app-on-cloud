FROM python:3.11-slim

WORKDIR /app

# Copiar archivos de configuración y dependencias
COPY pyproject.toml .
COPY README.md .

# Instalar dependencias
RUN pip install --no-cache-dir -e .

# Copiar el código fuente
COPY src/ ./src/

# Puerto en el que se ejecutará la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
