from fastapi import FastAPI, Request
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


@app.post("/log")
async def log_object(request: Request):
    data = await request.json()
    logger.info(f"Received data: {data}")
    return {"status": "Logged successfully", "data": data}
