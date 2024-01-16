FROM python:3.10-alpine
# pull official base image

# set work directory

WORKDIR /app

# set environment variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install psycopg2 dependencies 
RUN apk update && apk add postgresql-dev gcc python3-dev musl-devjpeg-dev zlib-dev

# install python dependencies
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# add app

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



