# Clave — Generador de contraseñas

Aplicación web en español con una interfaz ligera y una API FastAPI para generar contraseñas aleatorias con `secrets` de Python.

## Requisitos

- Python 3.10 o posterior

## Ejecutar en Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Abre <http://127.0.0.1:8000>.

## API

`POST /api/generate`

```json
{
  "length": 20,
  "lowercase": true,
  "uppercase": true,
  "numbers": true,
  "symbols": true
}
```

La longitud permitida es de 4 a 128 caracteres. Se debe seleccionar al menos un grupo; cada grupo seleccionado aparecerá al menos una vez. La respuesta contiene la contraseña en el campo `password`.

## Pruebas

```powershell
python -m unittest discover -s tests
```
