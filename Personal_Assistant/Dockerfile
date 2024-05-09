FROM python:3-alpine AS builder
 
WORKDIR .
 
RUN python3 -m venv venv
ENV VIRTUAL_ENV=/Personal_Assistant/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY requirements.txt .
RUN pip install -r requirements.txt
 
EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

