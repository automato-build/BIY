/*
      ^--------------------------------------+
      |    +-+ |                         |   |
      |    +-+ |                         |   |
      |     +  |                         |   |
      |        |                         |   |
      |        |                         |   |
      |     +-+|                         |   |
      |     | ||                         |   |
      |     +-+<------------------------<+   |
      +-------->\                        \<->v
                 \                        \
                  -\                       \-
                    \                        \
                     \                        >
                      ><----------------------->

       ______   __   __  __
      /\  == \ /\ \ /\ \_\ \
      \ \  __< \ \ \\ \____ \
       \ \_____\\ \_\\/\_____\
        \/_____/ \/_/ \/_____/
       _____    ______   ______   ______  __   __   __   __  __
      /\  __-. /\  ___\ /\  ___\ /\__  _\/\ \ /\ "-.\ \ /\ \_\ \
      \ \ \/\ \\ \  __\ \ \___  \\/_/\ \/\ \ \\ \ \-.  \\ \____ \
       \ \____- \ \_____\\/\_____\  \ \_\ \ \_\\ \_\\"\_\\/\_____\
        \/____/  \/_____/ \/_____/   \/_/  \/_/ \/_/ \/_/ \/_____/
       ______  ______   __   __   __   ______  ______   ______
      /\  == \/\  == \ /\ \ /\ "-.\ \ /\__  _\/\  ___\ /\  == \
      \ \  _-/\ \  __< \ \ \\ \ \-.  \\/_/\ \/\ \  __\ \ \  __<
       \ \_\   \ \_\ \_\\ \_\\ \_\\"\_\  \ \_\ \ \_____\\ \_\ \_\
        \/_/    \/_/ /_/ \/_/ \/_/ \/_/   \/_/  \/_____/ \/_/ /_/



*********************************************************************************************
  THIS IS THE SOURCE CODE USED FOR ATMEGA328 written by Saurabh Datta, partner @ automato.farm
  Saurabh Datta ---- [www.dattasaurabh.com, hi@dattasaurabh.com]
  Copyright (C) 2019 automato.farm - 2019 hi@automato.farm [www.automato.farm]
  - All Rights Reserved
  Unauthorized copying of this work, via any medium is strictly prohibited without permission.

  NOTE: CHECK license.txt for details
*********************************************************************************************
*/

//https://github.com/adafruit/Adafruit-Thermal-Printer-Library/pull/22/commits/107e1011a9765e1025f8b08f82fa56a28c40ebbe

/*
  ---------- TBD --------
  1. Remove any weired chars in received name with regexp lib
  2. ... 
*/

#include "Adafruit_Thermal.h"
#include "logo.h"
#include "mak_logo.h"
#include "SoftwareSerial.h"

#define PRINTER_RX_PIN 5
#define PRINTER_TX_PIN 6
#define DTR_PIN        4

SoftwareSerial PrinterSerial(PRINTER_RX_PIN, PRINTER_TX_PIN);
Adafruit_Thermal printer(&PrinterSerial, DTR_PIN);

String inputString = "";
bool stringComplete = false;

//const char* const destinies[9] PROGMEM = {
//  "You are influenced by Sun. You want respect and credit from people surrounding you. You want to be a winner and want to be appreciated for.",
//  "You are influenced by Moon. It makes you a peacemaker, born friendly and cooperative in nature. You have an inner desire of love, peace.",
//  "You are influenced by Jupiter. You reflect artistic talent, charismatic personality and cheerfulness. You have an urge to self express.",
//  "You are influenced by Uranus. You want to be safe for finance and future and respect loyalty and workmanship. For you Protection is utmost.",
//  "You are influenced by Mercury. You want freedom in every aspect of life. You are adventurous in unusual things. You are always curious.",
//  "You are influenced by Venus. You are idealistic. You have deep sense of responsibility. You are a nurturer. You desire for luxury in general.",
//  "You are influenced by Neptune. You are spiritual. You want peace and comfort. You want to be perfectionist and an intellectual.",
//  "You are influenced by Saturn. You want to be a leader in work. You want security in finance and authority. You want to be a big brother.",
//  "You are influenced by Mars. You want to be serve humanity and experience without expecting anything. You are courageous and take risks."
//};

void setup() {
  Serial.begin(9600);
  PrinterSerial.begin(19200);

  MainSerialflushReceive();
  PrinterSerialflushReceive();

  printer.begin(120);
  //  printer.upsideDownOn();
  printer.wake();
}


void loop() {
  if (stringComplete) {
    //    .. clean up and remove spaces and lower case it
    inputString.replace(" ", "");
    inputString.toLowerCase();

    //    Serial.println(inputString);
    //    Serial.print("Soul Urge Number: ");
    //    Serial.println(get_soul_urge_number(inputString));
    //    Serial.print("Personalilty number: ");
    //    Serial.println(get_heart_desire_number(inputString));

    String NAME = inputString;
    int DESTINY_NUMBER = get_soul_urge_number(inputString);
    if (NAME != "no_data" || DESTINY_NUMBER != 0) {
      printOut(NAME, DESTINY_NUMBER);
    }
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
      delay(2000);
    }
  }
}

