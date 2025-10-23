# Generic API

A simple and generic FastAPI application that provides basic API functionality.

## Features

- Health check endpoint
- Welcome message endpoint
- Personalized greeting endpoint
- API information endpoint
- Structured project layout following best practices

## Project Structure

```
my-app-on-cloud/
├── src/                    # Source code
│   ├── api/                # API layer
│   │   ├── routes/         # API route definitions
│   │   └── schemas/        # Pydantic models for request/response
│   ├── config/             # Configuration
│   └── core/               # Core application code
├── .env.example            # Example environment variables
└── pyproject.toml          # Project dependencies
```

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -e .
```

3. Create a `.env` file (you can copy from `.env.example`)

## Running the API

```bash
python -m src.main
```

Or with uvicorn directly:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint
- `GET /hello/{name}` - Personalized greeting endpoint
- `GET /info` - API information endpoint

## Documentation

- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Development

For development dependencies:

```bash
pip install -e ".[dev]"
```
