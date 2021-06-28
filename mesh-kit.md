# Mesh Kit Setup Guide

## What you will need:
* PuTTY (PC only)
* Ubiquiti chrome extension (all OS)
* Hostifi Network Access: Password information contained in PCW Admin Shared Drive: https://drive.google.com/drive/u/3/folders/1oMfGkZimoJqySSOyc8GlbCZZaxVZKDZR

## Setup Steps
Once the antenna is set up (see diagram), the following steps should lead to the light being turned on. If there is already an accesspoint (with an ERX and wired rooftop antenna), then just the mesh antenna can be configured. 

1. Configure ERX
    1. Physically connect with network cable from laptop to port 0 on ERX
    2. Set laptop static IP 192.168.1.29
        1. For Macs: https://www.howtogeek.com/howto/22161/how-to-set-up-a-static-ip-in-mac-os-x/
    3. Go to 192.168.1.1 in browser
        1. Login using: Pcwadmin
        2. Pword: PHILLYwisper
    4. Open Ubiquiti Discovery. The wizard should pop up automatically
    5. If it does not click ‘wizard’ tab > ‘basic setup’
2. Identify IP
    1. Use ubiquiti discovery tool to find the IP of device
    2. Alternatively you could use nmap
3. Issue set-inform command
    1. ssh into device
        1. ssh ubnt@ip
        2. Default password ubnt
    3. Issue set-inform command
        4. set-inform url (ex. hostify.pwcp.org)
4. Adopt Network
    1. Device will pop-up in ubiquity chrome extension
    2. Click ‘adopt’
    3. Click ‘confirm’
    4. Should take 5mins or so

Keep settings for Edge setup the same

