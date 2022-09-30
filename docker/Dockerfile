from python:3.10

# Environment variables

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY .pyproject.toml ./poetry.lock /code/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]