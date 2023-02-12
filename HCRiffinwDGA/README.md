HCRiffinwDGA
===============

Intro
-----

HCRiffinwDGA is a combination of SELKS system based on IDS/IPS platform with integrated Domain Anomaly detection (specifically DGA Domain) using machine learning.

The system will monitor the DNS, analyze the Internet access of users in the network. Thereby, extracting the domains that users access and classifying that domain. The classification results will be sent back to SELKS.

This version of HCRiffinwDGA is based on docker and intended to provide easier deployment and management.      
The installation procedure here is valid for any Linux OS that supports docker.

Minimum Requirements
--------------------
- 2 cores
- 8 GB of free RAM
- 10 GB of free disk space (actual disk occupation will mainly depend of the number of rules and the amount of traffic on the network). 200GB+ SSD grade is recommended.
- ``git``, ``curl``
- ``docker`` > 17.06.0 (will be installed during SELKS initial setup)
- ``docker-compose`` > 1.27.0 (will be installed during SELKS initial setup)

Install process
---------------
### Basic installation

```bash
git clone https://github.com/HaoPV-HPT/Hcriffin.git
cd Hcriffin/
sudo ./easy-setup.sh
sudo docker-compose up -d
```

Once the containers are up and running, you should just point your browser to `https://your.selks.IP.here/`
If you chose to install Portainer during the installation, you must visit `https://your.selks.IP.here:9443` to set portainer's admin password


### Credentials and log in

In order to access scirius, you will need following credentials:

-   user: `selks-user`
-   password: `selks-user`

