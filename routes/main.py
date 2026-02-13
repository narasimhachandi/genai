# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.agent import agent

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
        result = agent.invoke(
            {"messages": [("user", request.query)]}
        )

        return {
            "response": result["messages"][-1].content
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))