# Використовуємо базовий образ PostgreSQL
FROM postgres AS postgresql

# Встановлюємо пароль для користувача postgres
ENV POSTGRES_PASSWORD=567234

# Вказуємо порт, на якому PostgreSQL буде слухати підключення
EXPOSE 5432

# ---------------------

# Використовуємо базовий образ Python для створення віртуального середовища та іншого
FROM python:3.12-alpine AS builder

# Копіюємо файли додатку
COPY . /app

# Встановлюємо залежності
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Запускаємо додаток
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
