```
                       $$\   $$\                                   $$$$$$$\            $$\     
                       $$ |  $$ |                                  $$  __$$\           $$ |    
                       $$ |  $$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$ |  $$ | $$$$$$\$$$$$$\   
                       $$$$$$$$ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$$$$$$\ |$$  __$$\_$$  _|  
                       $$  __$$ |$$ /  $$ |$$ / $$ / $$ |$$$$$$$$ |$$  __$$\ $$ /  $$ |$$ |    
                       $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |$$\ 
                       $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$\ $$$$$$$  |\$$$$$$  |\$$$$  |
                       \__|  \__| \______/ \__| \__| \__| \_______|\_______/  \______/  \____/
```
 
 - HomeBot is an open source video surveillance application. It was made to offer an alternative to high-cost monitoring and surveillance systems. It currently provides video streaming with basic authentication and logs info of connected clients (for security purposes), all in a containerized environment for easy deployment to any platform with a USB camera

*Demo vid/photos coming soon*

## How to run:
1. Install [docker](https://docs.docker.com/engine/install/)

2. Clone repo:
    ```
    git clone https://github.com/gilbertgonz/homebot.git
    ```

2. Build:
    ```
    $ docker build --build-arg USER_ARG=enter_username --build-arg PASSWD_ARG=enter_passwd --build-arg PORT_ARG=enter_port -t homebot  .
    ```

3. Run:
    ```
    $ docker compose up --remove-orphans -d
    ```

4. Open browser and see video stream:
    ```
    http://127.0.0.1:PORT_NUMBER
    ```

6. If you want to set up online video monitoring, you need to:
    
    i. Find your public IP address (you can use [WhatIsMyIp](https://whatismyipaddress.com/) to find it).
    
    ii. From your router, forward the port you passed in the previous `docker build` command. 

    iii.  Open browser and see video stream outside local network:
    ```
    http://YOUR_PUBLIC_IP:PORT_NUMBER
    ```

 ## Disclaimer
 This is a simplified prototype. Not recommended for production, use at your own risk
