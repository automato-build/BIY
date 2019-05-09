#!/bin/sh

sudo apt-get update -y
clear
sleep 1


# installing pi power manager
echo "=> SETTING UP SAFE POWERING UTILITY.. \n"
sudo echo "sudo python /home/pi/BIY/harmony/Scripts/shutdown_pi.py &" >> /etc/rc.local


echo "=> SETTING UP pip and pip3"
sudo apt-get install git python-pip python3-pip -y
echo "\n=> both pip and pip3 are installed"
sleep 1
clear
sleep 1

echo"=> SETTING UP virtualenv and virtualenvwrapper"
sudo pip3 install virtualenv virtualenvwrapper
sudo pip install virtualenv virtualenvwrapper
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python" >> ~/.profile
echo "export VIRTUALENVWRAPPER_PYTHON3=/usr/bin/python3" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
source ~/.profile
mkvirtualenv harmonysensor_py3 -p python3
# source ~/.profile
# workon harmonysensor_py3
sleep 1
clear
sleep 1



echo"=> SETTING UP Serial"
# setup Serial over GPIO       
# You should do before: sudo raspi-config
# disbale console over serial
# enable hardware serial
sudo echo "dtoverlay=pi3-disable-bt" >> /boot/config.txt
sudo systemctl disable hciuart
pip3 install pyserial
# pip install pyserial
echo"=> Serial available now at /dev/ttyAMA0 pin GPIO 14 GPIO 15"
sleep 1
clear
sleep 1


echo "=> customizing Message of the Day file\n\n"
sudo mv /home/pi/BIY/harmony/modified/motd /etc/
sleep 1
clear
sleep 1


# Installing RPi.GPIO
echo "=> SETTING UP RPi.GPIO Lib.. \n"
pip3 install RPi.GPIO
echo "\n=> GPIO library INSTALLED!\n"
sleep 1
clear
sleep 1

echo "=> ALL THE INSTALLTION SUCCEFULLY FINISHED! :) \n\n"

sleep 4

echo "... REBOOTING NOW ..."

sleep 3

sudo reboot
