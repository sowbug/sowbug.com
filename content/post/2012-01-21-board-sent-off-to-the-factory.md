+++
date = "2012-01-21T16:42:05-08:00"
title = "Board sent off to the factory"
+++



No, not the replacement for the [Mess O' Wires](/post/16180992985/address-and-
data-bus-lines-are-now-connected). This is the [Dangerous
Prototypes](http://dangerousprototypes.com/) [XC9500XL CPLD Breakout
Board](http://dangerousprototypes.com/docs/XC9500XL_CPLD_breakout_board). I've
ordered from [DorkbotPDX](http://dorkbotpdx.org/wiki/pcb_order), and my batch
should be going to the fab today. (As a side note, I don't feel too bad about
depriving DP of revenue. I own one of approximately every other thing they've
sold, and I couldn't wait for the many-week shipment time from
[SeeedStudio](http://www.seeedstudio.com/).)

As I investigate (naively) the capabilities of this device, I'm pretty sure I
ought to be able to duplicate all of Joust with the following:

  * A Xilinx Spartan of some kind to reproduce the main chips (6809E, two 6821s, a 6808 for sound, and the "special" SC2) and a lot of the glue among them.
  * One of these little CPLDs for things like the Q/E clock generator and other glue that might not fit on the Spartan. (Actually, I doubt it'll be necessary at all, but I'm rationalizing it now so I can start working on programmable logic before the Spartan arrives.)
  * An SRAM.
  * An EEPROM to hold the game code.
  * The 4MHz oscillator.
  * An ATmega of some kind to load up the Spartan and maybe manage resets.
  * A bunch of resistors for video, and capacitors for power decoupling.

Unless I'm missing something major, this will be a pretty tiny board, compared
to the original five Joust boards!

