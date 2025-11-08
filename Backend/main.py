from fastapi import FastAPI

app = FastAPI(title="AtheletiQ Backend API")

@app.get("/")
def root():
    return {"message": "Welcome to AtheletiQ Backend API 🚀"}
