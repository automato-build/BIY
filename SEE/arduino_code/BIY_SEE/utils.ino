
/*
 * timer stuff
 */

long lastTimerStarted;
int timeInterval;

boolean timeExpired(){
	if (millis()-lastTimerStarted>timeInterval) {
		return (true);
	}else{
		return (false);
	}
}

void startTimer(int t){
	timeInterval=t;
	lastTimerStarted=millis();
}

boolean readButton() {
	buttonState = digitalRead(switchModePin);
	if (!buttonState && oldButtonState) {
		delay(50);
		return true;
	}
	oldButtonState = buttonState;
	return false;
}



void checkDataFromPi(){
	if (rpi.available()) {
		char c=rpi.read();
		if (c=='\n') {
			lastCommandReceived=cmdFromPI;
			cmdFromPI="";
			stringComplete=true;
		}else{
			cmdFromPI+=c;
		}
	}
}
