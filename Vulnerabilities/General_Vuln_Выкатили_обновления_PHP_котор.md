---
cve: []
tags: [vulnerability, security, devops_dev]
source: https://t.me/tech_b0lt_Genona/7414
date: 2026-11-20
---

# Уязвимость: General Vuln

## Детали
Выкатили обновления PHP, которые просили ставить из-за Critical https://t.me/tech_b0lt_Genona/7400 PHP 8.2.36 https://www.php.net/archive/2026.php#2026-11-19-1 PHP 8.3.37 https://www.php.net/archive/2026.php#2026-11-19-2 PHP 8.4.28 https://www.php.net/archive/2026.php#2026-11-19-3 PHP 8.5.13 https://www.php.net/archive/2026.php#2026-11-19-4 PHP 8.6.0 https://www.php.net/archive/2026.php#2026-11-19-5 Там много интересного и [не]весёлого пофиксили Большой пост на Опёнке Релиз языка программирования PHP 8.6. Устранено семь критических уязвимостей в PHP https://www.opennet.ru/opennews/art.shtml?num=66723 Широко известный в узких кругах Mattias Geniar сделал страницу с патч-статусом PHP security release of 19 November 2026: patch status https://ma.ttias.be/php-security-release-2026-11-19/ Он же наковырял (подсветил) прикольное. Так называемый case sensiteve TLS который жил в пыхе 20 лет 🌝 Oh boy … PHP sent clear text data when you used uppercased S in httpS:// in a protocol handler 🙈 🙈 file_get_contents('HTTPS://…') skipped TLS: tokens, POST bodies and FTPS logins went out unencrypted&#33; https://x.com/mattiasgeniar/status/2123436542995964123 Fair, but it's not just file_get_contents. Anything on PHP's stream wrappers leaked: getimagesize, exif_read_data, simplexml_load_file, DOMDocument::load, md5_file, SOAP WSDLs, even file_exists() on FTPS://. Guzzle, Symfony HttpClient and curl were fine. https://x.com/mattiasgeniar/status/2123448368865390967

## Ссылки
- Источник: [/@tech_b0lt_Genona](https://t.me/tech_b0lt_Genona/7414)
