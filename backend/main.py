from fastapi import FastAPI
from pydantic import BaseModel
from scraper import fetch_job_content, get_domain_age
from analyzer import analyze_job
from fastapi.middleware.cors import CORSMiddleware
from rules import rule_based_analysis
from extractor import extract_features
from validator import validate_company_domain


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

    rule_data = rule_based_analysis(content, age)

    features = extract_features(content)
    validation = validate_company_domain(
    content,
    data.url
    )

    print(validation)
    print(features)

    result = analyze_job(
    content,
    age,
    rule_data,
    features,
    validation
    )
    result["domain_age"] = age

    return result