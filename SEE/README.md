# BIY

## Instructions on how to setup a new board:
- 1 Flash the BIY_SEE to the board using usb to serial adaptor.
- 2 If the upload doesn't work, press the reset button when uploading
- 3 Flash the latest version of the AIY vision image from https://github.com/google/aiyprojects-raspbian/releases to an sd card
- 4 CLone this repository in the home directory of the pi `git clone https://github.com/automato-build/BIY.git`
- 5 Go to the SEE directory `cd /home/pi/BIY/SEE`
- 6 Launch the BIY.SEE installer `./install.sh`
- 7 Wait for the board to reboot and enjoy.

## If somethng goes wrong
- 1 Log in the raspi and disable the BIY_SEE service `sudo systemctl stop vision2Smorfia.service`
- 2 move to the folder AIY_vision `cd BIY/SEE/AIY_vision/`
- 3 make sure that the vision2Smorfia.py file is executable `chmod +x vision2smorfia.py`
- 4 manually launch the vision2Smorfia.py `-/vision2Smorfia.py`
- 5 check the terminal for errors
- 6 google is your friend

### **notes:**
- make sure the python script you want to run is executable. you can change permissions using `chmod +x myscript.py`
- !!! after flashing the latest AIY image do not upgrade the raspi !!! orelese the drivers to connect to the vision bonnet will stop to work!

#instructions on how to convert the data from the numbers file to a json

1) export the data from numbers in csv format
2) go to http://www.convertcsv.com/csv-to-json.htm
3) use the template below to structure the data in a json
4) save the generated json


```
{lb}
   "{h1}":{f1},
   "{h2}":{(f2)==""?"null":f2},
   "{h3}":[
      {(f3)==""?"":"\""}{(f3)==""?"":f3}{(f3)==""?"":"\""}{(f3)!="" && (f4)!=""  ? ",":""}
      {(f4)==""?"":"\""}{(f4)==""?"":f4}{(f4)==""?"":"\""}{(f4)!="" && (f5)!=""  ? ",":""}
      {(f5)==""?"":"\""}{(f5)==""?"":{f5}{(f5)==""?"":"\""}{(f5)!="" && (f6)!=""  ? ",":""}
      {(f6)==""?"":"\""}{(f6)==""?"":{f6}{(f6)==""?"":"\""}{(f6)!="" && (f7)!=""  ? ",":""}
      {(f7)==""?"":"\""}{(f7)==""?"":{f7}{(f7)==""?"":"\""}{(f7)!="" && (f8)!=""  ? ",":""}
      {(f8)==""?"":"\""}{(f8)==""?"":f3}{(f8)==""?"":"\""}{(f8)!="" && (f9)!=""  ? ",":""}
      {(f9)==""?"":"\""}{(f9)==""?"":f3}{(f9)==""?"":"\""}{(f9)!="" && (f10)!=""  ? ",":""}
      {(f10)==""?"":"\""}{(f10)==""?"":f3}{(f10)==""?"":"\""}{(f10)!="" && (f11)!=""  ? ",":""}
      {(f11)==""?"":"\""}{(f11)==""?"":f3}{(f11)==""?"":"\""}{(f11)!="" && (f12)!=""  ? ",":""}
      {(f12)==""?"":"\""}{(f12)==""?"":f3}{(f12)==""?"":"\""}{(f12)!=""?"":""}
    ]
{rb}
```
