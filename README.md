# Homebot

 - Home robot for monitoring and survailence
 - Inspired by [Amazon's Astro](https://www.amazon.com/Introducing-Amazon-Astro/dp/B078NSDFSB)

## System Design

 - **Hardware:**

    - Raspberry Pi 4 
    - Wide angle camera / Night vision
    - Hub motors (motor controller pending) (odometry pending)
    - Arduino for interfacing hardware-to-compute (microROS)
    - 3D Print enclosures
    - PS4 controller for local control
    - Power for components (look into intuitive charging)

    - **Others:**
        - Power switch
        - Cooling
        - Rigid mounting
        - Led lights
        - Indicator LCD screen
        - etc.

- **Software:**

    - Containerized environment
    - View camera feed and control robot over internet

- **Future additions:**

    - Lidar for mapping? (odomentry pending)
    - Mobile app? ("Kuvy" python lib for mobile dev)
    - Increase height of camera placement?
    - Touch screen interface?

- **Pi info:**

    - User: gil
    - Password: password
    - Static IP: (netplan pending, usually 10.0.0.240 at home)


- **Deployment Process:**
    1. Build image, save it, and scp to target machine:
        ```
        # install qemu
        sudo apt install qemu-user-static

        # ensure you're using arm64 compatible base image like 'ubuntu:jammy'
        docker build --force-rm --build-arg USER_ARG=enter_username --build-arg PASSWD_ARG=enter_passwd --build-arg PORT_ARG=enter_port --platform linux/arm64 -t homebot/web:arm64 .
        
        # save image
        docker save d9ddd8f743b9 > test3.tar

        # scp to target machine
        scp -C test3.tar gil@10.0.0.240:/home/gil
        ```
    2. In target machine load image, run it, and run ngrok all in background:
        ```
        # load image
        docker load -i test3.tar

        # tag image
        docker tag $image_id homebot/web:latest

        # run compose file
        docker compose up --remove-orphans -d