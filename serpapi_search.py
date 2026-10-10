
import os
from urllib.parse import urlparse

import serpapi
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SERPAPI_KEY")


# =========================================================
# TRUSTED AGRICULTURAL SOURCES
# =========================================================

TRUSTED_DOMAINS = (
    "icar.gov.in",
    "icar.org.in",
    "tnau.ac.in",
    "irri.org",
    "fao.org",
    "gov.in",
    "gov",
    "edu",
    "edu.in",
    "ac.in",
    "extension.org",
)

BLOCKED_DOMAINS = (
    "facebook.com",
    "instagram.com",
    "youtube.com",
    "pinterest.com",
    "twitter.com",
    "x.com",
    "linkedin.com",
    "slideshare.net",
)

AGRICULTURE_TERMS = (
    "agriculture",
    "agricultural",
    "crop",
    "plant",
    "rice",
    "paddy",
    "disease",
    "pest",
    "pathogen",
    "management",
    "prevention",
    "control",
    "symptoms",
    "treatment",
    "horticulture",
    "plant pathology",
    "extension",
    "farmer",
)

HEALTH_TERMS = (
    "human health",
    "blood pressure",
    "cholesterol",
    "diabetes",
    "cancer",
    "osteoporosis",
    "chikungunya",
    "mental health",
    "hospital",
    "patient",
)


# =========================================================
# DISEASE-SPECIFIC RULES
# =========================================================

DISEASE_RULES = {
    "bacterial leaf streak": {
        "aliases": (
            "bacterial leaf streak",
            "bacterial leaf-streak",
            "xanthomonas oryzae pv. oryzicola",
            "oryzicola",
        ),
        "exclude_if_only": (
            "bacterial leaf blight",
            "xanthomonas oryzae pv. oryzae",
            "blb",
        ),
    },

    "bacterial leaf blight": {
        "aliases": (
            "bacterial leaf blight",
            "xanthomonas oryzae pv. oryzae",
        ),
        "exclude_if_only": (
            "bacterial leaf streak",
            "xanthomonas oryzae pv. oryzicola",
        ),
    },
}


# =========================================================
# HELPERS
# =========================================================

def normalize(text):
    return " ".join(
        str(text or "")
        .lower()
        .replace("_", " ")
        .replace("-", " ")
        .split()
    )


def get_domain(url):
    try:
        return (
            urlparse(url).hostname or ""
        ).lower().rstrip(".")
    except (ValueError, TypeError):
        return ""


def is_normal_condition(condition):
    return normalize(condition) in {
        "normal",
        "healthy",
        "health",
    }


def is_blocked_domain(domain):
    return any(
        domain == blocked
        or domain.endswith("." + blocked)
        for blocked in BLOCKED_DOMAINS
    )


def is_trusted_domain(domain):
    for suffix in TRUSTED_DOMAINS:
        if domain == suffix or domain.endswith("." + suffix):
            return True
    return False


# =========================================================
# DISEASE RELEVANCE FILTER
# =========================================================

def disease_relevance(title, snippet, crop, disease):
    """
    Reject search results whose titles identify a different
    disease. Require explicit target-disease terminology.
    """

    title_text = normalize(title)
    content = normalize(f"{title} {snippet}")
    disease_text = normalize(disease)

    rules = DISEASE_RULES.get(disease_text)

    if rules:
        aliases = [
            normalize(alias)
            for alias in rules["aliases"]
        ]

        wrong_names = [
            normalize(name)
            for name in rules["exclude_if_only"]
        ]

        title_has_target = any(
            alias in title_text
            for alias in aliases
        )

        title_has_wrong = any(
            name in title_text
            for name in wrong_names
        )

        # Do not accept a result titled as another disease,
        # even if its snippet mentions the target disease.
        if title_has_wrong and not title_has_target:
            return False, "Title identifies a different disease"

        content_has_target = any(
            alias in content
            for alias in aliases
        )

        if not content_has_target:
            return False, "Exact disease not established"

        return True, "Target disease identified"

    # Generic matching for other supported disease classes.
    if disease_text not in content:
        words = [
            word for word in disease_text.split()
            if len(word) >= 3
        ]

        if not words or not all(
            word in content for word in words
        ):
            return False, "Disease mismatch"

    return True, "Disease match"


