+++
date = "2012-04-25T09:01:54-07:00"
title = "Hello World on STM32F4 Discovery"
+++



I got a blinking LED (the embedded Hello World) on my [STM32F4
Discovery](http://www.st.com/internet/evalboard/product/252419.jsp) board. It
probably would have been easy to do, except that I was on OS X. Here are the
steps I took:

  1. Tried a bunch of stuff.
  2. Switch to Linux.
  3. Tried a bunch more stuff.
  4. Took a break.
  5. Found this [extremely correct page](http://www.triplespark.net/elec/pdev/arm/stm32.html), which helped me build a real ARM toolchain.
  6. Built [stlink](https://github.com/esden/summon-arm-toolchain).
  7. Built some of the stlink samples.
  8. Got gdb going with the stlink gdbserver.
  9. Stepped through some code in RAM (not flashed).
  10. Using the stlink flash utility, flashed code I built to the board. Unplugged it and plugged it back in to confirm the code was still there.
  11. Flashed back the "Discovery" sample shipped with the board.

From this adventure I can confirm that summon-arm-toolchain does work if you
switch to the dev branch, and that the ARM version of gdb really and truly
allows interactive debugging on this tiny little dev board. Quite a step up
from the AT90S4433 and early avr-gcc toolchain that I first started hacking on
back in 2002.

