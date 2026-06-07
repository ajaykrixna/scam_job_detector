from fastapi import FastAPI
from pydantic import BaseModel
from scraper import fetch_job_content, get_domain_age
from analyzer import analyze_job
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class JobRequest(BaseModel):
    url: str = ""
    text: str = ""

@app.get("/")
def home():
    return {"message": "Server Running"}

@app.post("/analyze")
def analyze(data: JobRequest):
    if data.url:
        content = fetch_job_content(data.url)
        age = get_domain_age(data.url)
    else:
        content = data.text
        age = None

    result = analyze_job(content, age)
    result["domain_age"] = age

    return result