FROM postgres
FROM python:3.12-alpine AS builder

ENV POSTGRES_PASSWORD=567234
EXPOSE 5432

# Команда запуску сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
