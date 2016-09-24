+++
date = "2012-01-22T11:21:05-08:00"
title = "Board design improvements"
+++



As I improve the [board design](/post/16258162053/board-sent-off-to-the-
factory) in my head, I think I can eliminate the EEPROM and downgrade the
ATmega to an ATtiny. The design will now read files off an SD card instead.
The ATtiny will populate a bank of the SRAM and present that to the 6809 as
ROM, using the CPLD as a stand-in for a [series of '595s](/post/16088202626
/this-is-getting-ridiculous-its-time-to-make-a). The 'tiny will also load the
FPGA, both from files on the SD card. I'm assuming that Xilinx FPGAs can be
loaded with SPI or something similarly pin-frugal. This feels like a better,
more modern approach. Moreover, I wasn't looking forward to reflashing the
EEPROM throughout development.

Also, an amendment to my component count estimate: I forgot about power. So we
need to add a few SOT-23 LDOs for the various voltages (1.8, 3.3, 5.0). But
it'll still be a very small board.

