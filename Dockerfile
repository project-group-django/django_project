FROM postgres

ENV POSTGRES_PASSWORD=567234
EXPOSE 5432

# Команда запуску сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
