from fastapi import FastAPI

app = FastAPI(
    title="Production DevOps E-Commerce API",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "message": "E-Commerce API is running",
        "project": "production-devops-ecommerce",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}