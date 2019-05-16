#!/bin/sh

# installing pi power manager
#echo "=> SETTING UP SAFE POWERING UTILITY.. \n"

#sudo cp /home/pi/BIY/SEE/modified/shutdown_pi.service /etc/systemd/system/shutdown_pi.service
#sleep 1
#chmod u+x /etc/systemd/system/shutdown_pi.service
#sleep 1
#sudo systemctl daemon-reload
#sudo systemctl enable shutdown_pi.service
#sudo systemctl start shutdown_pi.service

#sleep 1



echo "=> SETTING UP Serial"
# setup Serial over GPIO
sudo cp /home/pi/BIY/SEE/config/cmdline.txt /boot/cmdline.txt
sudo echo "dtoverlay=pi3-disable-bt" >> /boot/config.txt
sudo systemctl disable hciuart
pip3 install pyserial
sudo adduser pi tty
# pip install pyserial
echo"=> Serial available now at /dev/ttyAMA0 pin GPIO 14 GPIO 15"
sleep 1


# Disable default joy detection demo
echo "=> Disabling joy detection demo.. \n"
sudo systemctl disable joy_detection_demo
sleep 1


# installing AIY vision to smorfia service
echo "=> SETTING UP VISION2SMORFIA SERVICE.. \n"

sudo cp /home/pi/BIY/SEE/modified/vision2Smorfia.service /etc/systemd/system/vision2Smorfia.service
sleep 1
chmod u+x /etc/systemd/system/vision2Smorfia.service
sleep 1
sudo systemctl daemon-reload
sudo systemctl enable vision2Smorfia.service
sudo systemctl start vision2Smorfia.service

sleep 1


echo "=> customizing Message of the Day file\n\n"
sudo cp /home/pi/BIY/SEE/modified/motd /etc/motd
sleep 1
clear
sleep 1


echo "=> ALL THE INSTALLTION SUCCEFULLY FINISHED! :) \n\n"

sleep 4

echo "... REBOOTING NOW ..."

sleep 3

sudo reboot
