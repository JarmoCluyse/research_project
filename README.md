# Intro
This is a insallation manual for driving a Freenove 4WD smart car kit autonomous with a Raspberry Pi trough a neural network. In this document is a part of their tutorial, So you need only this document to assemble the car.
This is their tutorial.
https://github.com/Freenove/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi/blob/master/Tutorial.pdf

---
# Components
## 4WD Smart Car Board for Raspberry Pi
![](https://i.imgur.com/5tkb7ZH.png)

## Parts
![](https://i.imgur.com/4PU6OLW.png)

## Transmission parts
![](https://i.imgur.com/r1IoYYl.png)

## Acrylic parts
![](https://i.imgur.com/2tpfAu1.png)

## Electronic parts
![](https://i.imgur.com/2x7x9lV.png)

## Batteries
![](https://i.imgur.com/QQiLzG5.png)

## Raspberry Pi
![](https://i.imgur.com/HcXE5Wx.png)

## Tools
![](https://i.imgur.com/sIrb7K9.png)
![](https://i.imgur.com/kndrVON.png)
![](https://i.imgur.com/qIeDHiv.png)

---
# Assembling the car
## motor and wheels
### Step 1
Install the bracket on the boards with the 2x M3*8 bolts.
![](https://i.imgur.com/w7XhDLF.png)
### Step 2
Install the motor on the bracket with 2x M3*30 bolts and 2x M3 nuts.
![](https://i.imgur.com/jkfpbzo.png)
### Step 3
Repeat the proccess for the other 3 motors.
![](https://i.imgur.com/MJV1f4U.png)
### Step 4
Connect the motors to the board.
![](https://i.imgur.com/yG1YKon.png)
### Step 5
Install the wheels.
![](https://i.imgur.com/HpnlfZX.png)

## Infrared line tracking module (not used in this project)
### Step 1
Install the module with 4x M3*6 bolts and 2x M3*60 standoffs.
![](https://i.imgur.com/oY3Yptv.png)
### Step 2
Connect the module with the XH 2.54 5pin cable to the board.
![](https://i.imgur.com/t9dtFFL.png)

## Raspberry Pi
### Step 1
install the Raspberry Pi on the board with 4x M2.5*8+6 standoffs and 4x M2.5*4 bolts.
![](https://i.imgur.com/qQjfF47.png)
### Step 2
Connect the Raspberry Pi to the board and press until you can see the pins.
![](https://i.imgur.com/iJfSfLt.png)
![](https://i.imgur.com/EkdjElJ.png)

## Pan Tilt + Ultrasonic + Camera
### Step 1
take from one of the two servos the rocker arm and 2 M2.5*8 screws.
![](https://i.imgur.com/Jbp91N3.png)
### Step 2
Assemble the module.
![](https://i.imgur.com/kCMPMJc.png)
### Step 3
Mount the pan tilt module with the M2*4 screw from the package of the servo.
![](https://i.imgur.com/BHayH9a.png)
![](https://i.imgur.com/D671fE5.png)
### Step 4
Connect the servo motors to the board.
![](https://i.imgur.com/e2NrmJT.png)
### Step 5
Connect the cables at the side of pan tilt module.
Put the blue side of the cable to the servo.
![](https://i.imgur.com/sU0QZ8C.png) ![](https://i.imgur.com/X4BagMm.png)
### Step 6
Connect the camera cable to the Raspberry Pi. Blue side to the ethernet port on the Raspberry Pi
![](https://i.imgur.com/cfxPcCt.png) ![](https://i.imgur.com/0x1O13j.png)
### Step 7
connect the ultrasonic module to the board
![](https://i.imgur.com/W6MKdvq.png)

## Batteries
### Step 1
Place the batteries end press them towards + for optimal contact.
![](https://i.imgur.com/b6W7UtS.png)
### Step 2
Test with the buttons
![](https://i.imgur.com/Fb1ozDT.png)

**You can still power the Raspberry Pi when buttons are pressed**

---
# Installing Raspberry Pi OS
## Software needded
- Win32-DiskImager
- Putty

## Download the OS
We begin with downloading the OS from the site of Raspberry Pi
https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit
Here you choose for the version with desktop and reccomended software
![](https://i.imgur.com/KiqsePo.png)
## write the image to the microSD-card
open win32-Diskimager
select the image file and on device choose the microSD-card.
Press write.
![](https://i.imgur.com/gLVyHgN.png)

## Activate ssh
make a file on the microSD-card. Name it ssh in small letters and without extension.
![](https://i.imgur.com/Lj20wXK.png)

## set the wifi connection
make a file on the microSD-card. Name it wpa_supplicant.conf
write this in the file but change username, password and country
```shell=
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=BE

network={
    ssid="username"
    psk="password"
    key_mgmt=WPA-PSK
}
```
## Test the configuration
remove the microSD-card from your pc and place it in your Raspberry Pi
**never insert the microSD-card when Raspberry Pi is powered on**

Open Putty and connect to pi@raspberrypi on port 22. If this doesn't work you need to find the IP-address of the Raspberry Pi manually. You should get a notification from putty to trust the host. Accept this.
![](https://i.imgur.com/xgU7WsA.png) ![](https://i.imgur.com/QMizqVT.png)

## raspi-config
Become root of the system and open the configuration
```shell=
sudo -i
raspi-config
```
You should now see this.
![](https://i.imgur.com/BwGGXGi.png)

change the following:
- change password of pi user
    - System options
        - password
- change the hostname of the pi (you will have to change it when you want to connect with putty)
    - System options
        - hostname
- change boot options
    - System options
        - network at boot
            - off
        - splash screen
            - off
- change timezone and location options
    - Localization options
        - Timezone
        - keyboard
- activate interfaces
    - Interface options
        - camera
            - on
        - ssh
            - on (should already be on)
        - VNC
            - on
        - I2C
            - on
- change the resolution
    - display options
        - resolution
            - set to DMT mode 1920x1080 60Hz 16:9
- press finish
- reboot

## User account management
### add own user
Add the user.
```shell=
sudo adduser <username>
```
Add user to groups.
```shell=
sudo usermod -aG adm,dialout,cdrom,sudo,audio,video,plugdev,games,users,input,netdev,gpio,i2c,spi <username>
```

### Change the permission of the new user
Open the sudoers file.
```shell=
sudo visudo
```
Add this to the file
```shell=
<username> ALL=NOPASSWD:ALL
```
Safe the file.

### Disable the default pi user
for security we disable the pi user
```shell=
sudo usermod -L pi
```

## update the Raspberry Pi
```shell=
sudo apt install update
sudo apt install upgrade
```

## disable the audio module
There is a problem where the LED's are not working properly if this is not disabled.
### blacklist the snd_bcl2835
Make a new file.
```shell=
sudo nano /etc/modprobe.d/snd-clacklist.conf
```
add the following
```shell=
blacklist snd_bcm2835
```
### disable in the boor config
Open the config file.
```shell=
sudo nano /boot/config.txt 
```
Set the line dtparam=audio=on in comment.
![](https://i.imgur.com/NaWGRDg.png)

## download extra packages
These packages must be downloaded.
```shell=
sudo apt install -y jd i2c-tools libatlas-base-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test python3-smbus
```
Get the rules for ps4 controllers and reload the rules.
```shell=
sudo wget https://raw.githubusercontent.com/chrippa/ds4drv/master/udev/50-ds4drv.rules -O /etc/udev/rules.d/50-ds4drv.rules
sudo udevadm control –-reload-rules
sudo udevadm trigger
```

Open the file rc.local.
```shell=
sudo nano /etc/rc.local
```
After the # in this script add this line.
```shell=
/usr/local/bin/ds4drv &
```
Reboot the Raspberry Pi.

# the program
## install the software
Go to the place you want to download the code
download the software from github
```shell=
git clone https://github.com/JarmoCluyse/research_project.git
```
**The code is writen for python3!!**

install the packages
```shell=
pip3 install -r Assets/requirements.txt
```

## Connect the PS4 controller
open the bluetooth client
```shell=
sudo bluetoothctl
```
if there is no agent type this
```shell=
agent on
default-agent
```
Make the ps4 controller visable by pressing the PS-button and the share button at the same time and hold until the light on the controller starts flashing.
then type this
```shell=
scan on
```
You should find it as wireless controller. You will need it's mac-address.
then you type
```shell=
pair XX:XX:XX:XX:XX:XX
connect XX:XX:XX:XX:XX:XX
```
Remember the mac-address. Next time you can do this instead
```shell=
bluetoothctl connect XX:XX:XX:XX:XX:XX
```

## screen or not
There is a possibility to see the camera images on a laptop or tablet. For this you need to be connected trough VNC and start the program there. You can not start it with screen from putty.

### without screen
This is the more easy option. Check if your controller is still connected. Go to the directory where you downloaded the files. make sure these are the files you see
![](https://i.imgur.com/cBEukqw.png)
now use this command
```shell=
python3 DataUsage.py
```
### with screen (VNC on windows)
Open the VNC-viewer application. Go to file and klick new connection
![](https://i.imgur.com/DBbcYdu.png)
The VNC server is the IP-address of the Raspberry Pi or his hostname. name is the user you want to login with.
![](https://i.imgur.com/r8rA5ck.png)
Press ok and connect to the Raspberry Pi.
Open the terminal
![](https://i.imgur.com/t0LYhav.png)
Check if the controller is connected. Go to the directory where you downloaded the files. make sure that you are in the right directory (see without screen)
now use this command
```shell=
python3 DataUsage.py showpython3 DataUsage.py show
```

## DataUsage.py
start the program (with or without screen). When the program is initialized the lights will turn on and you will hear a beep. Then you can drive manual. Left joystick is throttle, up is forward, down is backwards. The right joystick is steering, left is left, right is right. when you press the option button the car will drive autonomously , the color of the led wil change and you will hear a beep. Then the neural net will be driving the car. When you press again, you will regain controlnthe lights wil change and you will hear a beep.

## DataCollection.py
If you want to collect new data change the DataUsage with DataCollection and again with or without show.
```shell=
python3 DataCollection.py show
```
start the program (with or without screen). When the program is initialized the lights will turn on and you will hear a beep. Then you can drive manual. Left joystick is throttle, up is forward, down is backwards. The right joystick is steering, left is left, right is right. when you press the option button the led's will change collor and you will hear a beep sound. The programm is now collecting data and saving the images. It begins to make a CSV file with the steering information. When you press the button again the saving of images will stop and the CSV file will be saved. This will be indicated with color change and another beep sound.

## DataTraining.py
This is somewhat more tricky. If you want to retrain the data, this is done with a ipynb file. This file is added to the Git repository. Ther however can not be run on the Raspberry py. you need to copy the file and the DataCollected directory to your computer. Then make a new envirement in the terminal.
```shell=
python3 -m venv .venv
```
then activate the envirement
```shell=
./.venv/Scripts/Activate.ps1
```
You need to install some pip packages
```shell=
pip install jupyter notebook numpy tensorflow sklearn matplotlib pandas scikit-image scipy opencv-python  
```
then start a server
```shell=
jupyter notebook
```
Now you can retrain the model with new data. When you are ready place the model_0.h5 file back on the Raspberry Pi in the folder Assets. Now the model is ready to use in DataUsage.py