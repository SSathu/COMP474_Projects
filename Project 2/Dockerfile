FROM python:3.11

# scripts folder defaulting to read-only
COPY --chmod=777 scripts/ /scripts/
RUN ls -la /scripts

# install system dependencies
RUN apt-get update && apt-get install -y curl

# install ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# make subdirectory
RUN mkdir -p /scripts

# make scripts executable
COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
COPY ./scripts/ollama-entrypoint.sh /scripts/ollama-entrypoint.sh
RUN ls -la /scripts && \
    chmod +x /scripts/*.sh

# install requirements
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy app code
COPY ./app /code/app