# =========================================================
# SCORE SEARCH RESULTS
# =========================================================

def score_result(result, crop_name, disease_name):
    title = result.get("title", "")
    snippet = result.get("snippet", "")
    link = result.get("link", "")
    domain = get_domain(link)

    if not link or not domain:
        return -100

    if is_blocked_domain(domain):
        return -100

    relevant, reason = disease_relevance(
        title,
        snippet,
        crop_name,
        disease_name,
    )

    if not relevant:
        print(f"REJECTED: {title} — {reason}")
        return -100

    text = normalize(f"{title} {snippet} {domain}")
    score = 10

    if is_trusted_domain(domain):
        score += 8

    crop = normalize(crop_name)
    if crop and crop in text:
        score += 5

    score += min(
        sum(
            1 for term in AGRICULTURE_TERMS
            if term in text
        ) * 2,
        10,
    )

    if any(term in text for term in HEALTH_TERMS):
        score -= 8

    if any(
        term in text
        for term in (
            "management",
            "control",
            "prevention",
            "treatment",
        )
    ):
        score += 2

    return score


# =========================================================
# AGRICULTURAL SEARCH
# =========================================================

def search_agriculture(disease_name, crop_name=None):
    """
    Search agricultural sources through SerpApi.
    Returns relevant sources or [] if none qualify.
    """

    if not API_KEY:
        print("SERPAPI_KEY is not configured.")
        return []

    if is_normal_condition(disease_name):
        print("Healthy/normal condition: skipping search.")
        return []

    disease_text = normalize(disease_name)
    rules = DISEASE_RULES.get(disease_text)

    clean_disease = str(disease_name or "").replace("_", " ").strip()
    if rules:
        exact_name = rules["aliases"][0]
        identity = f'"{exact_name}"'
    else:
        identity = f'"{clean_disease}"'

    clean_crop = str(crop_name or "").replace("_", " ").strip()
    query = (
        f"{clean_crop} {identity} "
        "plant disease management control India"
    ).strip()

    print(f"\nAgricultural search query: {query}")

    try:
        client = serpapi.Client(api_key=API_KEY)

        response = client.search({
            "engine": "google",
            "q": query,
            "location": "India",
            "hl": "en",
            "gl": "in",
            "num": 10,
        })

    except Exception as exc:
        print(f"SerpApi request failed: {exc}")
        return []

    organic_results = response.get(
        "organic_results",
        [],
    )

    # -----------------------------------------------------
    # DEBUG: RAW RESULTS
    # -----------------------------------------------------

    print("\n--- RAW SERPAPI RESULTS ---")

    for result in organic_results:
        print("TITLE:", result.get("title", ""))
        print("LINK:", result.get("link", ""))
        print("SNIPPET:", result.get("snippet", ""))
        print("---")

    # -----------------------------------------------------
    # FILTER AND SCORE
    # -----------------------------------------------------

    scored_results = []

    print("\n--- FILTERED RESULTS ---")

    for result in organic_results:
        score = score_result(
            result,
            clean_crop,
            clean_disease,
        )

        print(
            f"SCORE: {score} | "
            f"{result.get('title', 'Untitled')}"
        )

        if score < 10:
            print("STATUS: REJECTED")
            continue

        print("STATUS: ACCEPTED")

        link = result.get("link", "")
        domain = get_domain(link)
        trust_badge = "Agricultural Reference"
        if any(term in domain for term in ("icar.gov.in", "tnau.ac.in", "irri.org", "fao.org", "gov.in")):
            trust_badge = "Official Research / University"
        elif any(domain.endswith(t) for t in ("edu", "ac.in", "gov", "org")):
            trust_badge = "Academic / Extension"

        scored_results.append({
            "score": score,
            "title": result.get("title", "Untitled"),
            "link": link,
            "snippet": result.get("snippet", ""),
            "domain": domain,
            "trust_badge": trust_badge
        })

    # -----------------------------------------------------
    # SORT, DEDUPLICATE AND RETURN
    # -----------------------------------------------------

    scored_results.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    sources = []
    seen_urls = set()

    for item in scored_results:
        url = item["link"].split("#")[0]

        if url in seen_urls:
            continue

        seen_urls.add(url)

        sources.append({
            "title": item["title"],
            "link": item["link"],
            "snippet": item["snippet"],
            "domain": item.get("domain", get_domain(item["link"])),
            "trust_badge": item.get("trust_badge", "Agricultural Reference")
        })

        if len(sources) >= 5:
            break

    print(
        f"\nRelevant sources returned: {len(sources)}"
    )

    if not sources:
        print("No matching agricultural sources found.")

    return sources


