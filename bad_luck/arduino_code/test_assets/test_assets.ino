/*********************************************************************
This is an example for Adafuit's Monochrome OLEDs based on SSD1306 drivers
  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/category/63_98
This example is for a 128x64 size display using I2C to communicate
3 pins are required to interface (2 I2C and one reset)
Adafruit invests time and resources providing this open source code, 
please support Adafruit and open-source hardware by purchasing 
products from Adafruit!
Written by Limor Fried/Ladyada  for Adafruit Industries.  
BSD license, check license.txt for more information
All text above, and the splash screen must be included in any redistribution
*********************************************************************/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);






void setup()   {                
  // On my display, I had to used 0x3C as the address, something to do with the RESET not being
  // connected to the Arduino. THe 0x3D address below is the address used in the original
  // Adafruit OLED example 
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);  // initialize with the I2C addr 0x3D (for the 128x64)
  
  display.clearDisplay(); // Make sure the display is cleared
  // Draw the bitmap:
  // drawBitmap(x position, y position, bitmap data, bitmap width, bitmap height, color)
 // display.drawBitmap(0, 0, logo, 108, 40, WHITE);

  // Update the display
  display.display();
}


void loop() {
  drawDreaming();
}


void drawDreaming() {
  display.clearDisplay();

  display.setTextSize(1);             // Normal 1:1 pixel scale
  display.setTextColor(WHITE);        // Draw white text 

  display.drawCircle(display.width()/2, (display.height()/2)-13, 17, WHITE);

  display.setTextSize(2);             // Normal 1:1 pixel scale
  display.setCursor(48, 12);            // Start at top-left corner
  display.println(F(" 5 "));

  display.setCursor(25, 47);            // Start at top-left corner
  display.println(F("La Mano"));

  display.display();
}
