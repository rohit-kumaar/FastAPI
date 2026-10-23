from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routers.reviews import router as reviews_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("================ Database tables created ================")
    yield
    # shutdown: clearup here
    print("============== Shutting down the app ==============")

app = FastAPI(
    title="Rangmanch API",
    description="API for theater and event management system",
    lifespan=lifespan
)

app.include_router(reviews_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Rangmanch API",
        "status": "active",
        "version": "1.0.0",
    }
