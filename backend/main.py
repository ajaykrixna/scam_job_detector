from fastapi import FastAPI
from pydantic import BaseModel
from scraper import fetch_job_content, get_domain_age
from analyzer import analyze_job
from fastapi.middleware.cors import CORSMiddleware
from rules import rule_based_analysis
from extractor import extract_features
from source_verifier import extract_source_info


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "https://scam-job-detector-delta.vercel.app"],
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

    source_info = extract_source_info(
    data.url,
    features
    )

    result = analyze_job(
    content,
    age,
    rule_data,
    features
    )

    score = result["scam_score"]

    if score >= 70:
        result["verdict"] = "Likely Scam"
    elif score >= 40:
        result["verdict"] = "Suspicious"
    else:
        result["verdict"] = "Likely Legitimate"

    result["domain_age"] = age

    result["source_verification"] = source_info


    return result