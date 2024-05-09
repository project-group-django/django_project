# Stage 1: Build stage
FROM python:3-alpine AS builder

# Встановлення змінних середовища
ENV PYTHONUNBUFFERED 1

# Встановлення робочого каталогу
WORKDIR /app

# Встановлення залежностей за допомогою pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3-alpine AS runner

# Встановлення змінних середовища
ENV PYTHONUNBUFFERED 1

# Встановлення робочого каталогу
WORKDIR /app

# Копіювання віртуального середовища та додатку з попереднього етапу
COPY --from=builder /app/venv /app/venv
COPY . .

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
    