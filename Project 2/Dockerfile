FROM python:3.11



# install system dependencies
RUN apt-get update && apt-get install -y curl

# install ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# scripts folder defaulting to read-only
COPY --chmod=777 scripts/ /scripts/
# RUN ls -la /scripts
# this just lists the scripts, so whenever theres anything changed here, it forces a new build for everything underneath
# not needed, and forces rebuild is scripts is changed
# also moved this under, cause we need the ollama download to the the upmost so nothing above it can change it

# make subdirectory
RUN mkdir -p /scripts

# make scripts executable
COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
COPY ./scripts/ollama-entrypoint.sh /scripts/ollama-entrypoint.sh
# COPY ./scripts/setup.sh /scripts/setup.sh
RUN chmod +x /scripts/entrypoint.sh
RUN chmod +x /scripts/ollama-entrypoint.sh
# RUN ls -la /scripts && \
#     chmod +x /scripts/*.sh
# ran the two files individually because theres more sh files added and we do not need to run those

# install requirements
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# # run setup script
# RUN /scripts/setup.sh

# copy app code
COPY ./app /code/app

