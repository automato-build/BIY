/*
   Init board buttons and variables
 */

boolean buttonState;
boolean oldButtonState;

int state = 0;

int OUTNUMPIN=9;
int OUTBOOLPIN=13;

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

int started=false;

/*
   RASPBBERRY PI COMMUNICATION
 */

int RPI_RX= 11;
int RPI_TX= 10;
SoftwareSerial rpi(RPI_RX, RPI_TX); // RX, TX

char cmdFromPI[30];
char lastCommandReceived[30];

boolean stringComplete=false;

char SmorfiaNumber[10];
char LabelToDisplay[30];

char SmorfiaLabel[30];

void setup() {
	pinMode(OUTNUMPIN, OUTPUT);
	pinMode(OUTBOOLPIN, OUTPUT);
	initScreen();
	drawSplash();
	Serial.begin(9600);
	rpi.begin(9600);
}

void loop() {
	checkDataFromPi();

	if (lastCommandReceived[0]!=0 && stringComplete) {
		parseCommand ();
		stringComplete=false;
	}

	stateMachine();
}

void parseCommand(){
	Serial.print("RECEIVED ->");

	Serial.println(lastCommandReceived);

	if(strcmp(lastCommandReceived, "BYE") == 0) {
		Serial.println("bye bye!");
		started=false;
		drawBye();
		state=4;
		startTimer(10000);

	}else if (strcmp(lastCommandReceived, "START") == 0) {
		Serial.println("starting now");
		started=true;
		initScreen();
		state = 0;
		drawSplash();

	}else{
		started=true;
		// Serial.print(F("parsing "));
		// Serial.println(lastCommandReceived);

		//find the separator position
		int separatorPosition=0;
		for (int i=0; i<30; i++) {
			if (lastCommandReceived[i]==':') {
				separatorPosition=i;
				break;
			}
		}
		//copy the first string
		for (int i=0; i<separatorPosition; i++) {
			SmorfiaNumber[i]=lastCommandReceived[i];
		}
		//copy the second string
		for (int i=0; i<30; i++) {
			SmorfiaLabel[i]=lastCommandReceived[i+separatorPosition+1];
		}

		// Serial.print(F("number: "));
		// Serial.println(SmorfiaNumber);
		// Serial.print(F("label: "));
		// Serial.println(SmorfiaLabelC);

	}
}


void stateMachine() {
	switch (state) {
	case 0:    //I'm showing the splash screen
		if (started) {
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

			strcpy(LabelToDisplay, SmorfiaLabel);
			showResult();      // I shoow la mano n.5
			beliefOut();
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

	case 4:    //I'm showign BYE BYE
		if (timeExpired()) {       //after a while
			startTimer(2000);
			state = 5;
			drawLogo();
		}
		break;

	case 5:     //I'm showing automato.farm logo
		if (timeExpired()) {        //after a while turn off the screen
			display.clearDisplay();
			display.display();
		}
		break;
	}
}
