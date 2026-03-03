from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hyperlocal Service Discovery API is running"}
