# Deployment Process:
Personal notes for deploying software to a target machine

1. Build image, save it, and scp to target machine:

```
# install qemu
sudo apt install qemu-user-static

# build
$ docker build --force-rm --build-arg USER_ARG=enter_username --build-arg PASSWD_ARG=enter_passwd --build-arg PORT_ARG=enter_port --platform linux/arm64 -t homebot:arm64 .

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