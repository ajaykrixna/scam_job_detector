import requests
from bs4 import BeautifulSoup
import re
import whois
from datetime import datetime

def get_domain_age(url):
    try:
        domain = url.replace("https://", "").replace("http://", "").split("/")[0]

        info = whois.whois(domain)

        creation_date = info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date:
            return (datetime.now(creation_date.tzinfo) - creation_date).days

        return None

    except Exception as e:
        print(e)
        return None

def fetch_job_content(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(separator=" ", strip=True)

    text = re.sub(r"\s+", " ", text)

    return text[:3000]