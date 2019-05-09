#!/bin/sh

clear
echo "\n=> INSTALLING & UPDATING pip & pip3 . HOLD TIGHT .. \n"
sleep 1
sudo apt install python-pip python3-pip -y
echo "\n=> INSTALLED & UPDATED pip & pip3 \n"
sleep 1
clear
sleep 1

# setting up SWAP
# get some swap memory so that the process doesn't die
# edit file /etc/dphys-swapfile and change CONF_SWAPSIZE value from 100 to 4096
echo "=> SETTING UP SWAP ASSUMING IT's a 32 GB partition"
sudo sed -i '/CONF_SWAPSIZE=100/s/^#*\s*//g' /etc/dphys-swapfile
sudo sed -i 's/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=4096/' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
echo "\n=> 4GB SWAP PARTITION activated! \n"
sleep 1
clear
sleep 1

# setup external sound card
echo "=> SETTING UP SOUND CARD IN ALSA CONFIGURATION \n"
sudo sed -i 's/defaults.ctl.card 0/defaults.ctl.card 1/' /usr/share/alsa/alsa.conf
sudo sed -i 's/defaults.pcm.card 0/defaults.pcm.card 1/' /usr/share/alsa/alsa.conf
sudo amixer cset numid=6 100%
sudo amixer cset numid=8 100%
sudo amixer cset numid=4 100%
sudo alsactl store
echo "\n=> SOUND CARD SETUP SUCCESSFULL\n"
sleep 1
clear
sleep 1

# INSTALLING SpeechRecognition
echo "=> INSTALLING SpeechRecognition.. \n"
sudo apt-get install python-pyaudio python3-pyaudio -y
sudo apt-get install build-essential swig libpulse-dev libasound2-dev portaudio19-dev flac -y
sudo pip install pyaudio
sudo pip3 install pyaudio
sudo pip3 install SpeechRecognition
sudo pip3 install google-api-python-client gcloud oauth2client
sudo pip3 install --upgrade pocketsphinx
echo "\n=> Installed SpeechRecognition!"
sleep 2
clear
sleep 2

# Replace __init__.py file of SpeechRecognition library to accommodate new azure api calls: 
echo "\n=> PATCHING __INIT_.py for newer Azure cloud support in SpeechRecognition.. \n"
sudo cp /usr/local/lib/python3.5/dist-packages/speech_recognition/__init__.py /usr/local/lib/python3.5/dist-packages/speech_recognition/__init__.py.backup
sudo cp /modified/__init__.py /usr/local/lib/python3.5/dist-packages/speech_recognition/__init__.py
echo "\n=> DONE PATCHING & SpeechRecognition LIB INSTALLED!\n"
sleep 2
clear
sleep 2

# Installing RPi.GPIO
echo "=> SETTING UP RPi.GPIO Lib.. \n"
sudo pip3 install RPi.GPIO
echo "\n=> GPIO library INSTALLED!\n"
sleep 2
clear
sleep 2

# installing tts libs
echo "=> SETTING UP TEXT TO SPEECH Libs.. \n"
sudo apt-get install espeak -y
sudo pip3 install pyttsx3
echo "\n=> espeak and pyttsx3 is INSTALLED SUCCESSFULLY!\n"
sleep 2
clear
sleep 2

# installing pi power manager
echo "=> SETTING UP SAFE POWERING UTILITY.. \n"
git clone https://github.com/Howchoo/pi-power-button.git
sudo chmod u+x pi-power-button/script/install
sudo ./pi-power-button/script/install
sudo rm -rf pi-power-button/
echo "=> SAFE POWERING UTILITY SETUP COMPLETE! \n"
sleep 2
clear
sleep 2

# INSTALLING spacy
echo "=> INSTALLING SPACY.. \n"
# if cat /proc/device-tree/model is Raspberry Pi Zero W Rev 1.1
sudo apt install libatlas3-base libatlas-base-dev
sudo pip3 uninstall numpy
apt install python3-numpy

sudo pip3 install -U spacy
sudo python3 -m spacy download en
echo "\n=> SPACY INSTALLED!\n"
sleep 2
clear
sleep 2

echo "== ALL DONE INSTALLTION == \n"
echo "REBOOT NOW"
