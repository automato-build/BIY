#!/bin/sh

# installing pi power manager
echo "=> SETTING UP SAFE POWERING UTILITY.. \n"

sudo cp /home/pi/BIY/bad_luck/modified/shutdown_pi.service /etc/systemd/system/shutdown_pi.service
sleep 1
chmod u+x /etc/systemd/system/shutdown_pi.service
sleep 1
sudo systemctl daemon-reload
sudo systemctl enable shutdown_pi.service
sudo systemctl start shutdown_pi.service

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
sudo cp /home/pi/BIY/bad_luck/modified/motd /etc/motd
sleep 1
clear
sleep 1


echo "=> ALL THE INSTALLTION SUCCEFULLY FINISHED! :) \n\n"

sleep 4

echo "... REBOOTING NOW ..."

sleep 3

sudo reboot
