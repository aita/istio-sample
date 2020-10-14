FROM python:3.9
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install


CMD [ "uvicorn", "app:app" ]