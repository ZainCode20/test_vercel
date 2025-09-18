from fastapi import FastAPI
from mangum import Mangum

# Minimal FastAPI app
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Zain's RAG Bot!", "status": "working"}

@app.get("/test")
def test():
    return {"test": "successful", "vercel": "working"}

# Handler for Vercel
handler = Mangum(app)
