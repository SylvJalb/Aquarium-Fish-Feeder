# Aquarium Fish Feeder

## Step 1 : Print alls parts

## Step 2 : Assemble all parts

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
pip install -r requirements.txt
touch env.py
```

## Step 6 : Network configurations
Put your environment variables in the env.py file:
```python
host = '0.0.0.0' # for internet visibility
port = '4600' # put the port you want to use (for exemple 4600)
```
Go on your internet router panel and configure your DNS define static IP to your Raspberry Pi.     
Open the port number in your router panel and configure it to your Raspberry Pi. (tcp protocol)

## Step 7 : Start the service
```bash
./run.sh
```

## Step 8 : IFTTT configuration