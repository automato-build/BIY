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
#include <SoftwareSerial.h>


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

/*
   RASPBBERRY PI COMMUNICATION
 */

int RPI_RX= 11;
int RPI_TX= 10;
SoftwareSerial rpi(RPI_RX, RPI_TX); // RX, TX

String cmdFromPI="";
String lastCommandReceived="";
boolean stringComplete=false;

String SmorfiaNumber="0";
String SmorfiaLabel="";
String LabelToDisplay="";

void setup() {
	pinMode(switchModePin, INPUT_PULLUP);
	Serial.begin(9600);
	initScreen();
	state = 0;
	drawSplash();
	rpi.begin(9600);
}

void loop() {
	readButton();
	//Serial.println(state);
	checkDataFromPi();

	if (lastCommandReceived!="" && stringComplete) {
		parseCommand ();
		stringComplete=false;
	}

	stateMachine();
}

void parseCommand(){
	if (lastCommandReceived=="BYE") {

	}else if (lastCommandReceived=="START") {

	}else{
		// Serial.print(F("parsing "));
		// Serial.println(lastCommandReceived);

		int separatorPosition=lastCommandReceived.indexOf(':');

		SmorfiaNumber=lastCommandReceived.substring(0,separatorPosition).toInt();
		SmorfiaLabel=lastCommandReceived.substring(separatorPosition+1);

		// Serial.print(F("number: "));
		// Serial.println(SmorfiaNumber);
		// Serial.print(F("label: "));
		// Serial.println(SmorfiaLabel);
	}
}


void stateMachine() {
	switch (state) {
	case 0:    //I'm showing the splash screen
		if (readButton()||(timeExpired)) {
			drawDreaming();
			startTimer(2000);
			state = 1;
		}
		break;
	case 1:   //I show entering dream mode screen
		if (timeExpired()) {     //after a while go to state 2
			startTimer(2000);
			state = 2;
		}
		break;
	case 2:    // I loop the icons animation
		showIconsAnimation();
		if (timeExpired()) {     //after a while
			state = 3;

			LabelToDisplay=SmorfiaLabel;
			Serial.println(LabelToDisplay);
			Serial.println(SmorfiaLabel);

			showResult();      // I shoow la mano n.5
			startTimer(12000);    //I start a timer for 5 seconds
		}
		break;
	case 3:    //I'm showign the resUlting number
		scrollScreenAnimation(); //UPDATE THE POSITION OF THE LABEL (IT SHOULD BE SCROLLING)
		if (timeExpired()) {       //after a while
			drawDreaming();
			startTimer(2000);
			state = 1;
		}
		break;
	}
}
