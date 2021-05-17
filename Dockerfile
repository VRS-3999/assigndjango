# pull official base image
FROM python:3.6

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# run gunicorn
CMD gunicorn excelvalidate.wsgi:application --bind 0.0.0.0:$PORT