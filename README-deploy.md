# Deployment Process:
Personal notes for deploying software to a target machine

1. Build image, save it, and scp to target machine:

```
# install qemu
sudo apt install qemu-user-static

# build
$ docker build --force-rm --build-arg USER_ARG=enter_username --build-arg PASSWD_ARG=enter_passwd --build-arg PORT_ARG=enter_port --platform linux/arm64 -t homebot/web:arm64 .

# save image
$ docker save d9ddd8f743b9 > test3.tar

# scp to target machine
$ scp -C test3.tar gil@10.0.0.240:/home/gil
```

2. In target machine load image and launch compose file:

```
# load image
$ docker load -i test3.tar

# tag image
$ docker tag $image_id homebot/web:latest

# run compose file
$ docker compose up --remove-orphans -d
```