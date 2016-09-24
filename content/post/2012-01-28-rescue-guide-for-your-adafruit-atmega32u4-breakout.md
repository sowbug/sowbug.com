+++
date = "2012-01-28T10:19:00-08:00"
title = "Rescue guide for your Adafruit ATmega32u4 breakout board"
+++



The [ATmega32u4 breakout
board](http://ladyada.net/products/atmega32u4breakout/) is a beta product. The
hardware is essentially perfect, but the firmware is wonky. At least once,
I've convinced myself that mine was broken, but I eventually figured it out.
Here's how to get yours back in shape.

Things required to get all the way through these steps:

  * The board
  * A USB cable to connect the board to your computer
  * A working copy of avrdude. If you have the Arduino IDE on your system, then it's buried deep inside the IDE.
  * _Possibly_ an in-system programmer. These instructions will work with any USBTiny-compatible programmer.

Before we get going, a warning: the
[fuses](http://www.ladyada.net/learn/avr/fuses.html) and the bootloader must
match, because the fuses tell the chip where the bootloader is. If you have
the Leonardo bootloader on your board, beware! That one uses a different fuse
combination (I think FCD5C3) from the Adafruit one (FCD0C3). Moreover, you
need the ISP to change the fuses; an ATmega32u4 unfortunately can't change its
own fuses. It's completely possible for you to flash the wrong bootloader to
the board, leaving it in a zombie state, needing the ISP to fix it. This means
that these steps might take you from a sort-of working board (e.g., an early
Leonardo bootloader) to one that's completely broken (the Adafruit bootloader
with the wrong fuses), and if you don't have an ISP to set the fuses, you'll
be stuck. **TL;DR: if you have a board that mostly works, and don't have an
ISP, then stop now.**

If your board is showing up as a serial device, we can learn a little from it
directly, without the ISP. Run **avrdude -c avr109 -p m32u4 -v -U lfuse:r:-:i
-U hfuse:r:-:i -U efuse:r:-:i -P
/dev/tty.usb_path_to_the_device_serial_port**. A bunch of information should
get spit out, ending with something like this:

`avrdude: safemode: lfuse reads as FC  
avrdude: safemode: hfuse reads as D0  
avrdude: safemode: efuse reads as C3  
avrdude: safemode: Fuses OK`

If you get an error, it's possible your board is running the Leonardo
bootloader, so you'll need to ask differently. Instead of **avr109** in the
previous command, try **arduino**.

Now you want to figure out what those fuses mean. Visit [Frank Zhao's AVR Fuse
Calculator](http://www.frank-zhao.com/fusecalc/fusecalc.php?chip=atmega32u4)
(in fact, you might want to set that as your home page) and type the three
into the "Current settings" fields at the bottom of the page. Apply values,
then go back up to the top of the page and see what the "Boot flash size"
dropdown is set to.

If the size is 2048, this is GOOD because it matches the size of the known-
good 2K-word (4096-byte) Adafruit build of the LUFA CDC bootloader. If this
size is anything else (probably 512, for the 1024-byte Leonardo bootloader),
then **stop unless you have an ISP because you need an ISP to change the
fuses**. If the size is not 2048 but you do have an ISP, **proceed to change
the fuses**.

To change the fuses, plug your board into your ISP and run **avrdude -v -c
usbtiny -p m32u4 -U lfuse:w:0xFC:m -U hfuse:w:0xD0:m -U efuse:w:0xC3:m**.
Again, skip this step if your boot flash size is already 2048. (Note that
these fuse values came from the [Adafruit BootloaderCDC
makefile](https://github.com/adafruit/Atmega32u4-Breakout-
Board/blob/master/makefile), but the F3 verifies as a C3 because not all 8
bits of the extended fuse are writable. Check out the [fuse
calculator](http://www.frank-zhao.com/fusecalc/fusecalc.php?chip=atmega32u4)
to see for yourself.)

Next, flash the one true bootloader that today is known to work:
[BootloaderCDC.hex](https://github.com/adafruit/Atmega32u4-Breakout-Board).
Run either of these commands, depending on whether your board is connected to
the ISP or directly to your machine:

Directly connected: **avrdude -c avr109 -p m32u4 -P
/dev/tty.usb_path_to_the_board_serial_port -U flash:w:BootloaderCDC.hex**

Connected to your ISP: **avrdude -c usbtiny -p m32u4 -U
flash:w:BootloaderCDC.hex**

Note that, unlike in the previous step, _**I am not**_ telling you to
substitute **arduino** for **avr109** in this step. That's because doing so
would kill your board and require the ISP to rescue it. If you wanted to
follow that step, it means you misunderstood the earlier steps about current
bootloader size.

By this point, you should have BootloaderCDC on your board, and fuses for a
2048-word bootloader. Plug the board via USB into your computer and press the
reset button. You should see the pulsing green light as well as a new serial
port on your computer. All should be well.

