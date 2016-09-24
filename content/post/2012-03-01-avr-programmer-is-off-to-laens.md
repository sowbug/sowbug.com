+++
date = "2012-03-01T14:04:06-08:00"
title = "AVR Programmer is off to Laen's!"
+++



I reached a good 1.0 stopping point, so I poured the ground planes, fired up
the CAM processor, churned out the gerbers, and emailed 1.46 square inches of
high functionality to [Laen's](http://dementeddiode.org/blog/) [DorkbotPDX PCB
service](http://dorkbotpdx.org/wiki/pcb_order)!

![](http://67.media.tumblr.com/tumblr_m06vseaaRE1qjj3vh.png)

Many thanks to DG who manually routed a interim version of the board, and
shaved off all but four vias and about a half square-inch of PCB.
Unfortunately I made a few more enhancements and added 14 more vias in the
process. Here's the current feature set:

  * ATmega8u2, 16MHz
  * Will program any ISP6-capable AVR
  * Will play XSVF via JTAG headers
  * Powered by USB
  * Mini-USB connector
  * Buffered I/O
  * Requires no 6-pin cable
  * Will power the target board at 5V (about 450mA) or 3.3V (about 100mA)
  * Target board can also be self-powered
  * I/O logic levels will always match target VCC (unless user does something silly)
  * Optional self-programming header
  * Optional secondary ISP6 header if you _really_ want to use a cable, or need to connect to an ISP10 board, or just want to hack hard on the 8u2 and prefer flying leads.

At this point all I can truly say is that _the hardware doesn't rule out any
of this functionality._ I haven't written the software yet, so the board
doesn't actually do anything. But it will.

[Watch the project](https://github.com/sowbug/avr-programmer) on GitHub! And
if you're interested in a prototype of the board, let me know!

