from fastapi import FastAPI
from pydantic import BaseModel
from scraper import fetch_job_content

app = FastAPI()

class JobRequest(BaseModel):
    url: str = ""
    text: str = ""

@app.get("/")
def home():
    return {"message": "Server Running"}

@app.post("/analyze")
def analyze(data: JobRequest):
    content = fetch_job_content(data.url)

    return {
        "content": content
    }