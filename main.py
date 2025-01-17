import asyncio

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routes import router
from src.services import write_worker

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_headers=["*"],
                   allow_methods=["*"]
                   )

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(write_worker())
