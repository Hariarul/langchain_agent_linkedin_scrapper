import os
from dotenv import load_dotenv
import requests

load_dotenv()

print(os.getenv("SCRAPIN_IO_API_KEY")) 

def scrape_linkedin_profile(linkedin_profile_url: str):
    """Scrape LinkedIn profile"""
    api_endpoint = "https://api.scrapin.io/enrichment/profile"

    headers = {
        "X-Api-Key": os.environ["SCRAPIN_IO_API_KEY"]
    }

    params = {
    "linkedinUrl": linkedin_profile_url
}


    response = requests.get(api_endpoint, headers=headers, params=params, timeout=10)

    json_data = response.json()
  
    data = json_data.get("person")

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/haribaskar-a-a56045301/")
    )
