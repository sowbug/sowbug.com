+++
date = "2012-05-03T09:13:07-07:00"
title = "OK Wake as its own breakout board"
+++



![](http://66.media.tumblr.com/tumblr_m3dj6d2Yz91qjj3vh.jpg)

I am not usually this smart. I was fretting about how to get accessible
pinouts to the tiny SOIC-8 PCF8523 while developing the OK Wake firmware on an
Arduino. I thought about dead-bug wires, or picking up an SOIC breakout board
from a local store, or doing something ugly with perfboard. I briefly explored
repurposing an old unpopulated PCB, like maybe the third Hypna Go Go PCB from
Laen, which uses an SOIC-8 for its ATtiny13a.

Then I realized that the OK Wake itself was the perfect board! Just connect
the ATtiny socket's pins to the corresponding pins on the big brother Arduino.
That's what I did, and it's working very nicely. And as a bonus, I didn't have
to sacrifice any PCBs or extra PCF8523s.

Kind of obvious in retrospect. But in mental cycles expended, I definitely
earned it.

**[Update from a couple hours later] **I've successfully done the following:

  * Using the Arduino's Wire I2C library, read the seconds from the '8523 and confirmed that they increment properly.
  * Turned off the CLKOUT default settings, which were messing up /INT.
  * Set SIE, which enables the once-a-second interrupt on /INT.
  * Configured TAM to pulse the /INT interrupt so I don't have to clear it.
  * Confirmed with my logic analyzer that the pulse is indeed 1/64 seconds long.
  * Got the Arduino firing an interrupt routine when /INT goes active.
  * Confirmed that the button and the '8532 /INT signal don't interfere with each other.

In other words, unless the ATtiny is weirdly different from the '328, then the
circuit is in perfect working order.

