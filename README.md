﻿# Web Hosting On Microsoft Azure

From Html/CSS Website to Python App, Host anything you want.

## Register An Account In Microsoft Azure
Register using your student mail to get $100 Azure Credits + No Credit Card Required: [Click Here To Register](https://azure.microsoft.com/en-us/free/students?wt.mc_id=studentamb_268271).

## Create a Virtual Machines with your choice of specifications.
1. After registering go to search bar and type ***Virtual Machine*** and click on it.
2. Click On Create.
3. Select Azure Virtual Machine
4. Fill Up All the details regarding the VM and resource groups.
5. Create the VM.

## Connect to VM
You can connect to VM by using [Putty](https://apps.microsoft.com/detail/putty/XPFNZKSKLBP7RJ?hl=en-us&gl=NP?wt.mc_id=studentamb_268271). Or, you can use your preferred SSH client.
1. Open Putty and enter your VM's IP Address.

![Putty Configuration](https://raw.githubusercontent.com/diwas7777/Hosting-On-Microsoft-Azure/main/putty.JPG)

3. Click on open and click accept.
4. Enter your username setup at the time of creating VM.
5. Enter your password (Note: Password typed will not be visible to the user.)
4. Voila! You have connected to your virtual machine.

## Setup your server
Update Packages
```
sudo apt update && sudo apt upgrade -y
```

Note: If access denied problem occurs when running any of the command you can always change to root user by:
```
sudo su
```

Install Apache webserver
```
sudo apt install apache2 -y
```

Now that we have installed webserver, lets have an HTML file served in it:
```
cd /var/www/html/
sudo nano index.html
```

Paste the following into `HTML` file:
```
<html>
<head>
  <title> Webhosting </title>
</head>
<body>
  <p> I'm running this website on Azure VM!
</body>
</html>
```
Pretty cool, right?

Now navigate to [cloudflare.com](https://dash.cloudflare.com)
then
- Select Zerotrust from Sidebar
- Select Network/tunnel
- Create tunnel
- Select Cloudflared
- Name your tunnel
- Choose your environment
- Run the given command in your terminal (You will get cloudflared installed successfully message)
- Click Next
- Select the domain you want to host on and also the subdomain and also give the local address to route as shown in image below
  ![Route Traffic](https://raw.githubusercontent.com/diwas7777/Hosting-On-Microsoft-Azure/main/route%20traffic.png)

- Save tunnel
- Voila its done now your tunnel must show healthy for it to be working.
![it works](https://raw.githubusercontent.com/diwas7777/Hosting-On-Microsoft-Azure/main/it%20works.png)

Now you can serve any content through your website
