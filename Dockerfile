ARG DOCKER_REGISTRY
FROM $DOCKER_REGISTRY/python...

WORKDIR /...

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH=${PATH}:/home/.../.local/bin

COPY . .
