from fastapi import FastAPI
from app.routes.auth_routes import auth_routes  # Change import

app = FastAPI()
app.include_router(auth_routes)

@app.get("/")
def health_check():
    return {"status": "Auth service is running"}
