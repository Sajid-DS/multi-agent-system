from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from agents import ResearchAgent
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv

if not os.getenv("GOOGLE_API_KEY"):
    logger.error("GOOGLE_API_KEY not found in environment variables.")
    raise EnvironmentError("GOOGLE_API_KEY not found in environment variables.")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    context: Optional[str] = None

class QueryResponse(BaseModel):
    response: str



@app.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    try:
        research_agent = ResearchAgent()
        result = research_agent.run(request.query)

        logger.info(f"Query processed successfully: {request.query}")

        return QueryResponse(response=result)

    except Exception as e:
        logger.error(f"Error processing query: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)