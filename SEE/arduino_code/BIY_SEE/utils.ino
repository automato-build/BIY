
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




int stringIndex=0;
void checkDataFromPi(){
	if (rpi.available()) {
		char c=rpi.read();
		if (c=='\n') {

			strcpy(lastCommandReceived, cmdFromPI);
			stringComplete=true;
			for (int i=0; i<30; i++) {
				cmdFromPI[i] = (char)0;
			}

			stringIndex=0;
		}else{
			cmdFromPI[stringIndex]=c;
			stringIndex++;
		}
	}
}


void beliefOut(){
	//send string out

	Serial.print(SmorfiaNumber);
	Serial.print(F("-"));
	Serial.print(SmorfiaLabel);
	Serial.println();

	//set putput analog value
	int outputNumber;
	outputNumber = atoi(SmorfiaNumber);
	analogWrite(OUTNUMPIN, map(outputNumber,0,90,0,1024));

	//set badluck led
	if (outputNumber==17) {
		digitalWrite(OUTBOOLPIN,HIGH);
	}else{
		digitalWrite(OUTBOOLPIN,LOW);
	}
}
