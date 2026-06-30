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
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15,
            allow_redirects=True
        )

        if response.status_code != 200:
            print(f"Failed to fetch page: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True)
        text = re.sub(r"\s+", " ", text)

        return text[:3000]

    except Exception as e:
        print("Scraping error:", e)
        return None