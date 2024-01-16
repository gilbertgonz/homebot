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
    - Host web interface via github
    - Backend running ROS2 and Django?
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

- **Notes:**
    - To build docker images for a different system architecture you need to install qemu:
        ```
        sudo apt install qemu-user-static
        docker build --force-rm --platform linux/aarch64 -t homebot/base_humble:aarch64 ./base_humble/
        ```