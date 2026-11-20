---
aliases: []
tags: [howto, devops_dev, tg/@hackproglib]
source: https://t.me/hackproglib/5823
date: 2026-11-20
---

# GitHub Actions: id-token: write само по себе не даёт доступ к облачным ресурсам ...

## Описание
GitHub Actions: id-token: write само по себе не даёт доступ к облачным ресурсам Разрешение id-token: write позволяет workflow запросить OIDC JWT у GitHub. Само по себе оно не разрешает менять ресурсы в облаке. Облачный провайдер проверяет claims токена по настроенной trust policy и при успешной проверке выдаёт короткоживущий access token. Настройте условия trust policy так, чтобы access token могли получить только ожидаемые репозитории и workflow. Если используете deployment environment, добавьте правила защиты, ограничивающие ветки и теги, из которых разрешён деплой. При аудите проверяйте отдельно право запросить JWT, соответствие claims политике провайдера и права полученного access token. Руководство GitHub по OIDC для облачных провайдеров Библиотека хакера

## Ссылки
- Источник: [/@hackproglib](https://t.me/hackproglib/5823)
