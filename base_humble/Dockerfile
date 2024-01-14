FROM arm64v8/ubuntu:22.04 as build

# Installing ROS2 Humble
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    TERM=xterm \
    PYTHONIOENCODING=UTF-8 \
    ROS2_DISTRO=humble \
    DEBIAN_FRONTEND=noninteractive

RUN ln -snf /bin/bash /bin/sh

# Install development tools
RUN apt update && apt install -q -y --no-install-recommends \
    software-properties-common locales curl build-essential

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

# Installing dependencies
RUN apt update && apt upgrade -y && apt install -q -y --no-install-recommends \
    ros-humble-ros-core python3-rosdep python3-colcon-ros \
    python3-pip python3-colcon-common-extensions \
    ros-humble-rosbag2 \
    && rm -rf /var/lib/apt/lists/*

# Clean up
RUN apt-get remove -y --auto-remove build-essential gcc

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

#####################
# Final release build
FROM scratch

COPY --from=build / /

ENTRYPOINT ["/entrypoint.sh"]