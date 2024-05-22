FROM ubuntu:jammy

COPY requirements.txt /

# Installing dependencies
RUN apt update && apt upgrade -y && apt install -y \
    python3-pip libgl1 libglib2.0-0 \
    && pip install -r /requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Args (see web/libs/notifications.py for list of supported carriers)
ARG USER="default"
ARG PASSWD="default"
ARG PORT=1234
ARG ENABLE_NOTIFICATIONS=0
ARG EMAIL="example@gmail.com"
ARG EMAIL_PASSWD="default"
ARG PHONE_NUM="1234567890"
ARG CARRIER="verizon"

# Convert args to envs
ENV USER=${USER} \
    PASSWD=${PASSWD} \
    PORT=${PORT} \
    ENABLE_NOTIFICATIONS=${ENABLE_NOTIFICATIONS} \
    EMAIL=${EMAIL} \
    EMAIL_PASSWD=${EMAIL_PASSWD} \
    PHONE_NUM=${PHONE_NUM} \
    CARRIER=${CARRIER} \

# Copy files
COPY web/ /web

WORKDIR /web

CMD ["python3", "server.py"]
