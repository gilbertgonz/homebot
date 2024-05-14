FROM ubuntu:jammy

# Args
ARG USER_ARG="default"
ARG PASSWD_ARG="default"
ARG PORT_ARG=1234

# Convert args to envs
ENV USER=${USER_ARG}
ENV PASSWD=${PASSWD_ARG}
ENV PORT=${PORT_ARG}

COPY requirements.txt /

# Installing dependencies
RUN apt update && apt upgrade -y && apt install -y \
    python3-pip libgl1 libglib2.0-0 python3-rpi.gpio \
    && pip install -r /requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY static /static
COPY templates /templates
COPY libs/ /libs
COPY server.py /server.py

WORKDIR /

CMD ["python3", "server.py"]
