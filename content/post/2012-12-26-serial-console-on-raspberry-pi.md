+++
date = "2012-12-26T19:20:00-08:00"
title = "Serial console on Raspberry Pi"
+++



If you have a
[CP2102](http://www.silabs.com/products/interface/usbtouart/Pages/usb-to-uart-
bridge.aspx)-based USB-to-serial adapter, it's very likely to use 3.3-volt
logic levels that are safe for your [Raspberry
Pi](http://www.raspberrypi.org/). I reviewed the datasheet for the chip, and
any normal circuit using it would use the internal 3.3-volt regulator powered
by the 5-volt USB bus, meaning that the I/O levels will be relative to Vdd
(i.e., 3.3 volts).

A recap of an [excellent tutorial](http://www.element14.com/community/groups
/raspberry-pi/blog/2012/07/18/look-ma-no-display-using-the-raspberry-pi-
serial-console) explaining how to get a serial console on your Pi:

  1. Hold your **unplugged** Pi so the GPIO header is close to you on the right side of the board, pointing up.
  2. Connect the TXD pin of your adapter to the fifth pin from the right on the closest row to you.
  3. Connect the RXD pin to the fourth pin, right next to the other one. So when you look at your Pi, you should see the yellow RCA jack in the middle, then to the right of that eight empty pins, then TXD, then RXD, then three empty pins.
  4. On your real computer, fire up a serial terminal and connect at 115200 bps. On my Mac, that's **screen /dev/tty.SLAB_USBtoUART 115200**.
  5. Plug in your Pi, but read this whole step first. I powered mine from my desktop computer's USB port, so I knew both machines were sharing ground. If you're plugging in your Pi from another power source, there's a chance it won't work because the two machines will have a different ground.
  6. You should see the kernel boot output appearing on your terminal. After a bit you'll get the Pi's login prompt, almost as if you were sshing into it.

**Update**: If you make it as far as the login prompt but see inverted diamonds with question marks and can't type in the username, you probably have the flow-control settings wrong. [According to elinux.org](http://elinux.org/RPi_Serial_Connection), the default UART settings use no flow control. To fix this on Ubuntu, I installed minicom, then navigated to its serial-port settings and turned off hardware flow control (which was on). This fixed things for me. You can probably use stty to change the settings without using minicom.

