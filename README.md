## Тестовое задание (Python-разработчик AI-ботов)


Задача: Сделать простой сервер, который принимает изображение и отправляет его в бесплатный сервис модерации, чтобы понять — есть ли на нём нежелательный контент.

Что нужно сделать: Написать backend-приложение на Python (лучше FastAPI, можно Flask)

Создать эндпоинт:

- POST /moderate

Принимает изображение (`.jpg`, `.png`)

Отправляет его в https://www.picpurify.com/analyse/1.1

Возвращает результат:

{"status": "OK"} — если безопасно

{"status": "REJECTED", "reason": "NSFW content"} — если найден неприемлемый контент

## Как установить и запустить приложение? ##
1. **Клонирование репозитория**:
    ```sh
    git clone https://github.com/AlexandrBorovkov/image_moderation.git
   ```
    или
    ```sh
    git clone git@github.com:AlexandrBorovkov/image_moderation.git
    ```
2. **Создайте файл .env (смотри образец .env.example)**

    Впишите ключ который дают после регистрации на https://www.picpurify.com/
3. **Установка зависимостей**:
    - Создайте и активируйте виртуальное окружение
    ```sh
    python3.12 -m venv venv
    ```
    ```sh
    source venv/bin/activate
    ```
    - Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```
4. **Запуск приложения**:
    ```sh
    python app/main.py
    ```

## Пример запроса:
```sh
curl -X POST http://localhost:8000/moderate -F "file=@/home/alexandr/Рабочий стол/photo_2025-07-02_21-26-26.jpg"
```




