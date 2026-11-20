---
aliases: []
tags: [howtos, devops_dev, "tg/@monitorim_it"]
source: https://t.me/monitorim_it/2671
date: 2026-11-18
---

# Как настроить мониторинг для 500+ узлов: опыт Perc


![Иллюстрация к посту](https://cdn4.telesco.pe/file/VTZmSrr9cwgErJ6BrqAinagSiUbnTJddVjFbMOa3kvRx0ASz0ma0vMifYfpzNOGuI24X1z36_s_TxeS0LhAleq7R26LkW0IBfGckTMnlJSKBZefRCv3RpRfv9voA8wobWAePPoYUE4gXAhRz6_uH1vBb37w69bMXqRWrH6YcbZt50wG2NVkcapHhGtavs73iq3oLasWzEbRtIqRvHHE-zDp68JQdDcQAXc7xfJskS9ZvzEdHYFpA-Y4QR5iayPQ6BpnPqCeW_cyDzGokzE9A-faDewQ1Q98MEH6AzfaaX3Re9cMlLcspix89XZIRzyRXdP_VT_SN3ElIKSdYTJaNrw.jpg)


## Содержание
Как настроить мониторинг для 500+ узлов: опыт Percona В статье разбирают опыт Percona по переработке мониторинга для 500+ узлов. Старый дашборд PMM на базе Grafana перегружал VictoriaMetrics запросами, медленно открывался и заставлял инженеров искать проблемы среди огромного количества панелей. Авторы рассказывают, как превратили его в понятную точку входа для расследования инцидентов: 🚀 сосредоточились на задержках, трафике, ошибках и насыщении 🚀 применили подходы RED и USE 🚀 отделили общую оценку состояния от детальной диагностики 🚀 добавили обнаружение аномалий и переход от проблемного статуса к конкретному узлу 🚀 предусмотрели фильтрацию инфраструктуры по окружениям Читать на Хабре 📱 Telegram | 📲 MAX

---
## Источник
- Канал: [[@monitorim_it]]
- Оригинал: [Читать в Telegram](https://t.me/monitorim_it/2671)

## Связанные заметки (Двунаправленные ссылки)
- [[Superpowers_это_полноценная_методология_разработ | Superpowers — это полноценная методологи...]]
- [[CVE-2026-114938_Java4Shell_RCE_уязвимость_в_декодировщике_Base64 | CVE-2026-114938: Java4Shell - RCE-уязвим...]]
- [[CVE-2026-123007_NGINX2Root_уязвимости_в_nginx_позволяющие_выпол | CVE-2026-123007: NGINX2Root - уязвимости...]]
- [[Vulnerability_Уязвимости_в_Ruby_допускающие_удалённое_выполнени | Vulnerability: Уязвимости в Ruby, допуск...]]
- [[Vulnerability_Релиз_языка_программирования_PHP_86_Семь_критиче | Vulnerability: Релиз языка программирова...]]
