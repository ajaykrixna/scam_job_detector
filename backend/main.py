from fastapi import FastAPI
from pydantic import BaseModel
from scraper import fetch_job_content, get_domain_age
from analyzer import analyze_job


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
    age = get_domain_age(data.url)

    result = analyze_job(content, age)

    return result