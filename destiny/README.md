### BIY DESTINY BOARD INSTALLATION_SETUP INSTRUCTIONS:
1. **_If you are using the_** `image_file` **_for PI, it comes bundled with everything. So plug and play. Follow the instructions of operation below._** [**SUGGESTED METHOD**]

    *NOTE: Do not update anything in this stock OS*

 2. **_If you want to fresh install everything:_**
    
    1. **Hardware**: `raspberry Pi3 A+`, (For rest, use the modules from the kit like the sound card, usb piggy back, speaker etc.)
    2. **Operating System**: `"Raspbian GNU/Linux 9 (stretch)" minimal comamnd line version`
    3. Do the typical PI setup steps like, Internet setup, SSH setup, system update and upgrade etc. 
    4. `git clone` this repository.
    5. **_Important:_** Make sure you have at-least the sound-card attached to the PI's USB before proceeding with the next steps.
    6. In `raspi-config` disable `console over serial` and enable `hardware serial`.
    7. `chmoc u+x install_dependencies_with_py3.6andVenv.sh`
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
    8. `sudo .install_dependencies_with_py3.6andVenv.sh`
=======
    8. `sudo ./install_dependencies_with_py3.6andVenv.sh`
>>>>>>> 5e81d4b... last push for tonight/morning
=======
    8. `sudo ./install_dependencies_with_py3.6andVenv.sh`
>>>>>>> 5e81d4b... last push for tonight/morning
=======
    8. `sudo ./install_dependencies_with_py3.6andVenv.sh`
>>>>>>> 5e81d4b... last push for tonight/morning
    9. This will take some time as it first downloads, builds and installs things like python3.6 (which doesn't come in raspbian and is absent from the package distribution), install virtual env, nlp packages, configures alsa (only if it can find teh attached hardware) etc.
    10. That's 
    11. Double check after installation script has ran, that everything is properly installed. ()
    12. create your own credentials and place them in dir: `python_scripts/api_creds/`
    13. We have a choice to use differemt AI services :

        1. Microsoft Azzure Cloud services: `azzure_creds.json`
        2. Google Cloud services:`google_creds.json`
        3. Houndify services: `houndify_creds.json`
        4. wit.ai services: `wit_ai_creds.json`
    14. By default you can see in `python_scripts/listener.py` under function `listen()` that azzure cloud service is enabled. You can use your one of choice by commenting or un-commenting the one service you'd like to use.
    15. 

### BIY DESTINY BOARD OPERATION INSTRUCTIONS:

### TO BE DONE NEXT:
1. **CORE functionality:** Correction in Hardware for destiny number/analog volatge OUTPUT.
2. **CORE functionality:** Implement Software for destiny number OUTPUT (*Arduino side*).
3. **CORE functionality:** Correction in Hardware for number/analog voltage INPUT.
4. **CORE functionality:** Implement Software for analog voltage INPUT and mapping to destiny number (*Arduino side*).
5. **GOOD TO HAVE:** Make digital IOs on pads available in main softwares.
