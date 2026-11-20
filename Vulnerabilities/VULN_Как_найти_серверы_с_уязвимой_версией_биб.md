---
aliases: []
tags: [vulnerabilities, devops_dev, "tg/@admguides"]
source: https://t.me/admguides/3257
date: 2026-11-19
---

# VULN: Как найти серверы с уязвимой версией биб


![Иллюстрация](https://cdn4.telesco.pe/file/J90SXxeDg-o7VMzVvtw7L7pW1kCk237Pf88-8DVdIwDQMlifWExPwa_rvzg8MQoncocJZM_dSIpq9HLIf06RtplyLeAukPZnRHnoSede7oovaD6CCMubKhFbKYvJadFUjhT1NKgK-Km4oXoRYx9hwAb_dthi86tgNdeSKtK620HvBqMbFypR4z9L3B0aOoePI-250Wq0XZjYzfak35PKg3KaKH5vr1txzPQuAFfioxSVctPP0RcHP8fcgDXGZiJLgo6EfZhmdkZBaypdXfxntvob3RpWyRRB2PaMpGZhRyc7T_avQFtg4s_eYLBCk7G-lxEp57-7jZwJcnVv3Aws6w.jpg)


## Содержание
Как найти серверы с уязвимой версией библиотеки Вышел критический CVE, и теперь нужно понять, какие серверы в инфраструктуре под угрозой. Проверять десятки или сотни машин вручную - долго. Здесь помогают инвентаризация пакетов и SBOM. ⏺ Собираем список компонентов SBOM (Software Bill of Materials) - перечень компонентов, из которых состоит приложение или образ. Создать его можно с помощью Syft: syft dir:/opt/myapp -o cyclonedx-json > sbom.json Для установленного ПО на Debian можно получить список пакетов: dpkg-query -W -f=‘&#036;{Package} &#036;{Version}&#092;n’ ⏺ Сопоставляем с уязвимостями Полученный SBOM можно проверить через Grype: grype sbom:sbom.json Инструмент сопоставляет обнаруженные компоненты с базой известных уязвимостей и выводит найденные CVE. ⏺ Распространяем проверку на инфраструктуру С помощью Ansible можно собрать версии пакетов со всех серверов, сохранить результаты и сформировать общую инвентаризацию. Затем сопоставить её с данными об уязвимостях. Важно учитывать: дистрибутивы могут переносить исправления в старые версии пакетов без изменения основного номера версии. Поэтому наличие совпадения по версии ещё не доказывает уязвимость - нужно проверять статус CVE в базе конкретного дистрибутива.

---
## Источник
- Канал: [[@admguides]]
- Оригинал: [Читать в Telegram](https://t.me/admguides/3257)

## Связанные заметки (Двунаправленные ссылки)
- [[Superpowers_это_полноценная_методологи | Superpowers — это полноценная методологи...]]
- [[CVE-2026-114938_Java4Shell_RCE_уязвимость_в_декодировщ | CVE-2026-114938: Java4Shell - RCE-уязвим...]]
- [[CVE-2026-123007_NGINX2Root_уязвимости_в_nginx_позволя | CVE-2026-123007: NGINX2Root - уязвимости...]]
- [[VULN_Уязвимости_в_Ruby_допускающие_удалённое | VULN: Уязвимости в Ruby, допускающие уда...]]
- [[VULN_Релиз_языка_программирования_PHP_86_Се | VULN: Релиз языка программирования PHP 8...]]
