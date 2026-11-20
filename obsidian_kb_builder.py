import json
import urllib.request
import re
from datetime import datetime, timezone, timedelta
import os

def fetch_channel_posts(username, hours=48):
    """Fetch posts from a Telegram channel preview for the last N hours."""
    url = f"https://t.me/s/{username}"
    req = urllib.request.Request(
        url, 
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html_content = resp.read().decode('utf-8')
    except Exception as e:
        return []

    posts = []
    now = datetime.now(timezone.utc)
    
    parts = html_content.split('class="tgme_widget_message ')
    for part in parts[1:]:
        dt_match = re.search(r'datetime="([^"]+)"', part)
        if not dt_match:
            continue
        dt_str = dt_match.group(1)
        try:
            dt = datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
        except Exception:
            continue
            
        if (now - dt) > timedelta(hours=hours):
            continue
            
        text_match = re.search(r'class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', part, re.DOTALL)
        text = ""
        if text_match:
            raw_text = text_match.group(1)
            text = re.sub(r'<[^>]+>', ' ', raw_text)
            text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
            text = text.replace('&quot;', '"').replace('&#39;', "'")
            text = ' '.join(text.split())
            
        link_match = re.search(r'class="tgme_widget_message_date"[^>]*href="([^"]+)"', part)
        link = link_match.group(1) if link_match else f"https://t.me/{username}"
        
        if text and len(text.strip()) > 30:
            posts.append({
                "channel": username,
                "text": text.strip(),
                "link": link,
                "time": dt.isoformat()
            })
            
    return posts

def analyze_kb_content(text):
    """Determine if a post is a HowTo or Vulnerability and extract metadata."""
    text_lower = text.lower()
    
    howto_kw = ['инструкция', 'как настроить', 'руководство', 'гайд', 'howto', 'настройка', 'конфигурация', 'туториал', 'шпаргалка', 'cookbook']
    vuln_kw = ['cve-', 'уязвимост', 'эксплойт', 'взлом', 'zero-day', '0-day', 'утечк', 'cwe-', 'бду']
    
    is_howto = any(k in text_lower for k in howto_kw)
    is_vuln = any(k in text_lower for k in vuln_kw)
    
    # Extract CVEs if present
    cves = re.findall(r'cve-\d{4}-\d{4,7}', text_lower)
    
    return {
        "is_howto": is_howto,
        "is_vuln": is_vuln,
        "cves": list(set(cves))
    }

def sanitize_filename(title):
    """Create a safe filename from title or text snippet."""
    clean = re.sub(r'[^\w\s-]', '', title).strip()
    return re.sub(r'[-\s]+', '_', clean)[:50]

def generate_obsidian_vault(vault_path="Obsidian_IT_KB"):
    os.makedirs(os.path.join(vault_path, "HowTos"), exist_ok=True)
    os.makedirs(os.path.join(vault_path, "Vulnerabilities"), exist_ok=True)
    
    with open('channels_config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        
    print("Scanning channels for KB content (HowTos & Vulnerabilities)...")
    count_howto = 0
    count_vuln = 0
    
    for cat, channels in config.items():
        for ch in channels:
            posts = fetch_channel_posts(ch, hours=72) # last 3 days for KB
            for p in posts:
                analysis = analyze_kb_content(p['text'])
                
                if analysis['is_howto']:
                    count_howto += 1
                    title = p['text'][:40].strip()
                    fname = sanitize_filename(title) or f"howto_{count_howto}"
                    filepath = os.path.join(vault_path, "HowTos", f"{fname}.md")
                    
                    frontmatter = f"""---
aliases: []
tags: [howto, {cat}, tg/@{p['channel']}]
source: {p['link']}
date: {p['time'][:10]}
---

# {p['text'][:80]}...

## Описание
{p['text']}

## Ссылки
- Источник: [/@{p['channel']}]({p['link']})
"""
                    with open(filepath, 'w', encoding='utf-8') as f_out:
                        f_out.write(frontmatter)
                        
                if analysis['is_vuln']:
                    count_vuln += 1
                    cve_str = ", ".join(analysis['cves']).upper() if analysis['cves'] else "General Vuln"
                    title = f"{cve_str} - {p['text'][:30]}"
                    fname = sanitize_filename(title) or f"vuln_{count_vuln}"
                    filepath = os.path.join(vault_path, "Vulnerabilities", f"{fname}.md")
                    
                    frontmatter = f"""---
cve: {analysis['cves']}
tags: [vulnerability, security, {cat}]
source: {p['link']}
date: {p['time'][:10]}
---

# Уязвимость: {cve_str}

## Детали
{p['text']}

## Ссылки
- Источник: [/@{p['channel']}]({p['link']})
"""
                    with open(filepath, 'w', encoding='utf-8') as f_out:
                        f_out.write(frontmatter)
                        
    print(f"Obsidian KB generated successfully at '{vault_path}/'")
    print(f"Created {count_howto} HowTo notes and {count_vuln} Vulnerability notes.")

if __name__ == '__main__':
    generate_obsidian_vault()
