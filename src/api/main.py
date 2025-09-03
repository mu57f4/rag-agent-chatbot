from fastapi import FastAPI
from routes import base_router
from routes import chat_router
import uvicorn

app = FastAPI()

app.include_router(base_router.base_router)
app.include_router(chat_router.chat_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

