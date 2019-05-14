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

int SmorfiaNumber=0;
String SmorfiaLabel="";

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
	stateMachine();
	String command=getStringFromPi();
	if(command!="") {
		parseCommand (command);
	}
}

void parseCommand(String s){
	if (s=="BYE") {

	}else if (s=="START") {

	}else{
		//Serial.println(s);
		int separatorPosition= s.indexOf(":");
		String number=s.substring(0,separatorPosition);
		SmorfiaNumber=number.toInt();
		SmorfiaLabel= s.substring(separatorPosition+1);
	}
}


void stateMachine() {
	switch (state) {
	case 0:    //I'm showing the splash screen
		if (readButton()||(timeExpired&&stringComplete)) {
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
			showResult(SmorfiaNumber,SmorfiaLabel);      // I shoow la mano n.5
			startTimer(5000);    //I start a timer for 5 seconds
		}
		break;
	case 3:    //I'm showign the resilting number
		if (timeExpired()) {       //after a while
			drawDreaming();
			startTimer(2000);
			state = 1;
		}
		break;
	}
}
