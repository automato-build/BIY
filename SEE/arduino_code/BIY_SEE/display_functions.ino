int16_t x1_number, y1_number;
uint16_t w_number, h_number;

int16_t x1_label, y1_label;
uint16_t w_label, h_label;

int labelPosition=SCREEN_WIDTH;
int updateInterval=100;
long lastTImeScroll=0;


void initScreen() {
	if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
		Serial.println(F("SSD1306 allocation failed"));
		for (;;);   // Don't proceed, loop forever
	}
	display.clearDisplay();
	display.display();
	drawHorns();
	display.setTextWrap(false);

}

void calculateNumberSize(String s){
	display.getTextBounds(s, 0, 0, &x1_number, &y1_number, &w_number, &h_number);
	Serial.println(s);
	Serial.print(F("N_size: "));
	Serial.print(w_number);
	Serial.print(F(" "));
	Serial.println(h_number);


}

void calculateLabelSize(String s){
	display.getTextBounds(s, 0, 0, &x1_label, &y1_label, &w_label, &h_label);
	Serial.println(s);
	Serial.print(F("L_width: "));
	Serial.print(w_label);
	Serial.print(F(" "));
	Serial.println(h_label);
}


void drawHorns() {
	display.clearDisplay();
	display.drawBitmap(
		(display.width()  - corna_size[0] ) / 2,
		(display.height() - corna_size[1]) / 2,
		corna, corna_size[0], corna_size[0], WHITE);
	display.display();
}

void drawEye() {
	display.clearDisplay();
	display.drawBitmap(
		(display.width()  - occhio_size[0] ) / 2,
		(display.height() - occhio_size[1]) / 2,
		occhio, occhio_size[0], occhio_size[0], WHITE);
	display.display();
}

void drawHoe() {
	display.clearDisplay();
	display.drawBitmap(
		(display.width()  - ferro_size[0] ) / 2,
		(display.height() - ferro_size[1]) / 2,
		ferro, ferro_size[0], ferro_size[0], WHITE);
	display.display();
}

void drawSplash() {
	display.clearDisplay();
	display.drawBitmap(
		(display.width()  - splash_size[0] ) / 2,
		(display.height() - splash_size[1]) / 2,
		splash, splash_size[0], splash_size[0], WHITE);
	display.display();
}

void drawDreaming() {
	display.clearDisplay();

	display.setTextSize(1);              // Normal 1:1 pixel scale
	display.setTextColor(WHITE);         // Draw white text

	display.setCursor(45, 15);             // Start at top-left corner
	display.println(F("Entering "));

	display.setCursor(10, 30);             // Start at top-left corner
	display.println(F("deep dreaming mode"));

	display.setCursor(58, 45);             // Start at top-left corner
	display.println(F("..."));

	display.display();

}


void showResult() {
	Serial.print(F("result: "));
	Serial.print(SmorfiaNumber);
	Serial.print(F(" - "));
	Serial.println(SmorfiaLabel);

	display.clearDisplay();

	display.setTextSize(1);
	display.setTextColor(WHITE);

	display.drawCircle(display.width() / 2, (display.height() / 2) - 13, 17, WHITE);

	display.setTextSize(2);

	calculateNumberSize(SmorfiaNumber);
	calculateLabelSize(SmorfiaLabel);

	//calculate cursor position to align the number to the center
	int cursorPosition_x=SCREEN_WIDTH/2-w_number/2;
	int cursorPosition_y=12;

	display.setCursor(cursorPosition_x, cursorPosition_y);
	display.println(SmorfiaNumber);

	//calculate cursor position to align the label to the center of the screen
	cursorPosition_x=SCREEN_WIDTH/2-w_label/2;
	cursorPosition_y=47;

	labelPosition=SCREEN_WIDTH;
	display.setCursor(labelPosition, 47);             // Start at top-left corner
	display.println(SmorfiaLabel);

	display.display();
}


void showIconsAnimation() {
	if (millis() - lastFrameChanged > changeFrameSpeed) {
		if (current_Frame < framesCount - 1) {
			current_Frame++;
		} else {
			current_Frame = 0;
		}

		switch (current_Frame) {
		case 0:
			drawHorns();
			break;
		case 1:
			drawEye();
			break;
		case 2:
			drawHoe();
			break;
		}
		lastFrameChanged = millis();
	}
}




void scrollScreenAnimation(){
	if (millis()-lastTImeScroll>updateInterval) {
		int16_t minXPosition=(w_label-30)* -1;

		if (labelPosition>minXPosition) {
			labelPosition-=4;
		}else{
			labelPosition=SCREEN_WIDTH;
		}
		Serial.print(minXPosition);
		Serial.print(F(" - "));
		Serial.println(labelPosition);


		display.fillRect(0, SCREEN_HEIGHT-20,SCREEN_WIDTH, 20, BLACK);
		display.setCursor(labelPosition, 47);             // Start at top-left corner
		display.println(SmorfiaLabel);

		display.display();

		lastTImeScroll=millis();
	}

}
