#include <Bounce2.h>
#include <Smoothed.h>

#define ANALOG_PIN A0
#define buttonPin 2
#define luckyNumberPin 9
#define GoodOrBadPin 3

Smoothed <float> POT;

Bounce debouncer1 = Bounce();

void setup() {
  Serial.begin(9600);

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(GoodOrBadPin, OUTPUT);
  pinMode(luckyNumberPin, OUTPUT);

  debouncer1.attach(buttonPin);
  debouncer1.interval(6);

  POT.begin(SMOOTHED_EXPONENTIAL, 5);
  POT.clear();
}

int buttonState = 0;
int oldButtonState = 0;
int counter = 0;
String names[] = {
  "Lorenzo",
  "Simone",
  "My name is matilda",
  "He is Tobias",
  "I do not know",
  "They are Lukas and Henry"
};
int id = 0;
String theName = "";
int theLuckyVoltage = 0;
boolean GoodOrBad = false;

void loop() {
  float currentPotValue = analogRead(ANALOG_PIN);
  POT.add(currentPotValue);
  theLuckyVoltage = int(POT.get());



  debouncer1.update();
  buttonState = debouncer1.read();
  if (buttonState != oldButtonState) {
    if (buttonState == LOW) {
      counter++;
      if (counter == 1) {
        // send a random word;
        id = int(random(0, 7));
        theName = names[id];
        Serial.println(theName);
        //        counter = 0;
      }
      if (counter == 2) {
        // send good or bad boolean;
        GoodOrBad = !GoodOrBad;
        digitalWrite(GoodOrBadPin, GoodOrBad);
        //        Serial.println(GoodOrBad);
        //        counter = 0;
      }
      //
      if (counter == 3) {
        // send a random lucky numer; (0-1022)
        analogWrite(luckyNumberPin, theLuckyVoltage);
        //        Serial.println(theLuckyVoltage);
        counter = 0;
      }
    }
    oldButtonState = buttonState;
  }


}
