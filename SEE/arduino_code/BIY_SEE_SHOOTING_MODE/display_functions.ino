
void initScreen() {
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;); // Don't proceed, loop forever
  }
  display.clearDisplay();
  display.display();
  drawHorns();

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

  display.setTextSize(1);             // Normal 1:1 pixel scale
  display.setTextColor(WHITE);        // Draw white text

  display.setCursor(45, 15);            // Start at top-left corner
  display.println(F("Entering "));

  display.setCursor(10, 30);            // Start at top-left corner
  display.println(F("deep dreaming mode"));

  display.setCursor(58, 45);            // Start at top-left corner
  display.println(F("..."));

  display.display();

}

void show5() {
  display.clearDisplay();

  display.setTextSize(1);             // Normal 1:1 pixel scale
  display.setTextColor(WHITE);        // Draw white text

  display.drawCircle(display.width() / 2, (display.height() / 2) - 13, 17, WHITE);

  display.setTextSize(2);             // Normal 1:1 pixel scale
  display.setCursor(48, 12);            // Start at top-left corner
  display.println(F(" 5 "));

  display.setCursor(25, 47);            // Start at top-left corner
  display.println(F("La Mano"));

  display.display();
}

void show17() {
  display.clearDisplay();

  display.setTextSize(1);             // Normal 1:1 pixel scale
  display.setTextColor(WHITE);        // Draw white text

  display.drawCircle(display.width() / 2, (display.height() / 2) - 13, 17, WHITE);

  display.setTextSize(2);             // Normal 1:1 pixel scale
  display.setCursor(40, 12);            // Start at top-left corner
  display.println(F(" 17 "));

  display.setCursor(18, 47);            // Start at top-left corner
  display.println(F("La Sfiga"));

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
