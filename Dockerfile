FROM alpine:latest

RUN apk add --update-cache \
    python3 \
    py-pip \
    && rm -rf /var/cache/apk/*

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]