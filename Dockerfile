FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

# make work directory
RUN mkdir /app

# set work directory
WORKDIR /app

# add requirement in project
ADD ./requirements.txt /app

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install -r requirements.txt
COPY ./Pipfile /app/Pipfile
RUN pipenv install --skip-lock --system --dev

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

# add project
ADD ./backend /app/backend

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
