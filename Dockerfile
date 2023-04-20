# Base build
FROM python:3.10-alpine as base
RUN apk add --update --virtual .build-deps \
    build-base \
    python3-dev \
    libpq

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Now multistage build
FROM python:3.10-alpine
WORKDIR /app
RUN apk add libpq
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY . /app
EXPOSE 8000
CMD [ "sh", "start-server.sh" ]