void MainSerialflushReceive() {
  while (Serial.available()) {
    Serial.read();
  }
}

void PrinterSerialflushReceive() {
  while (PrinterSerial.available()) {
    PrinterSerial.read();
  }
}


//void printLogo(String _logo) {
//}


String destiny_char_map_list[] = {"ajs", "bkt", "clu",
                                  "dmv", "enw", "fox",
                                  "gpy", "hqz", "ir"
                                 };
String vowels = "aeiou";
String consonants = "bcdfghjklmnpqrstvwxyz";


// -------------------------------------------------------
// For Soul Urge or Heart Desire number: Use sum of vowels
// -------------------------------------------------------
int get_soul_urge_number(String _word) {
  // -------- CREATING VOWEL LIST PART ------- //
  char vowel_char_list[100]; // some large size
  int idx = 0;
  int numsList[100];

  for (unsigned int i = 0; i < _word.length(); i++) {
    for (unsigned int j = 0; j < vowels.length(); j++) {
      if (_word[i] == vowels[j]) {
        vowel_char_list[idx] = _word[i];
        idx++;
      }
    }
  }

  //-------- NUM LIST PART FROM VOWEL LIST---------//
  for (int t = 0; t < idx; t++) {
    //    Serial.println(vowel_char_list[t]);
    if (vowel_char_list[t] == 'a' || vowel_char_list[t] == 'j' || vowel_char_list[t] == 's' ) {
      numsList[t] = 1;
    } else if (vowel_char_list[t] == 'b' || vowel_char_list[t] == 'k' || vowel_char_list[t] == 't' ) {
      numsList[t] = 2;
    } else if (vowel_char_list[t] == 'c' || vowel_char_list[t] == 'l' || vowel_char_list[t] == 'u' ) {
      numsList[t] = 3;
    } else if (vowel_char_list[t] == 'd' || vowel_char_list[t] == 'm' || vowel_char_list[t] == 'v' ) {
      numsList[t] = 4;
    } else if (vowel_char_list[t] == 'e' || vowel_char_list[t] == 'n' || vowel_char_list[t] == 'w' ) {
      numsList[t] = 5;
    } else if (vowel_char_list[t] == 'f' || vowel_char_list[t] == 'o' || vowel_char_list[t] == 'x' ) {
      numsList[t] = 6;
    } else if (vowel_char_list[t] == 'g' || vowel_char_list[t] == 'p' || vowel_char_list[t] == 'y' ) {
      numsList[t] = 7;
    } else if (vowel_char_list[t] == 'h' || vowel_char_list[t] == 'q' || vowel_char_list[t] == 'z' ) {
      numsList[t] = 8;
    }
  }

  // --------- SUMMATION OF NUMBERS PART --------//
  int first_sum = 0;
  for (int t = 0; t < idx; t++) {
    first_sum += numsList[t];
  }
  if (first_sum != 10) {
    while (first_sum > 9) {
      first_sum = summation(first_sum);
    }
  }
  if (first_sum == 10) {
    first_sum = 1;
  }

  //  Serial.println(actual_sum);
  return first_sum;
}


//// ------------------------------------------------------------
//// For Personality or Inner Dream number: Use sum of consonents
//// ------------------------------------------------------------
//
//int get_heart_desire_number(String _word) {
//  // -------- CREATING CONSONANT LIST PART ------- //
//  char consonant_char_list[100]; // some large size
//  int idx = 0;
//  int numsList[100];
//
//  for (unsigned int i = 0; i < _word.length(); i++) {
//    for (unsigned int j = 0; j < consonants.length(); j++) {
//      if (_word[i] == consonants[j]) {
//        consonant_char_list[idx] = _word[i];
//        idx++;
//      }
//    }
//  }
//
//  //-------- NUM LIST PART FROM VOWEL LIST---------//
//  for (int t = 0; t < idx; t++) {
//    //    Serial.println(consonant_char_list[t]);
//    if (consonant_char_list[t] == 'a' || consonant_char_list[t] == 'j' || consonant_char_list[t] == 's' ) {
//      numsList[t] = 1;
//    } else if (consonant_char_list[t] == 'b' || consonant_char_list[t] == 'k' || consonant_char_list[t] == 't' ) {
//      numsList[t] = 2;
//    } else if (consonant_char_list[t] == 'c' || consonant_char_list[t] == 'l' || consonant_char_list[t] == 'u' ) {
//      numsList[t] = 3;
//    } else if (consonant_char_list[t] == 'd' || consonant_char_list[t] == 'm' || consonant_char_list[t] == 'v' ) {
//      numsList[t] = 4;
//    } else if (consonant_char_list[t] == 'e' || consonant_char_list[t] == 'n' || consonant_char_list[t] == 'w' ) {
//      numsList[t] = 5;
//    } else if (consonant_char_list[t] == 'f' || consonant_char_list[t] == 'o' || consonant_char_list[t] == 'x' ) {
//      numsList[t] = 6;
//    } else if (consonant_char_list[t] == 'g' || consonant_char_list[t] == 'p' || consonant_char_list[t] == 'y' ) {
//      numsList[t] = 7;
//    } else if (consonant_char_list[t] == 'h' || consonant_char_list[t] == 'q' || consonant_char_list[t] == 'z' ) {
//      numsList[t] = 8;
//    }
//  }
//
//  // --------- SUMMATION OF NUMBERS PART --------//
//  int first_sum = 0;
//  for (int t = 0; t < idx; t++) {
//    first_sum += numsList[t];
//  }
//  while (first_sum > 9) {
//    first_sum = summation(first_sum);
//  }
//  //  Serial.println(actual_sum);
//  return first_sum;
//}

