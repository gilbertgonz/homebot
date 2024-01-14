FROM homebot/base_humble as build

COPY requirements.txt /

# Installing dependencies
RUN apt update && apt upgrade -y && apt install -y \
    python3-pip \
    && pip install -r /requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY images /
COPY static /
COPY templates /
COPY server.py /server.py

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

#####################
# Final release build
FROM scratch

COPY --from=build / /

WORKDIR /

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "server.py"]
