# Hosting-On-Microsoft-Azure

From Html/CSS Website to Python App

## Register An Account In Microsoft Azure
Register using your student mail to get $100 Azure Credits + No Credit Card Required: [Click Here To Register](https://azure.microsoft.com/en-us/free/students/).

## Create a Virtual Machines with your choice of specifications.
1. After registering go to search bar and type ***Virtual Machine*** and click on it.
2. Click On Create.
3. Select Azure Virtual Machine
4. Fill Up All the details regarding the VM and resource groups.
5. Create the VM.

## Connect to VM
You can connect to VM by using [Putty](https://apps.microsoft.com/detail/putty/XPFNZKSKLBP7RJ?hl=en-us&gl=NP). Or, you can use your preferred SSH client.
1. Open Putty and enter your VM's IP Address.

![Putty Configuration](https://raw.githubusercontent.com/diwas7777/Hosting-On-Microsoft-Azure/main/putty.JPG)

3. Click on open and click accept.
4. Enter your username setup at the time of creating VM.
5. Enter your password (Note: Password typed will not be visible to the user.)
4. Voila! You have connected to your virtual machine.

## Installing Control Panel for the website we are going to host.
For control Panel we're going to install **Cyberpanel**
To install it copy and run the code.

Update Packages
```
sudo apt update && sudo apt upgrade -y
```

Change to root user
```
sudo su
su -
```

Install Cyberpanel
```
sh <(curl https://cyberpanel.net/install.sh || wget -O - https://cyberpanel.net/install.sh)
```


**Patience is the key.** Wait For CyberPanel To Finish Installing .....

## Setting Up CyberPanel
1. Open your favourite browser and enter
   ```
   https://yourVMipaddress:8090
   ```
2. Login using your login details
   ```
   Default Username: admin
   Password: Password Set During Installation
   ```
