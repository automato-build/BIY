<<<<<<< HEAD
#/bin/sh
=======
#!/bin/sh
>>>>>>> 5e81d4b... last push for tonight/morning

sleep 2

# setting up SWAP
# get some swap memory so that the process doesn't die
# edit file /etc/dphys-swapfile and change CONF_SWAPSIZE value from 100 to 4096
clear
sleep 1
echo "=> SETTING UP SWAP ASSUMING IT's a 32 GB partition"
sudo sed -i '/CONF_SWAPSIZE=100/s/^#*\s*//g' /etc/dphys-swapfile
sudo sed -i 's/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=4096/' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
echo "\n=> 4GB SWAP PARTITION activated! \n"
sleep 1
clear
sleep 1

# INSTALLING python3.6
echo "=> INSTALLING python3.6..\n"
echo ">> Installing dependencies first and then building from source.\n"
echo ">> This will take some time. Go for a coffee :).. \n\n"
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libopenblas-dev cython3 libatlas-dev m4 libblas-dev cmake -y
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
tar xf Python-3.6.5.tar.xz
cd Python-3.6.5
./configure
make
sudo make altinstall
sudo mv /usr/local/bin/python3.6 /usr/bin/python3.6
sudo mv /usr/local/bin/python3.6m /usr/bin/python3.6m
sudo mv /usr/local/bin/python3.6m-config /usr/bin/python3.6m-config
cd ..
sudo rm Python-3.6.5.tar.xz
sudo rm -rf Python-3.6.5
echo "\n\n=> INSTALLED. NOW MAKING IT DEFAULT..\n"
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 2
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 3
echo "\n=> python3.6 INSTALLED and SETUP AS DEFAULT PYTHON ENV!\n"
sleep 1
clear
sleep 1

# INSTALLING pip3.6
echo "=> INSTALLING pip3.6..\n"
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py
sudo rm get-pip.py
echo "\n=> pip3.6 INSTALLED!\n"
sleep 1
clear
sleep 1

# TBD: Install virtual env
sudo pip3.6 install virtualenv virtualenvwrapper
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.profile
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.profile
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python" >> ~/.profile
echo "export VIRTUALENVWRAPPER_PYTHON3=/usr/bin/python3.6" >> ~/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.profile
<<<<<<< HEAD

source ~/.profile
# /bin/bash -c 'source ~/.bash_profile'
# /bin/bash -c 'source ~/.profile'
# . ~/.bash_profile
# . ~/.profile
=======
source ~/.profile
>>>>>>> 5e81d4b... last push for tonight/morning

mkvirtualenv destinysensor -p python3.6
# source ~/.profile
# workon destinysensor


# INSTALLING SpeechRecognition
echo "=> INSTALLING SpeechRecognition.. \n"
sudo apt-get install build-essential swig libpulse-dev libasound2-dev portaudio19-dev flac -y
pip3.6 install pyyaml numpy cython SpeechRecognition setuptools wheel pyaudio google-api-python-client gcloud oauth2client
pip3.6 install SpeechRecognition
pip3.6 install --upgrade pocketsphinx
sleep 1
clear
sleep 1

# Replace __init__.py file of SpeechRecognition library to accommodate new azure api calls: 
echo "\n=> PATCHING __INIT_.py for newer Azure cloud support in SpeechRecognition.. \n"
sudo cp /home/pi/.virtualenvs/destinysensor/lib/python3.6/site-packages/speech_recognition/__init__.py /home/pi/.virtualenvs/destinysensor/lib/python3.6/site-packages/speech_recognition/__init__.py.backup
sudo cp modified/__init__.py /home/pi/.virtualenvs/destinysensor/lib/python3.6/site-packages/speech_recognition/__init__.py
cd ..
echo "\n=> DONE PATCHING & SpeechRecognition LIB INSTALLED!\n"
sleep 1
clear
sleep 1

# INSTALLING spacy
echo "=> INSTALLING SPACY.. \n"
pip3.6 install spacy
python3.6 -m spacy download en
echo "\n=> SPACY INSTALLED!\n"
sleep 1
clear
sleep 1

# Installing RPi.GPIO
echo "=> SETTING UP RPi.GPIO Lib.. \n"
pip3.6 install RPi.GPIO
echo "\n=> GPIO library INSTALLED!\n"
sleep 1
clear
sleep 1

# installing tts libs
echo "=> SETTING UP TEXT TO SPEECH Libs.. \n"
sudo apt-get install espeak -y
pip3.6 install pyttsx3
echo "\n=> espeak and pyttsx3 is INSTALLED SUCCESSFULLY!\n"
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
pip3.6 install pyserial
echo"=> Serial available now at /dev/ttyAMA0 pin GPIO 14 GPIO 15"
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

# setup mpg321 player
# sudo apt-get install mpg321 -y
# sudo apt-get install


# installing pi power manager
echo "=> SETTING UP SAFE POWERING UTILITY.. \n"
git clone https://github.com/Howchoo/pi-power-button.git
sudo chmod u+x pi-power-button/script/install
sudo ./pi-power-button/script/installing
sudo rm -rf pi-power-button/
echo "=> SAFE POWERING UTILITY SETUP COMPLETE! \n"
sleep 1
clear
sleep 1


echo "=> customizing Message of the Day file\n\n"
sudo mv /home/pi/destiny_sensor/modified/motd /etc/
sleep 1
clear
sleep 1

echo "=> ALL THE INSTALLTION SUCCEFULLY FINISHED! :) \n\n"

sleep 4

echo "... REBOOTING NOW ..."

sleep 3

sudo reboot
