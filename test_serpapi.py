import os
from dotenv import load_dotenv
import serpapi

load_dotenv()

api_key = os.getenv("SERPAPI_KEY")

if not api_key:
    print("❌ SERPAPI_KEY not found in .env")
    exit()

print("✅ API key loaded")

client = serpapi.Client(api_key=api_key)

results = client.search({
    "engine": "google",
    "q": "tomato early blight treatment",
    "location": "India",
    "hl": "en",
    "gl": "in"
})

print("✅ SerpApi request successful!")

for result in results.get("organic_results", [])[:5]:
    print("\nTitle:", result.get("title"))
    print("Link:", result.get("link"))
    