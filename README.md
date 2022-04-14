# Aquarium Fish Feeder

## Step 1 : Print alls parts

For this, you need a 3D printer and ~100g of plastic (PLA).     

Find all stl files in the folder "3D_print" and print them.     
Instructions:   
- Nozzle: 0.4 mm
- Filament: PLA
- Layer height: 0.2 mm
- Infill: 10%
- Support: Yes for `Holder` (60°), No for Other parts
- Wall thickness: 2.0 mm (5 wall lines count) for `Holder`, By default for Other parts
- Disable "Union overlapping Volumes"

## Step 2 : Assemble all parts
For that, you can see my video [on YouTube](https://www.youtube.com/watch?v=yZgBFvdJES4). ([5:02](https://youtu.be/yZgBFvdJES4?t=302))    
[![Sylvain Jalbert - YouTube](https://img.youtube.com/vi/yZgBFvdJES4/0.jpg)](https://www.youtube.com/watch?v=yZgBFvdJES4)

## Step 3 : Install raspbian on your Raspberry Pi
1. Download [Raspbian OS](https://howtoraspberrypi.com/downloads/)    
1. Flash a SD card with the zip file by using [balenaEtcher](https://www.balena.io/etcher/) (for exemple)    
1. Plug the SD card into the Raspberry Pi and turn on the power.       
1. Follow the instructions on the screen to install the Raspbian OS.    

## Step 4 : Import the repo on your Raspberry Pi
```bash
git clone https://github.com/SylvJalb/Aquarium-Fish-Feeder.git
cd Aquarium-Fish-Feeder
```

## Step 5 : Installations
```bash
pip3 install -r requirements.txt
```
Make sure you have gunicorn installed. Do the command `which gunicorn` and make sure you have the good path in `run.sh` (last line).   

Then define your environment variables in env.py (`nano env.py`):
```python
timezone_name = "Europe/Paris" # Your timezone
pwm_gpio = 12 #Use pin 12 for PWM signal
frequence = 50

# Positions of the servo (in degrees)
posFeed = 160   #Position to drop the food
posReload = 30  #Position to reload the food
```

## Step 6 : Network configurations
Go on your internet router panel and configure your DHCP to define static IP to your Raspberry Pi.     
Open the port number in your router panel and configure it to your Raspberry Pi. (tcp protocol)

## Step 7 : Start the service
```bash
./run.sh
```
----------
If you want to automatically start the service at boot, create `/etc/systemd/system/feeder.service` file:
```bash
sudo nano /etc/systemd/system/feeder.service
```
Paste this content, then **modify paths** to your files:  
```bash
[Unit]
Description=feeder service

[Service]
User=pi
WorkingDirectory=/home/pi/Aquarium-Fish-Feeder
ExecStart=/bin/bash /home/pi/Aquarium-Fish-Feeder/run.sh
Restart=always

[Install]
WantedBy=multi-user.target
```     
Then, do `sudo systemctl enable feeder.service` to activate the auto-start of the service after each startup.

To start the service, do `sudo systemctl start feeder.service`

----------


## Step 8 : IFTTT configuration
Go on your IFTTT account and create a new webhook.
Add a Applet : **IF** you condition... **THEN** use webhook like this:

<img src="./images/IFTTT.png" width="300px">

# Log visualization
Now you can see the logs (dates when the feeder have been feeded) on this link:     
http://YOUR_IP_ADDRESS:PORT/feed

# Sources
https://raspberry-pi.fr/servomoteur-raspberry-pi/       
https://pythonbasics.org/flask-http-methods/        
