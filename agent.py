import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_live_ai_video_news():
    print("Fetching real-time AI tools and news...")
    results = []
    
    # Source 1: Hacker News API pour rechercher les mentions d'outils vidéo IA
    try:
        hn_url = "https://hn.algolia.com/api/v1/search?query=ai%20video%20tool&tags=story"
        res = requests.get(hn_url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            for item in data.get("hits", [])[:5]:
                results.append({
                    "source": "HackerNews",
                    "title": item.get("title"),
                    "url": item.get("url") or f"https://news.ycombinator.com/item?id={item.get('objectID')}",
                    "points": item.get("points", 0)
                })
    except Exception as e:
        print(f"Error fetching HN data: {e}")

    # Source 2: Scraping de GitHub Trending (Python/AI)
    try:
        gh_url = "https://github.com/trending/python?since=daily"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(gh_url, headers=headers, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            repos = soup.select("article.Box-row")
            for repo in repos[:5]:
                title = repo.select_one("h2 a").text.strip().replace("\n", "").replace(" ", "")
                desc = repo.select_one("p")
                desc_text = desc.text.strip() if desc else "No description"
                if any(kw in desc_text.lower() or kw in title.lower() for kwk in ["video", "media", "gen", "diffusion", "ai"] for kw in [kwk]):
                    results.append({
                        "source": "GitHub Trending",
                        "title": title,
                        "description": desc_text,
                        "url": f"https://github.com/{title}"
                    })
    except Exception as e:
        print(f"Error scraping GitHub Trending: {e}")

    return results

def run_research():
    print("=== NOVA Live AI Video Research Agent ===")
    live_findings = fetch_live_ai_video_news()
    
    report_data = {
        "timestamp": datetime.now().isoformat(),
        "status": "live_scraped",
        "total_items_found": len(live_findings),
        "findings": live_findings
    }
    
    os.makedirs("reports", exist_ok=True)
    report_path = "reports/research_latest.json"
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
        
    print(f"✓ Rapport réel généré avec succès dans {report_path} ({len(live_findings)} éléments trouvés)")

if __name__ == "__main__":
    run_research()
