/*
   Init board buttons and variables
*/
int switchModePin = 12;

boolean buttonState;
boolean oldButtonState;

int state = 0;

/*
   Init oled screen
*/
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#include "graphics.h"

/*
   animations variables
*/

int current_Frame = 0;
int framesCount = 3;
long lastFrameChanged = 0;
int changeFrameSpeed = 250;


void setup() {
  pinMode(switchModePin, INPUT_PULLUP);
  Serial.begin(9600);
  initScreen();
  state = 0;
  drawSplash();
}

void loop() {
  readButton();
  //Serial.println(state);
  stateMachine();
}


void stateMachine() {
  switch (state) {
    case 0: //I'm showing the splash screen
      if (readButton()) {
        drawDreaming();
        startTimer(2000);
        state = 1;
      }
      break;
    case 1://I show entering dream mode screen
      if (timeExpired()) { //after a while go to state 2
        startTimer(2000);
        state = 2;
      }
      break;
    case 2: // I loop the icons animation
      showIconsAnimation();
      if (timeExpired()) { //after a while
        state = 3;
        show5(); // I shoow la mano n.5
      }
      break;
    case 3: //I'm showing la mano
      if (readButton()) { //when press the button reenter dreaming mode
        state = 4;
        drawDreaming();
        startTimer(1000);
      }
      break;
    case 4: // Im showing dreaming
      if (timeExpired()) { //after a while start the icon animation
        startTimer(2000);
        state = 5;
      }
      break;
    case 5: // I'm showing the icon animation
      showIconsAnimation();
      if (timeExpired()) { //after a while
        state = 6;
        show17(); // I shoow n.17
        digitalWrite(13, HIGH);
      }
      break;
    case 6: // I'm showing the number 17
      if (readButton()) {
        state = 0;
        drawSplash();
        digitalWrite(13, LOW);
      }
      break;
  }
}
