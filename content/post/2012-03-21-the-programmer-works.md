+++
date = "2012-03-21T09:00:06-07:00"
title = "The programmer works!"
+++



![](http://66.media.tumblr.com/tumblr_m17r107BVZ1qjj3vh.jpg)

The boards tagged [DORKBOT_1_0_1](https://github.com/sowbug/avr-
programmer/tags) arrived on Monday. I'd somehow forgotten to order the
NX8045-package crystals, so I had to solder a temporary, silly-looking HC49
crystal onto the board. But otherwise, assembly went fairly smoothly.

I followed the usual order of PCB population: add the power circuitry first,
then power it up and read testpoints. All was fine. Then the "expensive"
(i.e., two-dollar) parts: the '32u2, the buffer, and the sockets. More
continuity testing, some examination under the USB microscope for solder
bridges… and then fingers crossed while I plugged it in to USB.

![](http://67.media.tumblr.com/tumblr_m17ra8fDkJ1qjj3vh.jpg)

Success! Or at least, as much success as I could detect at this point, which
is to say I didn't smell smoke.

I first connected it to my USBtiny and read the default fuses ([5e d9
f4](http://www.frank-
zhao.com/fusecalc/fusecalc.php?chip=atmega32u2&LOW=5E&HIGH=D9&EXTENDED=F4&LOCKBIT=FF)),
then tried changing the lfuse to use the internal oscillator (**avrdude -c
usbtiny -p m32u2 -P usb -U lock:w:0x3F:m**). No luck; avrdude kept reporting
"verification error; content mismatch," and the fuse stayed as-is. I ended up
looking at some other avrdude command-line invocations on the web and realized
that (1) the lock fuse had been preset to disallow further programming, and
(2) I had to erase the chip with a -e flag to undo that fuse. Achievement, and
fuse, unlocked.

Next, installing the bootloader. I built LUFA's CDCBootloader, then wrote it:
**avrdude -c usbtiny -p m32u2 -P usb -v -e -U flash:w:BootloaderCDC.hex** (by
this point I think the -e was implied, but I spelled it out anyway). I then
disconnected the USBtiny, plugged the programmer into USB, and saw
/dev/tty.usbmodemfa121! My programmer was running code!

Finally, making the programmer a programmer. I built the LUFA AVRISP mkII
clone, then wrote it (**avrdude -p m32u2 -P /dev/tty.usbmodemfa121 -c avr109
****-U ****flash:w:AVRISP-MKII.hex**). The serial device vanished, as
expected. My computer's System Information informed me that an AVRISP mkII had
just joined us, and I was able to read from and write to a target 328p on an
[Evil Mad Science breakout
board](http://evilmadscience.com/productsmenu/tinykitlist/74-atmegaxx8).

I now know that feeling one feels when a fabbed circuit works on the first
shot. The feeling is mostly surprise… and mostly delight.

P.S. Will someone please tell me why I've been wasting my time using anything
but [CrossPack](http://www.obdev.at/products/crosspack/)?