# =========================================================
# ADVANCED AGRICULTURAL INTELLIGENCE SEARCH
# =========================================================

def search_agricultural_intelligence(crop_name=None, disease_name=None, query=None, category=None):
    """
    Search agricultural intelligence via SerpApi with category filters.
    Categories supported: 'all', 'symptoms', 'prevention', 'management', 'extension'.
    """
    if not API_KEY:
        return {
            "success": False,
            "sources": [],
            "message": "SERPAPI_KEY is not configured in environment variables."
        }

    clean_crop = str(crop_name or "").replace("_", " ").strip()
    clean_disease = str(disease_name or "").replace("_", " ").strip()

    # Build query based on category
    cat = (category or "all").lower().strip()
    if query and query.strip():
        # Custom user query sanitized
        clean_q = " ".join(query.strip().split()[:20]) # Limit length
        search_q = f"{clean_q} agriculture India"
    elif clean_disease and not is_normal_condition(clean_disease):
        if cat == "symptoms":
            search_q = f'{clean_crop} "{clean_disease}" visible symptoms identification leaf damage'
        elif cat == "prevention":
            search_q = f'{clean_crop} "{clean_disease}" prevention cultural practices resistant varieties crop rotation'
        elif cat == "extension":
            search_q = f'{clean_crop} "{clean_disease}" ICAR TNAU IRRI KVK university advisory management'
        elif cat == "management":
            search_q = f'{clean_crop} "{clean_disease}" integrated pest management control biological measures'
        else:
            search_q = f'{clean_crop} "{clean_disease}" plant disease management control India'
    elif clean_crop:
        search_q = f'{clean_crop} crop care disease management ICAR agricultural advisory'
    else:
        search_q = 'crop disease detection and integrated pest management ICAR India'

    print(f"\nAdvanced agricultural intelligence query: {search_q}")

    try:
        client = serpapi.Client(api_key=API_KEY)
        response = client.search({
            "engine": "google",
            "q": search_q,
            "location": "India",
            "hl": "en",
            "gl": "in",
            "num": 10,
        })
    except Exception as exc:
        print(f"SerpApi request failed: {exc}")
        return {
            "success": False,
            "sources": [],
            "message": f"Agricultural search service error: {str(exc)}"
        }

    organic_results = response.get("organic_results", [])
    sources = []
    seen_urls = set()

    for result in organic_results:
        link = result.get("link", "")
        domain = get_domain(link)
        if not link or not domain or is_blocked_domain(domain):
            continue

        url = link.split("#")[0]
        if url in seen_urls:
            continue
        seen_urls.add(url)

        trust_badge = "Agricultural Reference"
        if any(term in domain for term in ("icar.gov.in", "tnau.ac.in", "irri.org", "fao.org", "gov.in")):
            trust_badge = "Official Research / University"
        elif any(domain.endswith(t) for t in ("edu", "ac.in", "gov", "org")):
            trust_badge = "Academic / Extension"

        sources.append({
            "title": result.get("title", "Untitled"),
            "link": link,
            "snippet": result.get("snippet", ""),
            "domain": domain,
            "trust_badge": trust_badge
        })

        if len(sources) >= 6:
            break

    return {
        "success": True,
        "sources": sources,
        "query_used": search_q,
        "count": len(sources),
        "message": "Sources retrieved successfully." if sources else "No matching agricultural resources found."
    }


# =========================================================
# DIRECT TEST
# =========================================================

if __name__ == "__main__":
    results = search_agriculture(
        "bacterial leaf streak",
        "Paddy",
    )

    print("\n--- FINAL SOURCES ---")

    if not results:
        print("No relevant sources found.")

    for source in results:
        print("\nTitle:", source["title"])
        print("Link:", source["link"])
        print("Snippet:", source["snippet"])
