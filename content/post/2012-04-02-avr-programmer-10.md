+++
date = "2012-04-02T08:43:00-07:00"
title = "AVR Programmer 1.0"
+++



Just sent off [DORKBOT_1_0](https://github.com/sowbug/avr-
programmer/zipball/DORKBOT_1_0) to Laen (yeah, we reuse version numbers around
here). Interesting changes:

  * Added an FTDI-cable-compatible header. This means the board has the hardware capability to do USB-TTL serial I/O, and it should be able to program Arduino Pros and other barebones Arduinos.
  * Dropped the two ground pins on the VCC/3.3/5.0 header. The original idea was to make it possible for that header to act as a small power source, but it turned out to be a confusing opportunity for short circuits.
  * Brought out the 4MHz emergency clock source that Dean's AVRISP source code already provides.
  * Brought out XCK. In theory, with a couple external resistors connecting TXO and RXI to form the DATA line, TPI/PDI programming will be possible.
  * Brought out two GPIO pins. They're buffered so they're output-only.
  * Switched from the '125 to a '241 to accommodate the extra outs.
  * Dropped the redundant pullup resistor on /RESET.
  * Added a solder jumper for /HWB so it's easier to get the board into bootloader mode.
  * Stopped sending MISO through the buffer. This was a curious design decision for USBtinyISP, and it also made ISP of the board itself more difficult than it should have been.
  * Switched to larger-than-microscopic labels. Maybe they'll be readable this time!

