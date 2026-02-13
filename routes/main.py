# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.agent import agent
from core.config import agent_config

app = FastAPI()


# Request Model
class QueryRequest(BaseModel):
    query: str


# Response Model (optional but recommended)
class QueryResponse(BaseModel):
    response: str


@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    try:
        result = agent.invoke({
            "messages": [{"role": "user", "content": request.query}]  
        },
            config=agent_config)
        
        return {
        "response": result["messages"][-1].content,
        "todos": result.get("todos", [])
    }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))