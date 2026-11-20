---
aliases: []
tags: [howtos, devops_dev, "tg/@it_fullstak"]
source: https://t.me/it_fullstak/3733
date: 2026-11-19
---

# 🪟 Усиливаем встроенную защиту Windows Ha


![Иллюстрация](https://cdn4.telesco.pe/file/vd3uhwdFc9ksARpzIbZ5PrJo0qbidtan6LW8c5_k8vSpz1u80Mc2dSK5dNpDVbX2_DM5rCzpNDBr4HoK7Hfzm57S-98wnEhdxAbQEtL8ZuBxbtiWVjhQuTpDJxbxOcPmN7wrTLN7mEfTcFO5RgbaD980HYFc0G6w_DSN5G7eC3RSUCNsNwgmLjPMLNEdThezrDYN1XrYOTCOuUat1oYCt8O71jJZyMK9RblD1B_WpIl9_7wXUl_6t_sVGlsgoGvUUY3AvvNrnb7UHoWCAieu3TnWbbsge15FkfoJyHpP42lQeswXG0We6s90XNFHdwdixHjr4EOwW27coQJUSs2v3Q.jpg)


## Содержание
🪟 Усиливаем встроенную защиту Windows Harden Windows Security — это набор PowerShell-скриптов и политик, которые помогают жёстко (но адекватно) харденить Windows — то есть усиливать её защиту на всех уровнях : от базовых настроек Defender до отключения Windows Script Host и защиты от ransomware — Он автоматически активирует и тонко настраивает встроенные механизмы безопасности, которые по умолчанию иногда работают не в полную силу или даже отключены Некоторые из них: Настраивает Microsoft Defender : включает защиту в реальном времени, блокирует потенциально нежелательные программы (PUA), активирует облачную защиту и расширенные эвристики; Активирует Attack Surface Reduction (ASR) : правила ASR помогают защититься от опасных сценариев: например, от внедрения скриптов или запуска подозрительных процессов; Усиливает Exploit Protection : защищает от техник эксплуатации вроде переполнения буфера или ROP-атак; Включает другие защитные механизмы : Defender Application Guard, Smart App Control (если доступно), Credential Guard, изоляцию ядра (Core Isolation), Control Flow Guard и другие; Отключает или блокирует устаревшие или уязвимые компоненты : например, отключает протокол SMBv1, запрещает Windows Script Host (WSH), может скрывать системные инструменты вроде regedit или cmd; Настраивает другие параметры : групповые политики, настройки BitLocker, параметры TLS, UAC и другие • Репозиторий на GitHub • Harden-Windows-Security: превратите Windows в параноика… но в хорошем смысле • Harden Windows Security — Полное руководство по защите Windows • Бронируем Windows. Комплексный аудит безопасности — от файрвола до Active Directory (по подписке) #Tools #Windows #PowerShell #Ransomware 🥷 INSPECTOR

---
## Источник
- Канал: [[@it_fullstak]]
- Оригинал: [Читать в Telegram](https://t.me/it_fullstak/3733)

## Связанные заметки (Двунаправленные ссылки)
- [[Superpowers_это_полноценная_методологи | Superpowers — это полноценная методологи...]]
- [[CVE-2026-114938_Java4Shell_RCE_уязвимость_в_декодировщ | CVE-2026-114938: Java4Shell - RCE-уязвим...]]
- [[CVE-2026-123007_NGINX2Root_уязвимости_в_nginx_позволя | CVE-2026-123007: NGINX2Root - уязвимости...]]
- [[VULN_Уязвимости_в_Ruby_допускающие_удалённое | VULN: Уязвимости в Ruby, допускающие уда...]]
- [[VULN_Релиз_языка_программирования_PHP_86_Се | VULN: Релиз языка программирования PHP 8...]]
