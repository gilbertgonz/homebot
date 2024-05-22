# Deployment Process:
Personal notes for deploying software to a target machine

1. Build image, save it, and scp to target machine:

```
# install qemu
sudo apt install qemu-user-static

# build
$ docker build \
    --force-rm \
    --build-arg USER=your_username \
    --build-arg PASSWD=your_passwd \
    --build-arg PORT=your_port \
    --build-arg ENABLE_NOTIFICATIONS=1_foryes_or_0_forno \
    --build-arg EMAIL=your_email \
    --build-arg EMAIL_PASSWD=your_email_passwd \
    --build-arg PHONE_NUM=your_phone_number \
    --build-arg CARRIER=your_phone_carrier \
    --platform linux/arm64 \
    -t homebot:arm64 .

# save image
$ docker save $image_id > homebot.tar

# scp to target machine
$ scp -P PORT_NUMBER -C homebot.tar USER@IP_ADDRESS:/home/$USER
```

2. In target machine load image and launch compose file:

```
# load image
$ docker load -i homebot.tar

# tag image
$ docker tag $image_id homebot:latest

# run compose file
$ docker compose up --remove-orphans -d
```