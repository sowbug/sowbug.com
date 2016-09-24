+++
date = "2012-01-29T11:22:05-08:00"
title = "The JTAG Whisperer"
+++



Available [here on GitHub](https://github.com/sowbug/JTAGWhisperer). The JTAG
Whisperer turns your Arduino into a JTAG cable. **Wow, sounds great!** Here
are the caveats:

  * It's actually just an XSVF player. This is a tiny subset of what [JTAG](http://en.wikipedia.org/wiki/Joint_Test_Action_Group) does. The current architecture has the desktop load the XSVF file, then send it over serial to the Arduino. Since serial is going to be limited to the kilobits-per-second range of speed, it's unlikely it'll be suitable for more ambitious interactive JTAG operations. But it'd be interesting to see what could be accomplished with the newer Arduinos that have replaced the FTDI chip with the more flexible ATmega U-series chips.
  * It has been tested only on a [Xilinx XC9572XL breakout board](http://dangerousprototypes.com/docs/CPLD:_Complex_programmable_logic_devices) from Dangerous Prototypes, and the only function it has performed so far is asking the chip its device ID (spoiler: it's 0xf9604093). I would have happily used the [Bus Pirate's XSVF Player firmware](http://dangerousprototypes.com/docs/Bus_Pirate), but it hasn't yet been ported to my BPv4 hardware, and I wasn't willing to invest in learning PIC development.
  * It doesn't work very well yet. The serial communication between the desktop and the PC frequently gets logjammed, and the Arduino sometimes has to ask repeatedly for the ID.

I have high hopes for this project. Its immediate use will be to program the
'9572 so that I can start experimenting with replacing discrete logic 74xx
chips. Eventually I hope it'll become a robust, reliable XSVF player for the
Arduino.

Please [give it a try](https://github.com/sowbug/JTAGWhisperer). I look
forward to your pull requests!

