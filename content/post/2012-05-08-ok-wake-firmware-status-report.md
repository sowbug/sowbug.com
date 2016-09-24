+++
date = "2012-05-08T08:53:56-07:00"
title = "OK Wake firmware, status report"
+++



I have the AVR and the PCF8523 communicating with each other, and the AVR is
mostly able to manipulate its own EEPROM. Things are at least a couple
bugfixes away from working end-to-end, though.

**Things I Learned Recently**

  * The RTC should be reset when the AVR starts up. It's far too easy to leave it with sticky state that causes known-good code to misbehave. Fortunately, resetting leaves the time and alarms intact, so it's nondestructive to do it regularly.
  * The ATtiny25 has frustrating support for I2C, a.k.a. TWI or two-wire mode. Yes, it has a USART that can do what I'll call hardware-assisted bitbanging of I2C, but the code to actually do that bitbanging uses up lots of program space. The combination of 8-pin AVR, I2C, and small program space is challenging. I think I can do it, but it might be smarter to switch to an ATtiny85 during development so I can add more diagnostics while debugging.
  * I was spending a lot of time trying to distinguish different reasons why my single interrupt was firing (button-press, /INT low for second interrupt or alarm) without communicating with the '8523\. The reason for the no-communication part was that the '8523 was unavailable within the interrupt (interrupts disabled = no I2C). This was a losing proposition. It was much easier to have the interrupt wake me up, exit the interrupt without doing any work, then ask the '8523 via SF/AF whether it wanted me awake. If yes, deal with that. If no, then it must have been the button. This approach is much more solid, and it's what the '8523 designers intended.
  * Doing development with a coin-cell-powered circuit means that your code might start acting weird if the coin cell approaches 1.8V. Better to power via a reliable supply during development.
  * Power pins and test points would have been a godsend on this ridiculously small board. I should have added a header for V+, GND, /INT, SDA, and SCL. Nice big 0.1"-spaced pins to attach logic probes.
  * Binary-coded decimal is a _**pain**_ to work with. This is the '8523's native number format. I am currently staying in packed BCD for all operations, which neutralizes the annoyance, except for doing time math, where I have to convert back to regular decimal. I need to think harder about whether there's a clever way to multiply/divide by 60 in native packed BCD.

