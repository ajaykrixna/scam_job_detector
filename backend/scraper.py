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
        print("WHOIS Error:", e)
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

        if response.status_code == 403:
            return {
                "success": False,
                "error": (
                    "Unable to access this job URL because the website blocks "
                    "automated requests. Please paste the complete job description manually."
                )
            }

        elif response.status_code == 404:
            return {
                "success": False,
                "error": "Job page not found."
            }

        elif response.status_code == 429:
            return {
                "success": False,
                "error": (
                    "Too many requests. Please wait a few minutes and try again."
                )
            }

        elif response.status_code != 200:
            return {
                "success": False,
                "error": (
                    f"Unable to access the job page (HTTP {response.status_code}). "
                    "Please paste the job description manually."
                )
            }

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text(separator=" ", strip=True)
        text = re.sub(r"\s+", " ", text)

        if len(text) < 100:
            return {
                "success": False,
                "error": (
                    "Unable to extract a readable job description from this URL. "
                    "The website may require JavaScript or block automated access. "
                    "Please paste the complete job description manually."
                )
            }

        return {
            "success": True,
            "content": text[:3000]
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": (
                "The website took too long to respond. "
                "Please paste the job description manually."
            )
        }

    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": (
                "Unable to connect to the website. "
                "Please check the URL or paste the job description manually."
            )
        }

    except requests.exceptions.InvalidURL:
        return {
            "success": False,
            "error": "Invalid job URL."
        }

    except Exception as e:
        print("Scraping Error:", e)
        return {
            "success": False,
            "error": (
                "Unable to process this job URL. "
                "Please paste the complete job description manually."
            )
        }