# Deployment Process:
Notes on deploying software to target machine (NVIDIA Jetson Nano)

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
    --build-arg ENABLE_NOTIFICATIONS=1 \
    --build-arg ENABLE_DETECTION=1 \
    --build-arg EMAIL=your_email \
    --build-arg EMAIL_PASSWD=your_email_passwd \
    --platform linux/arm64 \
    -t homebot:arm64 -f Dockerfile.deploy .

# save image
$ docker save $image_id > homebot.tar

# save other run files
$ tar cf run_files.tar compose-jetson.yml run.sh

# scp to target machine
$ scp -P PORT_NUMBER -C homebot.tar USER@IP_ADDRESS:/home/$USER
```

2. In target machine load image and launch compose file:

```
# load image
$ docker load -i homebot.tar

# tag image
$ docker tag $image_id homebot:latest

# extract run files
$ tar xvf run_files.tar

# run
$ ./run.sh
```