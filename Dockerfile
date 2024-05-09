# Етап збирання
FROM python:3.9-slim AS builder

# Встановлення необхідних пакетів
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Створення та активація віртуального середовища
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Копіювання файлив залежностей та встановлення їх
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Додаткові кроки збирання, якщо потрібно

# Етап запуску
FROM python:3.9-slim AS runner

# Копіювання віртуального середовища та додатку з попереднього етапу
COPY --from=builder /app/venv /app/venv
COPY . /app

# Встановлення змінних середовища
ENV PATH="/app/venv/bin:$PATH"

# Встановлення змінних середовища Django
ENV DJANGO_SETTINGS_MODULE=Personal_Assistant.settings

# Встановлення порту
ENV PORT=8000

# Відкриття порту для доступу до додатку
EXPOSE ${PORT}

# Команда для запуску gunicorn сервера
CMD ["gunicorn", "--bind", ":${PORT}", "--workers", "2", "Personal_Assistant.wsgi"]
