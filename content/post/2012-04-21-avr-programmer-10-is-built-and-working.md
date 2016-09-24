+++
date = "2012-04-21T09:04:00-07:00"
title = "AVR Programmer 1.0 is Built and Working"
+++



![](http://67.media.tumblr.com/tumblr_m2u5baMHvi1qjj3vh.jpg)

The boards arrived from [Dorkbot](http://dorkbotpdx.org/wiki/pcb_order)
yesterday. I learned my lesson from last time and assembled all three in
parallel (taking the risk that the circuit was bad and that I'd waste 3x the
materials). I flashed the bootloader to the first one using the alpha version
of the board (in the back with the blue shunt), then self-programmed it over
USB with the [AVRISP mkII](http://www.fourwalledcubicle.com/LUFA.php)
firmware. Final test:

![](http://66.media.tumblr.com/tumblr_m2u5l9djG01qjj3vh.jpg)

I read the fuses from my [Hypna Go Go](/post/20906913903/the-hypna-go-go)'s
ATtiny13A, and I got the lovely `Device signature = 0x1e9007` that seems to
play a critical role in many dreams I recall nowadays. Success!

Bringing up the other two boards was a bit more difficult. The first would
program and would blink its bootloader status LED, but it wouldn't program. A
cold solder joint on the '32u2's core GND pin was the cause. The last board
was a more serious case: the '32u2 got hot when I plugged in the USB, and
other than being ISP-programmable, it was dead to the world. I never found the
short, but I did scrub off the flux more carefully, and I resoldered a couple
capacitors that looked slightly suspicious, and when I plugged it back in
again, it was fine.

Next steps:

  * Validate that the new HWBE jumper works.
  * Port over the [JTAG Whisperer](https://github.com/sowbug/JTAGWhisperer/).
  * Expose the USB-TTL serial functionality.
  * Fix a few layout issues (obscured labels, component placement that is inconvenient for assembly).
  * Switch to a version of the USB socket that has pegs. I can already tell a high-use application like this is going to need a little more strength than just SMD solder pads.
  * Replacement of the current-limiting resistor on the LED. Someone please remind me why I picked 1K ohms. My gorgeous purple LEDs are hardly visible!

**(Update: [linked to this post](http://redd.it/sle0a) on Reddit.)**

