# BIY

To run the code move into AIY_vision_experiments folder and run the example with './image_classification_camera.py'


### **notes:**
- make sure the python script you want to run is executable. you can change permissions using `chmod +x myscript.py`

- !!! after flashing the latest AIY image do not upgrade the raspi following!!! orelese the drivers to connect to the vision bonnet will stop to work!

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
