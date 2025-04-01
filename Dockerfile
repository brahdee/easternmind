FROM pfeiffermax/python-poetry:1.12.0-poetry1.8.4-python3.12.7-slim-bookworm

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /easternmind
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry check && poetry install --no-interaction --no-cache

COPY . .

EXPOSE 8000
WORKDIR /easternmind/easternmind
RUN poetry run python manage.py migrate --noinput
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "easternmind.wsgi"]