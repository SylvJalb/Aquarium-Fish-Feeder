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
git clone git@github.com:SylvJalb/Aquarium-Fish-Feeder.git
cd Aquarium-Fish-Feeder
```

## Step 5 : Installations
```bash
pip install -r requirements.txt
chmod +x run.sh
mkdir env.py
```

## Step 6 : Configurations
Put your environment variables in the env.py file:
```python
host = 'YOUR_IP_ADDRESS'
port = '80'
```

## Step 7 : Start the service
```bash
./run.sh
```