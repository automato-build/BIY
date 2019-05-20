#include <neotimer.h>
Neotimer dir_led_blink_timer = Neotimer(300);
Neotimer compass_led_change_timer = Neotimer(1500);

int directional_led_blink_max_number = 20;
int compass_led_limit = 5; // stop at water

int fake_counter = 0;
boolean dir_leds_on = false;

int compass_led_counter = 0;

boolean cycleDirLEDs = false;
boolean cycleCompassLEDs = false;



#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

#define LED_PIN    12
#define LED_COUNT 18
Adafruit_NeoPixel pixels(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ400);

// non neopixel, digital pin leds
#define MOUNTAIN 7
#define WATER 8
#define AUSPICIOUS A4
#define CONNECTED 13

#include <RotaryEncoder.h>
RotaryEncoder encoder(A1, A2);


#include <Bounce2.h>
#define BUTTON_PIN A0
Bounce debouncer = Bounce();


void setup() {
  Serial.begin(9600);

  pinMode(BUTTON_PIN, INPUT_PULLUP);
  debouncer.attach(BUTTON_PIN);
  debouncer.interval(5);


  pixels.begin();           // INITIALIZE NeoPixel pixels object (REQUIRED)
  pixels.show();            // Turn OFF all pixels ASAP
  pixels.setBrightness(50);

  pixels.clear();

  // 1. INNER RING BLINK FOR 3 times AND TURN OFF
  //    OnSeq(max_number_of_blink, delay_between_blinks);
  InnerRingOnSeq(3, 500);
  delay(250);

  initiateNonNeopixelLEDs();
  // 2. GPS LED blink 3 time AND TURN ON
  GPSConnectionSeq(5, 100);
  delay(250);
  // 3. Mountaina nd water LED turn ON
  mountainWaterTurnOn();
  delay(500);
  // 4. Compass selection is "Fire"
  CompassLEDFireOnAtBegining(0);
}

void CompassLEDFireOnAtBegining(int _id) {
  //  pixels.clear();
  pixels.setPixelColor(_id, pixels.Color(150, 155, 10));
  pixels.show();
}

void CompassLEDFireOff(int _id) {
  //  pixels.clear();
  pixels.setPixelColor(_id, pixels.Color(0, 0, 0));
  pixels.show();
}

void InnerRingOnSeq(int _counter, int _delay) {
  int c = 1;
  while (c <= _counter) {
    amberOn();
    delay(_delay);
    amberOff();
    delay(_delay);
    c++;
  }
  amberOff();
}

void amberOn() {
  pixels.clear();
  //  Turn on
  for (int i = 13; i < 18; i++) {
    pixels.setPixelColor(i, pixels.Color(255, 255, 255));
  }
  pixels.show();
}

void amberOff() {
  pixels.clear();
  //  Turn on
  for (int i = 13; i < 18; i++) {
    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
  }
  pixels.show();
}

void initiateNonNeopixelLEDs() {
  pinMode(CONNECTED, OUTPUT);
  pinMode(MOUNTAIN, OUTPUT);
  pinMode(WATER, OUTPUT);
}

void GPSConnectionSeq(int _counter, int _delay) {
  static int c = 1;
  while (c <= _counter) {
    digitalWrite(CONNECTED, HIGH);
    delay(_delay);
    digitalWrite(CONNECTED, LOW);
    delay(_delay);
    c++;
  }
  digitalWrite(CONNECTED, HIGH);
}

void mountainWaterTurnOn() {
  digitalWrite(MOUNTAIN, HIGH);
  digitalWrite(WATER, HIGH);
}

void mountainWaterTurnOff() {
  digitalWrite(MOUNTAIN, LOW);
  digitalWrite(WATER, LOW);
}


int encoderPos() {
  static int pos = 0;
  encoder.tick();

  int newPos = encoder.getPosition();
  if (pos != newPos) {
    return newPos;
    pos = newPos;
  }
}

void assignLED(int _id) {
  pixels.clear();
  pixels.setPixelColor(_id, pixels.Color(255, 255, 255));
  pixels.show();
}

void ShowBalanceDirection(String _dir, int _max_blink_count) {
  if (dir_led_blink_timer.repeat(_max_blink_count)) {
    dir_leds_on = !dir_leds_on;
    fake_counter++;

    if (dir_leds_on) {
      if (_dir == "left") {
        showLeft();
      }
      if (_dir == "right") {
        showRight();
      }
    } else {
      directionLEDsOFF();
    }
    //    Serial.println(fake_counter);
  }
}


void directionLEDsOFF() {
  for (int i = 8; i <= 12; i++) {
    pixels.setPixelColor(i, pixels.Color(0, 0, 0));
    pixels.show();
  }
}

void showRight() {
  for (int i = 10; i <= 12; i++) {
    pixels.setPixelColor(i, pixels.Color(255,   0,   0));
    pixels.show();
    delay(20);
  }
}

void showLeft() {
  for (int i = 10; i >= 8; i--) {
    pixels.setPixelColor(i, pixels.Color(255,   0,   0));
    pixels.show();
    delay(20);
  }
}

void ShowCompassDirLEDs(String _dir, int _max_blink_count) {
  if (compass_led_change_timer.repeat(_max_blink_count)) {
    //    Serial.println(compass_led_counter);
    pixels.setPixelColor(compass_led_counter, pixels.Color(255, 255, 255));
    pixels.setPixelColor(compass_led_counter - 1, pixels.Color(0, 0, 0));
    pixels.show();

    compass_led_counter++;
  }
}

int POS = 1;
int OLDPOS = 1;
int innerledID = 13; // inner ring first LED
int outerledID = 0;
int button_state = 0;
int old_button_state = 0;
String balance_dir = "";

boolean RESET = false;

void(* resetFunc) (void) = 0; //declare reset function @ address 0

void loop() {
  RESET = false;
  // FAKE SELECT FIRE ELEMENT (5th inner right LED)
  while (POS <= 5) {
    Serial.println(POS);
    innerledID = int(map(POS, 1, 5, 13, 17));
    assignLED(innerledID);
    POS++;
    delay(1500);
  }
  //  Serial.println("--------");
  //  Serial.println(POS);

  // FAKE BUTTON PRESSED TO SELECT ELEMENT
  if (POS == 6) {
    button_state = 1;
  }


  if (button_state != old_button_state) {
    Serial.println(button_state);
    if (button_state == 1) {
      cycleDirLEDs = true;
      cycleCompassLEDs = true;

      dir_led_blink_timer.repeatReset();
      compass_led_change_timer.repeatReset();

      fake_counter = 0;
      compass_led_counter = 0;

      CompassLEDFireOff(0); // it was set on at begining

      // POS == 5;
      // so
      balance_dir = "right";

      //      Serial.println(POS);
      //      Serial.println(balance_dir);
    }
    old_button_state = button_state;
  }

  if (cycleDirLEDs) {
    ShowBalanceDirection(balance_dir, directional_led_blink_max_number);
  }
  //     cycle ouside led till it reached water LED at the same time
  if (cycleCompassLEDs) {
    ShowCompassDirLEDs(balance_dir, compass_led_limit);
  }

  if (fake_counter == directional_led_blink_max_number) {
    cycleDirLEDs = false;
    fake_counter = 0;
    directionLEDsOFF();
  }

  if (compass_led_counter == compass_led_limit) {
    cycleCompassLEDs = false;
    compass_led_counter = 0;

    resetFunc();
  }

}
