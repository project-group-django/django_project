FROM python:3-alpine AS builder

WORKDIR /app

# Копіюємо файл відразу
COPY requirements.txt .

# Встановлюємо залежності для компіляції деяких Python-пакетів
RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Створюємо віртуальне середовище та встановлюємо залежності
RUN python -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip && pip install -r requirements.txt

# Використовуємо `EXPOSE`, щоб показати, на якому порту запускатиметься додаток
EXPOSE 8000

# Команда запуску сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
