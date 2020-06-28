#include <SPI.h>
#include "SH1106_SPI.h"

#define USE_FRAME_BUFFER

#ifdef USE_FRAME_BUFFER
SH1106_SPI_FB lcd;
#else
SH1106_SPI lcd;
#endif

void setup(void)
{
	Serial.begin(9600);
	lcd.begin();
	lcd.print(F("Mobiiiina"));
#ifdef USE_FRAME_BUFFER
	lcd.renderAll();
#endif
}

void loop(void) 
{
	
}
