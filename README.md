# Проект: Диалоговый чат-бот на базе ruDialoGPT

## Описание
Этот проект включает в себя чат-бота для Telegram, обученного на базе модели ruDialoGPT, а также шаги для дополнительного обучения этой модели на собственных данных.

## Структура проекта
- `model_service/`: Содержит сервис для загрузки и выполнения предсказаний модели.
- `telegram_bot_service/`: Содержит код для Telegram бота.
- `output/`: Содержит обученную модель (в репозитории его нет), так же обратите внимание, что в docker-compose.yml прокинута папка `output/` в контейнер как `model/output/`, 
если хотите использовать другую директорию - надо поменять название папки в docker-compose.yml и в .env файле в папке `model_service/`.

## Подготовка

1. Добавьте ваш токен Telegram в `.env` файл в папке `telegram_bot_service/`.
2. Добавьте путь к вашей модели в `.env` файл в папке `model_service/`.
3. docker-compose up --build -d



## Дообучение модели

### Шаги дообучения

1. **Подготовка данных**: Убедитесь, что ваш csv-файл (`data.csv`) имеет структуру с колонками `context_1`, `context_2`, `context_3` и `response`.

2. **Обработка данных**: Скрипт собирает все строки из файла `data.csv` и сохраняет их в текстовом файле (`text_data.txt`).

3. **Токенизация**: Используется токенизатор из библиотеки transformers для конвертации текста в токены.

4. **Специальные токены**: Добавляются специальные токены, такие как `<bos>`, `<eos>` для начала и конца последовательности.

5. **Фильтрация токенов**: Токены, которых нет в словаре токенизатора, заменяются на токен `<unk>`.

6. **Создание датасета**: Используется `TextDataset` для подготовки данных для обучения.

7. **Data Collator**: Используется `DataCollatorForLanguageModeling` для подготовки батчей данных.

8. **Настройка аргументов для обучения**: Задаются аргументы для обучения, такие как количество эпох, размер батча и т.д.

9. **Обучение**: Запускается процесс обучения с помощью `Trainer`.

10. **Сохранение модели**: После обучения модель сохраняется в папке `output/`.

## Запуск сервисов

1. **Сборка Docker образов**: Запустите `docker-compose build`.

2. **Запуск контейнеров**: Запустите `docker-compose up`.

3. **Проверка**: Откройте Telegram и начните диалог с вашим ботом.

4. **Логи**: Проверьте логи в терминале для дебага или мониторинга.

Это всё! Теперь у вас должен быть работающий чат-бот на базе ruDialoGPT с возможностью дополнительного обучения.