---
aliases: []
tags: [howtos, infosec, "tg/@info_cybersecurity"]
source: https://t.me/info_cybersecurity/1860
date: 2026-11-18
---

# 🤖 Безопасность LLM-агентов и генеративны


![Иллюстрация](https://cdn4.telesco.pe/file/HuJ1T3AgVAq3RlXNruM_9TDOU82U2Do8cvXMgGLxzdJoT8vKW8k1IXZvwccKu7RyCEEnZKCtCLNpkqdEacwwFAC6OrGqjnGt-dZLK8ngRsy9LuoMJw6JzHvLw-ADf6OV475dSN6baNNuLR5_MTFGDr9mxmi119wISDQoh2g2xy_mnmaDlgNpfPnu5K5RFXo_ySRHvuf3IeZNYl2mPzRLWmzUSVrb44VmdMQOm4vmSTGNpLcyPnk8ZwloEKAvi2F8B-QRlRWIzFIrq1shRzQ3sf6kfEWLku54-wYV3DfnyvIrNvF0-qcqIWCkrQI6oJg6Hox7BMHmtriYTfeJsTxXvw.jpg)


## Содержание
🤖 Безопасность LLM-агентов и генеративных продуктов: угрозы и методы защиты Главный контекст, который необходимо понимать при построении архитектуры любого генеративного продукта с использованием LLM — это то, что модель не различает данные и инструкции Поэтому очень важно внедрять механизмы разграничения, чтобы система четко понимала, где находится пользовательская инструкция, а где — преднамеренное действие разработчика — В этой статье рассмотрим сценарии атак, охватывающие категории от LLM01 до LLM09 по методологии OWASP Top 10 for LLM Applications, и расскажем, как от них защититься Содержание статьи: 🔵 Сценарий 1. Косвенная инъекция промпта, или Indirect Prompt Injection, и злоупотребление тулами 🔵 Сценарий 2. XSS через LLM и внутренние заметки 🔵 Сценарий 3. Утечка системного промпта, или System Prompt Leakage 🔵 Сценарий 4. Отравление базы знаний, или RAG Poisoning 🔵 Методы защиты 🔵 Правила безопасности&nbsp; ⛓️ https://habr.com/ru/companies/avito/articles/1108426/ #AI #OWASP #LLM #BlueTeam ✈️ inf0

---
## Источник
- Канал: [[@info_cybersecurity]]
- Оригинал: [Читать в Telegram](https://t.me/info_cybersecurity/1860)

## Связанные заметки (Двунаправленные ссылки)
- [[VULN_Обновление_БДУ_Обновлены_сведения_об_уяз | VULN: Обновление БДУ Обновлены сведения ...]]
- [[CVE-2026-116331_Уязвимость_функций_min_и_max_системы | CVE-2026-116331: Уязвимость функций min(...]]
- [[CVE-2026-114938_Уязвимость_компонента_Compiler_программн | CVE-2026-114938: Уязвимость компонента C...]]
- [[VULN_Уязвимость_платформы_для_работы_с_кодом | VULN: Уязвимость платформы для работы с ...]]
- [[VULN_Обновление_БДУ_Обновлены_сведения_об_уяз | VULN: Обновление БДУ Обновлены сведения ...]]
