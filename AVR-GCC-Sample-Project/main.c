/**
 * @Author: @IamRezaMousavi
 * @Date:   2022-07-19 00:50:46
 * @Last Modified by:   @IamRezaMousavi
 * @Last Modified time: 2022-10-20 19:25:35
 */

#ifndef __AVR_ATmega16__
  #define __AVR_ATmega16__
#endif

#define F_CPU 1000000UL

#include <avr/io.h>
#include <util/delay.h>

int main(void) {
  // Input/Output Ports initialization
  // Port A initialization
  // Function: Bit7=Out Bit6=Out Bit5=Out Bit4=Out Bit3=Out Bit2=Out Bit1=Out
  // Bit0=Out
  DDRA = (1 << DDA7) | (1 << DDA6) | (1 << DDA5) | (1 << DDA4) | (1 << DDA3)
         | (1 << DDA2) | (1 << DDA1) | (1 << DDA0);
  // State: Bit7=0 Bit6=0 Bit5=0 Bit4=0 Bit3=0 Bit2=0 Bit1=0 Bit0=0
  PORTA = (0 << PORTA7) | (0 << PORTA6) | (0 << PORTA5) | (0 << PORTA4)
          | (0 << PORTA3) | (0 << PORTA2) | (0 << PORTA1) | (0 << PORTA0);

  while (1) {
	PORTA = ~(PORTA);
	_delay_ms(250);
  }
}
