# README.md
# Simple FastAPI POST Logging API

## Setup

Ensure you have Python 3.11+ installed.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn main:app --reload
```

API will be available at: [http://localhost:8000](http://localhost:8000)

## Running Tests

```bash
    locust -f locustfiles/endurance_test.py --users 100 --spawn-rate 5 --run-time 2m --host http://localhost:8000 
```

## Example Usage

```bash
curl -X POST "http://localhost:8000/log" -H "Content-Type: application/json" -d '{"message": "Hello, World!"}'
```

## Resources
- https://docs.locust.io/en/stable/what-is-locust.html

