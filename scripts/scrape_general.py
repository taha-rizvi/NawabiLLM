import requests
from bs4 import BeautifulSoup
import json



# def scrape_intro_or_section(url, section_id=None, max_paragraphs=5):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     if section_id:
#         # --- Case 1: Section scraping ---
#         heading = soup.find(["h2", "h3"], {"id": section_id})

#         if not heading:
#             span = soup.find("span", {"id": section_id})
#             if span:
#                 heading = span.find_parent(["h2", "h3"])

#         if not heading:
#             print(f"❌ Section '{section_id}' not found in page: {url}")
#             return ""

#         next_tag = heading.find_next_sibling()
#         paragraphs = []

#         while next_tag:
#             if next_tag.name in ["h2", "h3"]:
#                 break
#             if next_tag.name == "p":
#                 text = next_tag.get_text(strip=True)
#                 if text:
#                     paragraphs.append(text)
#             next_tag = next_tag.find_next_sibling()

#         return "\n\n".join(paragraphs[:max_paragraphs])

#     else:
#         # --- Case 2: Standalone page, get intro before first <h2> ---
#         content_div = soup.find("div", {"class": "mw-parser-output"})
#         paragraphs = []
#         for tag in content_div.find_all(["p", "h2"], recursive=False):
#             if tag.name == "h2":
#                 break
#             if tag.name == "p":
#                 text = tag.get_text(strip=True)
#                 if text:
#                     paragraphs.append(text)
#         return "\n\n".join(paragraphs[:max_paragraphs])
def scrape_intro_or_section(url, section_id=None, max_paragraphs=5):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # 📌 Case 1: Section scraping (section_id is provided)
    if section_id:
        # Try to find the heading with span id first (most common)
        heading = None
        span = soup.find("span", {"id": section_id})
        if span:
            heading = span.find_parent(["h2", "h3"])
        else:
            # Fallback: directly look for h2/h3 with id
            heading = soup.find(["h2", "h3"], {"id": section_id})

        if not heading:
            print(f"❌ Section '{section_id}' not found in page: {url}")
            return ""

        # Traverse all siblings after heading until next heading
        paragraphs = []
        next_tag = heading.parent
        while True:
            next_tag = next_tag.find_next_sibling()
            # print("👀 Tag after heading:", next_tag)
            if not next_tag:
                break
            if next_tag.name in ["h2", "h3"]:
                break
            if next_tag.name == "p":
                text = next_tag.get_text(strip=True)
                if text:
                    paragraphs.append(text)
            elif next_tag.name in ["div", "ul", "ol"]:
                for p in next_tag.find_all("p", recursive=True):
                    text = p.get_text(strip=True)
                    if text:
                        paragraphs.append(text)

        if not paragraphs:
            print(f"⚠️ No paragraphs found under section '{section_id}'")
        return "\n\n".join(paragraphs[:max_paragraphs])

    # 📌 Case 2: Standalone page, scrape intro before first <h2>
    else:
        content_div = soup.find("div", {"class": "mw-parser-output"})
        paragraphs = []
        for tag in content_div.find_all(["p", "h2"], recursive=False):
            if tag.name == "h2":
                break
            if tag.name == "p":
                text = tag.get_text(strip=True)
                if text:
                    paragraphs.append(text)

        return "\n\n".join(paragraphs[:max_paragraphs])
pages = [
    # Section on a shared page
    {"topic": "culture", "url": "https://en.wikipedia.org/wiki/Lucknow", "section_id": "Culture"},
    {"topic": "architechture", "url": "https://en.wikipedia.org/wiki/Lucknow", "section_id": "Architecture"},
    {"topic": "history", "url": "https://en.wikipedia.org/wiki/Lucknow", "section_id": "History"},
    {"topic": "education", "url": "https://en.wikipedia.org/wiki/Lucknow", "section_id": "Education"},


    # Full article pages
    {"topic": "chikankari", "url": "https://en.wikipedia.org/wiki/Chikankari"},
    {"topic": "tunday_kababi", "url": "https://en.wikipedia.org/wiki/Tunday_Kababi"},
    {"topic": "cuisine","url": "https://en.wikipedia.org/wiki/Awadhi_cuisine"}
]

corpus = []

for page in pages:
    print(f"📥 Scraping: {page['topic']}")
    text = scrape_intro_or_section(
        url=page["url"],
        section_id=page.get("section_id")
    )
    if text:
        corpus.append({
            "topic": page["topic"],
            "source": page["url"],
            "text": text
        })

# Save to JSON
import json
with open("data/raw_general.json", "w", encoding="utf-8") as f:
    json.dump(corpus, f, indent=4, ensure_ascii=False)

print("✅ Done! All entries saved in raw_general.json")