int summation(int _num) {
  String NUM = String(_num);
  int s = 0;
  for (int i = 0; i < NUM.length(); i++) {
    s += String(NUM[i]).toInt();
  }
  return s;
}


void printName(String _name) {
  printer.setSize('L');
  //  Serial.println(_name);
  printer.println(_name);

}

void printNumber(String _num) {
  printer.boldOn();
  String number_area = "Destiny No.: " + _num;
  printer.println(number_area);
  printer.boldOff();
}

void printDestiny(String _numm) {
  String _destiny = "-";
  int __num = _numm.toInt();

  //  int _destiny_list_idx = __num - 1;
  //  _destiny = String(_destinies[_destiny_list_idx]);

  switch (__num) {
    case 1:
      _destiny = F("You are influenced by Sun. You want respect and credit from people surrounding you. You want to be a winner and want to be appreciated for.");
      break;
    case 2:
      _destiny = F("You are influenced by Moon. It makes you a peacemaker, born friendly and cooperative in nature. You have an inner desire of love, peace.");
      break;
    case 3:
      _destiny = F("You are influenced by Jupiter. You reflect artistic talent, charismatic personality and cheerfulness. You have an urge to self express.");
      break;
    case 4:
      _destiny = F("You are influenced by Uranus. You want to be safe for finance and future and respect loyalty and workmanship. For you Protection is utmost.");
      break;
    case 5:
      _destiny = F("You are influenced by Mercury. You want freedom in every aspect of life. You are adventurous in unusual things. You are always curious.");
      break;
    case 6:
      _destiny = F("You are influenced by Venus. You are idealistic. You have deep sense of responsibility. You are a nurturer. You desire for luxury in general.");
      break;
    case 7:
      _destiny = F("You are influenced by Neptune. You are spiritual. You want peace and comfort. You want to be perfectionist and an intellectual.");
      break;
    case 8:
      _destiny = F("You are influenced by Saturn. You want to be a leader in work. You want security in finance and authority. You want to be a big brother.");
      break;
    case 9:
      _destiny = F("You are influenced by Mars. You want to be serve humanity and experience without expecting anything. You are courageous and take risks.");
      break;
  }

  //  Serial.println(_destiny);
  printer.setSize('S');
  printer.println(_destiny);
}

void printOut(String _inputString, int _num) {
  printer.justify('C');
  printer.printBitmap(logo_width, logo_height, logo_data);
  printName(_inputString);
  String numbr = String(_num);
  printNumber(numbr);
  printer.feed(1);
  printDestiny(numbr);
  printer.justify('L');
  printer.println(" ");
  printer.println(F("- automato.farm"));
  printer.println(F("- Making beliefs since 2019"));
  printer.println(F(""));
  printer.printBitmap(mak_logo_width, mak_logo_height, mak_logo_data);
  printer.justify('C');
  printer.println(F("--------------------------------"));
  printer.feed(3);
  printer.wake();


  // ----- if inverse is on
  //  printer.justify('C');
  //  printer.println(F("--------------------------------"));
  //  printer.justify('L');
  //  printer.println(F(""));
  //  printer.printBitmap(mak_logo_width, mak_logo_height, mak_logo_data);
  //  printer.println(F("- Making beliefs since 2019"));
  //  printer.println(F("- automato.farm"));
  //  printer.feed(1);
  //  printer.justify('C');
  //  String numbr = String(_num);
  //  printer.upsideDownOn();
  //  printDestiny(numbr);
  //  printer.upsideDownOff();
  //  printer.boldOn();
  //  printer.println(F("DESTINY/DESIRE:"));
  //  printer.boldOff();
  //  printer.feed(1);
  //  printNumber(numbr);
  //  printer.feed(1);
  //  printName(_inputString);
  //
  //  printer.printBitmap(logo_width, logo_height, logo_data);
  //  printer.feed(3);
  //  printer.wake();
}
