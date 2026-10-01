import os
import serpapi
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SERPAPI_KEY")


def search_agriculture(disease_name, crop_name=None):
    """Search current agricultural information using SerpApi."""

    if not API_KEY:
        return []

    if crop_name:
        query = f"{crop_name} {disease_name} treatment prevention management"
    else:
        query = f"{disease_name} treatment prevention management"

    client = serpapi.Client(api_key=API_KEY)

    results = client.search({
        "engine": "google",
        "q": query,
        "location": "India",
        "hl": "en",
        "gl": "in",
        "num": 8
    })

    sources = []

    for result in results.get("organic_results", []):
        sources.append({
            "title": result.get("title", "Untitled"),
            "link": result.get("link", ""),
            "snippet": result.get("snippet", "")
        })

    return sources
if __name__ == "__main__":
    results = search_agriculture(
        "Early Blight",
        "Tomato"
    )

    for item in results:
        print("\n" + item["title"])
        print(item["link"])
        print(item["snippet"])