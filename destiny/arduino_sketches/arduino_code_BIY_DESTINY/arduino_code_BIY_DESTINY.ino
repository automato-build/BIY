/*
               +-----+
               |     |
               |     +--------------------------+
               |                                |
               |=                               |
               |=                          +----+
               |=       +----------+       |
               |=       |          |       |
               |=       |          |      =|
               |        |          |      =|
               |        +----------+      =|
               |                          =|
          +----+                          =|
          |                                |
          |                                |
          +--------------------------------+
   ______  __  __  __       __  __  ______  ______  ______
  /\  == \/\ \/\ \_\ \     /\ \_\ \/\  ___\/\  __ \/\  == \
  \ \  __<\ \ \ \____ \    \ \  __ \ \  __\\ \  __ \ \  __<
   \ \_____\ \_\/\_____\    \ \_\ \_\ \_____\ \_\ \_\ \_\ \_\
    \/_____/\/_/\/_____/     \/_/\/_/\/_____/\/_/\/_/\/_/ /_/

*********************************************************************************************
  THIS IS THE SOURCE CODE USED FOR ATMEGA328 written by Saurabh Datta, partner @ automato.farm
  Saurabh Datta ---- [www.dattasaurabh.com, hi@dattasaurabh.com]
  Copyright (C) 2019 automato.farm - 2019 hi@automato.farm [www.automato.farm]
  - All Rights Reserved
  Unauthorized copying of this work, via any medium is strictly prohibited without permission.

  NOTE: CHECK license.txt for details
*********************************************************************************************
  /*
  --------- TBD--------
  Analog Input read
  Send to pi
  Receive data after that and send out through output channel
*/

#include <Wire.h>
#include "Adafruit_MPR121.h"
#include <SoftwareSerial.h>
//#include <Smoothed.h>

SoftwareSerial PISerial(2, 3); // RX, TX

#ifndef _BV
#define _BV(bit) (1 << (bit))
#endif

// You can have up to 4 on one i2c bus but one is enough for testing!
Adafruit_MPR121 cap = Adafruit_MPR121();

// Keeps track of the last pins touched
// so we know when buttons are 'released'
uint16_t lasttouched = 0;
uint16_t currtouched = 0;

// --- for name/words as strings from other sesonrs
String inputString = "";
bool stringComplete = false;
// --- for receiving data from PI over software serial
String PImsg = "";
bool msgComplete = false;

//#define ANALOG_IN_PIN A0
//Smoothed <float> input_num;
//int theLuckyVoltage = 0;
//int prevInputVoltage = 0;

//#define numOUTPUTpin A1
#define boolINPUTpin 4
#define boolOUTPUTpin 5
int inputAnalogVal = 0;

boolean enableReading = true;



void(* resetFunc) (void) = 0; //declare reset function @ address 0

void setup() {
  enableReading = true;

  Serial.begin(9600);
  PISerial.begin(57600);

  pinMode(13, OUTPUT);

  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  delay(500);
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  delay(500);


  pinMode(boolOUTPUTpin, OUTPUT);
  pinMode(boolINPUTpin, INPUT);

  // reserve 200 bytes for the inputString:
  inputString.reserve(200);

  // This block code needs to be here to keep blocing until the i2c touch sensor is found.
  // Or else the program sometimes proceeds without initializing the touch sensor
  // and we cannot read the data
  if (!cap.begin(0x5A)) {
    while (1);
  }

  // analog input smoothing
  //  input_num.begin(SMOOTHED_AVERAGE, 20);
  //  input_num.clear();
}


void loop() {
  // -------- ECHO out bool - READ and WRITE bool - I don't need it to pass
  //  digitalWrite(boolOUTPUTpin, digitalRead(boolINPUTpin));

  // -------- READ analog value from other modules via analog pin
  //   send to pi for figuring out destiny
  //  float currentPotValue = analogRead(ANALOG_IN_PIN);
  //  input_num.add(currentPotValue);
  //  theLuckyVoltage = int(input_num.get());
  //  Serial.println(theLuckyVoltage);
  //  -----------------------------------------------------------

  // -------- READ Touch and Send process start flag by softwareserial to PI
  currtouched = cap.touched();
  if ((currtouched & _BV(1)) && !(lasttouched & _BV(1)) && enableReading) {
    PISerial.println("start");
    enableReading = false;
  }
  if ((currtouched & _BV(1)) && !(lasttouched & _BV(1)) && !enableReading) {
    PISerial.println("stop");
    enableReading = false;
  }
  lasttouched = currtouched;

  // -------- READ String from other SENSORS via default serial (look at the serial event)
  //  pass the constructed string to PI via softwareSerial when a newline arrives
  if (stringComplete && enableReading) {
    PISerial.println(inputString);
    inputString = "";
    stringComplete = false;
    enableReading = false;
  }
  if (stringComplete && !enableReading) {
    PISerial.println("stop");
    inputString = "";
    stringComplete = false;
    enableReading = false;
  }

  // -------- READ String from PI via softserial
  if (PISerial.available() && !msgComplete) {
    enableReading = false;
    char ic = (char)PISerial.read();
    PImsg += ic;
    if (ic == ':') {
      msgComplete = true;
    }
  }
  if (msgComplete) {
    // Serial.println(PImsg);
    //------------
    if (PImsg.length() > 0) {
      parserAllocaterAndTaskSchedular(PImsg);
    }

    PImsg = "";
    msgComplete = false;
    enableReading = true;
  }

  if (enableReading) {
    digitalWrite(13, HIGH);
  } else {
    digitalWrite(13, LOW);
  }

  delay(50);
}


void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}


void parserAllocaterAndTaskSchedular(String _data) {
  int idxOfFirstComma = idxOfFirstComma = _data.indexOf(',');
  String _string = _data.substring(0, idxOfFirstComma);
  int _num = _num = _data.substring(idxOfFirstComma + 1, _data.length() - 1).toInt();

  if (_string.equals("no_data") == false && _string.equals("rst") == false) {
    //  if ( _string.equals("rst") == false) {
    // means it's name. then only send it to printer arduino via default serial
    // show data was received
    digitalWrite(13, HIGH);
    delay(500);
    digitalWrite(13, LOW);
    delay(500);
    digitalWrite(13, HIGH);
    delay(500);
    digitalWrite(13, LOW);
    delay(500);


    Serial.println(_string);
    // delay(2000);

    // Serial.println(_num);
    // send the _num to pwm output
  }

  if ((_string.equals("rst") == true) ) {
    resetFunc();
  }
}
