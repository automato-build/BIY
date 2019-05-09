/*
  Matthieu|6|jbfdghjsdbngfbsdhjbsvfhjasvjhasjhdsbfjhsdbfjhsd|9|sbfvhsfvhasvfhasvfghasvfasgfvhkfvashgfvagfhgfasghfc;
  Matthieu|6|You are influenced by Sun. You want respect and credit from people surrounding you. You want to be a winner and want to be appreciated for.|9|You are ruled by Sun. You tend to be confident, strong and independent. You dream to be a leader among the people. You present yourself as courageous;
  Matthieu|6|You are influenced by Sun You want respect and credit from people surrounding you You want to be a winner and want to be appreciated for This brings you positivity and creativity|9|You are ruled by Sun. You tend to be confident, strong and independent. You dream to be a leader among the people. You present yourself as courageous, daring and aggressive for the first impression.;
  Helen|8|You are influenced by Saturn. You want to be a leader in work. You want security in finance and authority. You want to be a big brother.|9|You have an emphasis by Saturn. You are able to draw your picture as successful administrators or business man. You have a great attractive personality.;
*/

//name
#include "Adafruit_Thermal.h"
#include "SoftwareSerial.h"

#define PRINTER_RX_PIN 5
#define PRINTER_TX_PIN 6

#define PI_RX_PIN 2
#define PI_TX_PIN 3

SoftwareSerial PrinterSerial(PRINTER_RX_PIN, PRINTER_TX_PIN);
Adafruit_Thermal printer(&PrinterSerial, 4);     // Pass addr to printer constructor., 4 goes to DTR for making printing faster

SoftwareSerial PISerial(PI_RX_PIN, PI_TX_PIN);

void setup() {
  //  Serial.begin(9600);

  PISerial.begin(9600);

  //  9600 for Nano thermal printer and 19200 for usual general serial thermal printer
  PrinterSerial.begin(9600);  // Initialize SoftwareSerial
  while (!PrinterSerial);

  printer.begin(80);

  printer.setSize('S');
  printer.println("arduino awake");
  printer.feed(2);

  //  delay(4000);
  //  Serial.println("next");
}

//String content = "";
//String oldContent = "";
//char character;

void loop() {
  //  while ( PISerial.available()) {
  //    character =  PISerial.read();
  //    content.concat(character);
  //  }
  // -------- for testing ----------
  //  while (Serial.available() > 0) {
  //    character =  Serial.read();
  //    content.concat(character);
  //  }
  // -------------------------------
  //
  //  if (content != oldContent) {
  //    if (content.length() > 0 && content.charAt(content.length() - 1) == ';') {
  //      //      Serial.println(content);
  //      printFormattedData(content);
  //      content = "";
  //    }
  //    oldContent = content;
  //  }
}

//void printFormattedData(String data) {
//  int firstDelimatorIndex = data.indexOf('|');
//  int secondDelimatorIndex = data.indexOf('|', firstDelimatorIndex + 1);
//  int thirdDelimatorIndex = data.indexOf('|', secondDelimatorIndex + 1);
//  int fourthDelimatorIndex = data.indexOf('|', thirdDelimatorIndex + 1);
//  int firstColonIndex = data.indexOf(';');
//
//  String firstName = data.substring(0, firstDelimatorIndex);
//  //  Soul Urge / Heart Desire
//  String soulUrgeNumber = data.substring(firstDelimatorIndex + 1, secondDelimatorIndex);
//  String heartDesire = data.substring(secondDelimatorIndex + 1, thirdDelimatorIndex);
//  // personality / inner dream
//  String personalityNumber = data.substring(thirdDelimatorIndex + 1, fourthDelimatorIndex);
//  String innerDreams = data.substring(fourthDelimatorIndex + 1, firstColonIndex);
//
//  //  Serial.println("For name: " + firstName);
//  //  Serial.println("Soul Urge Number is: " + soulUrgeNumber);
//  //  Serial.println("Heart Desire:");
//  //  Serial.println(heartDesire);
//  //  Serial.println();
//  //  Serial.println("Personality Number is: " + personalityNumber);
//  //  Serial.println("Inner Dreams:");
//  //  Serial.println(innerDreams);
//  //  Serial.println("--------------------------------");
//  //  Serial.println();
//
//  printer.setSize('L');
//  printer.boldOn();
//  printer.inverseOn();
//  printer.println(firstName);
//  printer.inverseOff();
//  printer.boldOff();
//
//  delay(1000);
//
//  printer.setSize('M');
//  printer.print("SOUL URGE NO.:");
//  printer.print(soulUrgeNumber);
//  printer.println(" ");
//  printer.println("HEART DESIRE:");
//  delay(1000);
//  printer.setSize('S');
//  printer.println(heartDesire);
//
//  printer.feed(1);
//
//  printer.setSize('M');
//  printer.print("PERSONALITY NO.:");
//  printer.print(personalityNumber);
//  printer.println(" ");
//  printer.println("INNER DREAMS:");
//  delay(1000);
//  printer.setSize('S');
//  printer.println(innerDreams);
//  printer.println("--------------------------------");
//  //
//  printer.feed(4);
//  printer.setDefault();
//
//  delay(2000);
//  Serial.println("next");
//  //  PISerial.println("next");
//}
