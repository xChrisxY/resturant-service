from pydantic_settings import BaseSettings 

class Settings(BaseSettings): 
    # Application settings
    app_name: str = "Restaurant Service"
    debug: bool = False 
    version: str = "1.0.0"
    
    # Database settings 
    mongo_url: str = "mongodb://localhost:27017"
    database_name: str = "restaurant_db"
    
    # JWT settings 
    secret_key: str = "my-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30 
    
    # CORS settings 
    allowed_origins: list = ["http://localhost:3000", "http://localhost:8080"]
    
    class Config: 
        env_file = ".env"
        
settings = Settings()