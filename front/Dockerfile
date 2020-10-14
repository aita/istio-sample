FROM python:3.9
ENV PYTHONUNBUFFERED=1

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install

COPY . .

CMD [ "uvicorn", "app:app" ]