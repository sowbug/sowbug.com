+++
date = "2012-02-16T14:03:05-08:00"
title = "a very early and surely broken board layout on"
+++


![](http://67.media.tumblr.com/tumblr_lzf4slUlMb1qly645o1_1280.png)  

A very early and surely broken board layout. On the left are the power jack,
USB port, and micro-SD slot. The socketed chip in the middle is the SRAM, and
the one on the right is the 6809E. The middle guys are the CPLD, an
ATmega32u4, and the frickin' huge oscillator that I will no doubt replace with
an SMD version. A friend has graciously offered to do the layout for real, so
I'm not too concerned about the ugly EAGLE autoroutes. I just want to get an
idea of how big the board will be.

Known errors in this version:

  * There's no JTAG header. I intend to program the CPLD with the ATmega, but I'd like a backup plan.
  * I might want to consider a fuse. This isn't a general-purpose board with wildly varying current needs or likelihood of short-circuits, but still, it'd be smart.
  * There's no circuitry to choose between USB and jack power sources. I'm OK with this; if I plug in both simultaneously, I deserve the consequences.
  * I phoned in the capacitor placement. I will read the datasheets and take their advice.
  * As-is, any SD card placed in the board would burn up. Voltage-dividing resistors between the 5V '32u4 and the 3.3V card signals are needed.
  * Like the oscillator, the SRAM could be switched to an SMD version. Only the 6809E is unavailable as an SMD.

Missing functionality:

  * Video.
  * Sound.
  * Game inputs.
  * Anything that could even theoretically serve as the Williams Special Chip.
  * Header sockets for a future stacked board that will eventually contain all of the above.

But this is OK. As long as I add the headers, this will serve as a fairly
functionally complete 6809E-based computer with persistent storage, huge DRAM,
huge ROM, and… virtually no way to demonstrate that it's doing anything at all
except through a logic analyzer or maybe [Quinn's HexOut
tool](http://quinndunki.com/blondihacks/?p=610). Again, this is OK. I'll add
the second stackable board, and that's when it'll start to do cool stuff.

Parting thought: if the SRAM is an SMD, the 6809E is rotated 90 degrees, and
things are scrunched together as closely as possible, then it's starting to
look a lot like a very special-purpose Arduino shield. The Arduino would
replace the ATmega, the crystal, the power circuitry, and the ISP header. That
saves a _lot_ of room on the board. In fact, it might even leave room for v2
to have everything from the missing-stuff list. Hmmm.

