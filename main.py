from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication

app = FastAPI()

# Create all database tables
models.Base.metadata.create_all(engine)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API 🚀. Visit /docs for the Swagger UI."}

# Include routers
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
