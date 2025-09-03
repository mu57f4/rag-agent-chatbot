from fastapi import APIRouter
from pydantic import BaseModel
from crew.chatbot import chat_crew
# from ...crew.chatbot import chat_crew


chat_router = APIRouter(
    prefix='/api/v1/crew',
    tags=['api_v1', 'crew']
)

class ChatRequest(BaseModel):
    customer_id: str
    customer_name: str
    customer_question: str

@chat_router.post("/chat")
async def chat_crew_endpoint(chat_request: ChatRequest):
    response = chat_crew(
        chat_request.customer_id,
        chat_request.customer_name,
        chat_request.customer_question
    )
    return {
        "response": response
    }