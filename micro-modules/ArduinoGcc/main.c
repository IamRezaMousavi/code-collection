/**
 * @Author: Reza Mousavi
 * @Date:   2026-07-07 16:42:43
 * @Last Modified by:   Reza Mousavi
 * @Last Modified time: 2026-07-07 17:25:21
 */

#ifndef __AVR_ATmega328P__
#define __AVR_ATmega328P__
#endif

#ifndef F_CPU
#define F_CPU 16000000UL
#endif

#include <avr/io.h>
#include <util/delay.h>

int main(void) {
  // Bitwise OR to set register bit to 1 which sets the pin as output
  DDRB |= (1 << PB5); // Set PB5 (Arduino pin 13) as output
  // Loop forever. This is equivalent to the Arduino loop() function
  while (1) {
    // Bitwise OR to set register bit to 1 which sets the pin high
    PORTB |= (1 << PB5); // Equivalent to digitalWrite(13, HIGH);
    _delay_ms(3000);
    // Bitwise AND with NOT to set register bit to 0 which sets the pin low
    PORTB &= ~(1 << PB5); // Equivalent to digitalWrite(13, LOW);
    _delay_ms(1000);
  }

  return 0; // This line is never reached, but it's good practice to include it
}
