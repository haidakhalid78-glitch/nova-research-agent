import os
import json
from datetime import datetime

def run_research():
    print("=== NOVA Free AI Video Research Agent ===")
    
    # Structure de rapport de recherche d'outils vidéo IA gratuits
    report_data = {
        "timestamp": datetime.now().isoformat(),
        "status": "active",
        "category": "Free AI Video Tools",
        "findings": [
            {
                "tool_name": "CapCut Web / Desktop",
                "tier": "Free / Freemium",
                "commercial_use": "Restricted on specific free audio assets",
                "best_for": "Auto-captions, TikTok/Shorts editing, AI effects"
            },
            {
                "tool_name": "Clipchamp",
                "tier": "Free (1080p export)",
                "commercial_use": "Allowed with standard assets",
                "best_for": "Text-to-speech, basic video assembly"
            },
            {
                "tool_name": "Runway Gen-2",
                "tier": "Free credits on sign-up",
                "commercial_use": "Check active license terms per generation",
                "best_for": "Text-to-video, Image-to-video generation"
            }
        ]
    }
    
    os.makedirs("reports", exist_ok=True)
    report_path = f"reports/research_latest.json"
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
        
    print(f"✓ Rapport généré avec succès dans {report_path}")

if __name__ == "__main__":
    run_research()
