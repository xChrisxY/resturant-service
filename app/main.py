from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from contextlib import asynccontextmanager
from .config.settings import settings
from .config.database import connect_to_mongo, close_mongo_connection
import logging

from .restaurant.infrastructure.routers.restaurant import router as restaurant_router

logging.basicConfig(format="%(asctime)s | %(name)s | %(levelname)s | %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager 
async def lifespan(app: FastAPI):
    logger.info("Starting Orders Service...")
    await connect_to_mongo()
    logger.info("Connect to mongo")

    yield 
    
    logger.info("Shutting down Restaurant Service...")
    await close_mongo_connection()
    logger.info("Disconnected from MongoDB")
    

app = FastAPI(
    title=settings.app_name,
    description="Microservicio de restaurantes para sistema de pedidos distribuido", 
    version=settings.version, 
    debug=settings.debug, 
    lifespan=lifespan,
    docs_url="/docs", 
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=settings.allowed_origins,
    allow_credentials=True, 
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["*"]
)

@app.get("/health", tags=["health"])
async def health_check():
    return {
        "status" : "healthy",
        "service" : settings.app_name,
        "version" : settings.version
    }

app.include_router(restaurant_router)

if __name__ == "__main__": 
    import uvicorn 
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.debug, log_level="info")