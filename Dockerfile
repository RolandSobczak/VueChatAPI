FROM python:3.11.6

WORKDIR /src

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

COPY /src/pyproject.toml /src/poetry.lock /src/

RUN pip3 install poetry && \
    python -m poetry config virtualenvs.create false && \
    python -m poetry install --no-interaction --no-root

COPY /src /src/

RUN chmod 777 /src/entrypoint.sh

CMD ["/src/entrypoint.sh"]


