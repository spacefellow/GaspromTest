from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router


app = FastAPI(
    title='GasProm test',
)

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    router,
    prefix='/test',
)
