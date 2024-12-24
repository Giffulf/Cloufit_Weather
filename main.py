from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routes import router

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_headers=["*"],
                   allow_methods=["*"]
                   )

app.include_router(router)

