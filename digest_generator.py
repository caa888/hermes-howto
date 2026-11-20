import json
import urllib.request
import re
from datetime import datetime, timezone, timedelta
from collections import defaultdict

def fetch_channel_posts(username, hours=24):
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
        
        if text and len(text.strip()) > 20:
            posts.append({
                "channel": username,
                "text": text.strip(),
                "link": link,
                "time": dt.isoformat()
            })
            
    return posts

def classify_post(text, default_cat):
    """Classify into requested categories: security, ai, telecom, devops."""
    text_lower = text.lower()
    
    # AI keywords
    ai_kw = ['ии', 'искусственный интеллект', 'нейросет', 'гпт', 'llm', 'модель', 'machine learning', 'gpt']
    # Telecom keywords
    tel_kw = ['телеком', 'оператор', 'связь', '5g', '4g', 'оптоволокно', 'базовая станция', 'telecom']
    # Security keywords
    sec_kw = ['уязвимост', 'эксплуат', 'атака', 'взлом', 'вредоносн', 'малвар', 'фишинг', 'ddos', 'ransomware', 'cve-', 'патч', 'утечк', 'слив', 'кибератак', 'security', 'vulnerab', 'exploit', 'breach', 'leak', 'hack', 'malware']
    # Dev keywords
    dev_kw = ['выпуск', 'релиз', 'обновление', 'версия', 'новый продукт', 'linux', 'kernel', 'docker', 'kubernetes', 'git', 'github', 'опенсорс', 'open source', 'framework', 'библиотека', 'sdk', 'api', 'devops']

    if any(k in text_lower for k in ai_kw):
        return 'ai'
    if any(k in text_lower for k in tel_kw):
        return 'telecom'
    if any(k in text_lower for k in sec_kw):
        return 'security'
    if any(k in text_lower for k in dev_kw):
        return 'devops'
        
    # Map default category from config
    if default_cat in ['infosec', 'security']:
        return 'security'
    if default_cat in ['telecom']:
        return 'telecom'
    if default_cat in ['ai']:
        return 'ai'
    return 'devops'

def similarity_score(text1, text2):
    words1 = set(re.findall(r'\b[а-яёa-z]+\b', text1.lower()))
    words2 = set(re.findall(r'\b[а-яёa-z]+\b', text2.lower()))
    if not words1 or not words2:
        return 0.0
    return len(words1.intersection(words2)) / len(words1.union(words2))

def group_similar_posts(posts, threshold=0.22):
    if not posts:
        return []
    groups = []
    used = [False] * len(posts)
    for i, post in enumerate(posts):
        if used[i]:
            continue
        group = [post]
        used[i] = True
        for j in range(i+1, len(posts)):
            if used[j]:
                continue
            if similarity_score(post['text'], posts[j]['text']) >= threshold:
                group.append(posts[j])
                used[j] = True
        groups.append(group)
    return groups

def format_digest(grouped_by_category):
    lines = []
    lines.append("📰 *Ежедневный IT и ИБ дайджест*")
    lines.append(f"🕐 За период (на 08:00 MSK {datetime.now().strftime('%d.%m.%Y')})")
    lines.append("")
    
    sections = [
        ('security', '🔐 Информационная безопасность (Уязвимости, утечки, инциденты)'),
        ('ai', '🤖 Искусственный интеллект (Технологии, уязвимости, инциденты)'),
        ('telecom', '📡 Телекоммуникации и сети (Технологии, сбои, инциденты)'),
        ('devops', '💻 DevOps и Разработка (Новые продукты, релизы, технологии)')
    ]
    
    for cat_key, cat_title in sections:
        groups = grouped_by_category.get(cat_key, [])
        if not groups:
            continue
            
        lines.append(f"*{cat_title}*")
        lines.append("")
        
        for group in groups:
            # Pick primary post (longest text or first)
            primary = max(group, key=lambda p: len(p['text']))
            sources = sorted(list(set(p['channel'] for p in group)))
            
            text_preview = primary['text']
            if len(text_preview) > 350:
                text_preview = text_preview[:347] + "..."
                
            lines.append(f"• {text_preview}")
            
            # Source confirmation info
            if len(sources) > 1:
                sources_str = ", ".join([f"@{s}" for s in sources])
                lines.append(f"  📌 *Подтверждено в {len(sources)} источниках*: {sources_str}")
            else:
                lines.append(f"  📌 *Источник*: @{sources[0]}")
                
            lines.append(f"  🔗 [Ссылка на публикацию]({primary['link']})")
            lines.append("")
            
    return "\n".join(lines)

def main():
    with open('channels_config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        
    all_posts = []
    for cat, channels in config.items():
        for ch in channels:
            posts = fetch_channel_posts(ch, hours=24)
            for p in posts:
                p['category'] = classify_post(p['text'], cat)
                all_posts.append(p)
                
    by_cat = defaultdict(list)
    for p in all_posts:
        by_cat[p['category']].append(p)
        
    grouped = {}
    for cat, posts in by_cat.items():
        grouped[cat] = group_similar_posts(posts)
        
    digest = format_digest(grouped)
    
    timestamp = datetime.now().strftime('%Y%m%d')
    output_file = f"daily_digest_{timestamp}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(digest)
        
    print(f"Digest successfully generated: {output_file}")
    print(digest[:1500])

if __name__ == '__main__':
    main()
