import requests
from bs4 import BeautifulSoup

def fetch_job_content(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    return soup.get_text()