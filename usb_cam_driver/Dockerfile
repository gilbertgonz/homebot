FROM homebot/base_humble

COPY requirements.txt /

# Installing dependencies
RUN apt update && apt upgrade -y && apt install -y --no-install-recommends \
    python3-pip ros-humble-cv-bridge \
    && pip install -r /requirements.txt \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY usb_cam.py /usb_cam.py

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /web

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "usb_cam.py"]
