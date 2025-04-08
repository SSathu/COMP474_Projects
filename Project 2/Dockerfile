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
<<<<<<< HEAD
COPY ./scripts/setup.sh /scripts/setup.sh
=======
>>>>>>> d85a853ca654d6cb5755d15401b7893510a03886
RUN ls -la /scripts && \
    chmod +x /scripts/*.sh

# install requirements
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# run setup script
RUN /scripts/setup.sh

# copy app code
COPY ./app /code/app

