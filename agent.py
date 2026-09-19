import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_live_ai_video_news():
    print("Fetching real-time AI tools and news...")
    results = []
    
    # Source 1: Hacker News API
    try:
        hn_url = "https://hn.algolia.com/api/v1/search?query=ai%20video%20tool&tags=story"
        res = requests.get(hn_url, timeout=10)
        if res.status_code == 200:
            data = res.json()
            for item in data.get("hits", [])[:3]:
                results.append({
                    "source": "HackerNews",
                    "title": item.get("title"),
                    "url": item.get("url") or f"https://news.ycombinator.com/item?id={item.get('objectID')}"
                })
    except Exception as e:
        print(f"Error fetching HN data: {e}")

    # Source 2: GitHub Trending
    try:
        gh_url = "https://github.com/trending/python?since=daily"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(gh_url, headers=headers, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")
            repos = soup.select("article.Box-row")
            for repo in repos[:3]:
                title = repo.select_one("h2 a").text.strip().replace("\n", "").replace(" ", "")
                desc = repo.select_one("p")
                desc_text = desc.text.strip() if desc else "No description"
                results.append({
                    "source": "GitHub Trending",
                    "title": title,
                    "description": desc_text,
                    "url": f"https://github.com/{title}"
                })
    except Exception as e:
        print(f"Error scraping GitHub Trending: {e}")

    return results

def generate_tiktok_script(findings):
    if not findings:
        top_item = "les derniers outils d'IA vidéo gratuits"
    else:
        top_item = findings[0].get("title", "un nouvel outil IA vidéo")

    script_md = f"""# Script Vidéo Court (TikTok / Shorts / Reels)
**Date :** {datetime.now().strftime('%Y-%m-%d')}
**Sujet :** {top_item}

---

### 🟢 Accroche (0-3s)
"Arrête de payer pour tes montages vidéo. Cet outil IA gratuit vient tout changer."

### 🔵 Corps (3-30s)
"Si tu créers du contenu, tu dois absolument tester **{top_item}**. 
Il te permet d'automatiser ta recherche et de repérer les meilleures pépites IA du moment sans débourser un seul centime.
Plus besoin de passer des heures à chercher sur Google ou ProductHunt."

### 🔴 Appel à l'action / CTA (30-45s)
"Enregistre cette vidéo pour ne pas l'oublier, et abonne-toi pour découvrir l'outil de demain !"
"""
    return script_md

def run_research():
    print("=== NOVA Live AI Video & Script Agent ===")
    live_findings = fetch_live_ai_video_news()
    
    # 1. Sauvegarde du rapport JSON
    report_data = {
        "timestamp": datetime.now().isoformat(),
        "status": "live_scraped",
        "total_items_found": len(live_findings),
        "findings": live_findings
    }
    
    os.makedirs("reports", exist_ok=True)
    with open("reports/research_latest.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
        
    # 2. Génération automatique du script TikTok
    script_content = generate_tiktok_script(live_findings)
    os.makedirs("scripts", exist_ok=True)
    with open("scripts/latest_video_script.md", "w", encoding="utf-8") as f:
        f.write(script_content)
        
    print("✓ Rapport JSON et Script TikTok générés avec succès !")

if __name__ == "__main__":
    run_research()
