+++
date = "2012-03-10T14:00:00-08:00"
title = "XMEGA Breakout Board"
+++



(Yes, apparently Atmel spells it in all caps.)

Because the [AVR Programmer](https://github.com/sowbug/avr-programmer) will
support SPI-based ISP, PDI for XMEGAs, and TPI for low-end 'tinys, I need to
acquire test targets of each kind. Unfortunately, XMEGA isn't available as a
DIP, which means it's breakout board time.

I've made a half-hearted resolution to design and build rather than buy tools
where possible, because, well, because building is fun. That rules out buying
the [SparkFun board](http://www.sparkfun.com/products/9546) and Atmel's own
[XPLAIN series](http://www.atmel.com/xplain) (even though the Atmel boards are
pretty reasonably priced for all the bells and whistles they include). But I
can still build on others' work. Current influences for my design:

  * David Watson's [Xmega 4 breakout](http://david.neonquill.com/projects/xmega_breakout/). OSHW, and pretty good-looking for a homemade prototype (Laen's deep purple boards always help with the aesthetics). But it's missing USB and a voltage regulator, which I'd really prefer to lower the cable count on my desk.
  * Batsocks' [BreadMate XMega](http://www.batsocks.co.uk/products/BreadMate/XMega%20PDI.htm). Pretty much perfect; gives you that "ooh I want it" feeling that you also get when you see the [Teensy](http://www.pjrc.com/teensy/). But like the Teensy, it's not OSHW, so I can't really do anything with it. (I'd have been happy to buy at least one if the source were provided.) **Update 5/23/2012: Nigel has open-sourced the USB version of the project. As promised I've bought one; it's on its way from Batsocks now!**
  * [brendan0powers' board](http://dangerousprototypes.com/forum/viewtopic.php?t=3527&p=35454). This board mostly confirms that I want to steer clear of QFN. It has a good feature set (USB, vreg, missing a crystal).

I want David's layout, Brendan's USB, no FTDI header, and Batsocks'
manufacturing chops. EAGLE, here I come!

