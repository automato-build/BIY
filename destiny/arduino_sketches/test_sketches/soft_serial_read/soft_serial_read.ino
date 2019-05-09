#include <SoftwareSerial.h>

SoftwareSerial PISerial(2, 3); // RX, TX

String inputString = "";
bool stringComplete = false;

boolean enableReading = false;

void setup() {
  //  enableReading = false;

  Serial.begin(9600);
  while (!Serial) {
    ;
  }
  PISerial.begin(57600);
}

void loop() {
  if (PISerial.available() && !stringComplete) {
    enableReading = false;
    // get the new byte:
    char inChar = (char)PISerial.read();
    // add it to the inputString:
    inputString += inChar;
    if (inChar == ':') {
      stringComplete = true;
    }
  }
  if (stringComplete) {
    Serial.println(inputString);
    parsedata(inputString);
    inputString = "";
    stringComplete = false;
    enableReading = true;
  }


  //  Serial.println(enableReading);

  if (enableReading) {
    Serial.println("was enabled. will disable now");
    //    delay(5000);
    enableReading = false;
  }
}

void parsedata(String _data) {
  int idxOfFirstComma = _data.indexOf(',');
  String _string = _data.substring(0, idxOfFirstComma);
  int _num = _data.substring(idxOfFirstComma + 1, _data.length() - 1).toInt();
  Serial.println(_string);
  Serial.println(_num);
}
