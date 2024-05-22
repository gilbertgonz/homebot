```
@@\   @@\                                   @@@@@@@\            @@\     
@@ |  @@ |                                  @@  __@@\           @@ |    
@@ |  @@ | @@@@@@\  @@@@@@\@@@@\   @@@@@@\  @@ |  @@ | @@@@@@\@@@@@@\   
@@@@@@@@ |@@  __@@\ @@  _@@  _@@\ @@  __@@\ @@@@@@@\ |@@  __@@\_@@  _|  
@@  __@@ |@@ /  @@ |@@ / @@ / @@ |@@@@@@@@ |@@  __@@\ @@ /  @@ |@@ |    
@@ |  @@ |@@ |  @@ |@@ | @@ | @@ |@@   ____|@@ |  @@ |@@ |  @@ |@@ |@@\ 
@@ |  @@ |\@@@@@@  |@@ | @@ | @@ |\@@@@@@@\ @@@@@@@  |\@@@@@@  |\@@@@  |
\__|  \__| \______/ \__| \__| \__| \_______|\_______/  \______/  \____/
```
 
HomeBot is an open source video surveillance application. It was made to offer an alternative to high-cost monitoring and surveillance systems. It currently provides real-time video streaming, real-time email and text notifications, basic authentication, and a containerized environment for easy deployment to any platform with a USB camera or webcam

<p align="center">
  <img src="https://github.com/gilbertgonz/homebot/blob/main/imgs/example.png">
</p>

## How to run:
1. Install [docker](https://docs.docker.com/engine/install/)

2. Clone repo:
    ```
    git clone https://github.com/gilbertgonz/homebot.git
    ```

3. Build:
    ```
    $ docker build \
        --build-arg USER=your_username \
        --build-arg PASSWD=your_passwd \
        --build-arg PORT=your_port \
        --build-arg ENABLE_NOTIFICATIONS=0 \
        --build-arg EMAIL=your_email \
        --build-arg EMAIL_PASSWD=your_email_passwd \
        --build-arg PHONE_NUM=your_phone_number \
        --build-arg CARRIER=your_phone_carrier \
        -t homebot .
    ```
    i. To enable notifications, input 1. Please note only gmail is supported. Also, you will need to make an app-specific password for your gmail, see the top answer [here](https://stackoverflow.com/questions/77340573/python-script-for-sending-an-email-via-gmail-refuses-to-accept-username-and-app) for easy guidance on how to do so.

4. Run:
    ```
    $ docker compose up --remove-orphans -d
    ```

5. Open browser and see video stream:
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
