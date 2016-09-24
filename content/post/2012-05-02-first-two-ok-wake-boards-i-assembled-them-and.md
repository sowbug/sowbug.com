+++
date = "2012-05-02T08:07:42-07:00"
title = "first two ok wake boards i assembled them and"
+++


![](http://67.media.tumblr.com/tumblr_m3bws8oKA11qly645o1_1280.jpg)  

First two [OK Wake](/post/21150945583/ok-wake) boards. I assembled them and
wrote a quickie program to test that everything was wired up properly. I
haven't yet run the PCF8523 real-time clock through its paces, but everything
else is working properly.

This board is going to require some nontrivial firmware, and I haven't ever
worked with I2C (or the generic-brand TWI, or two-wire interface) on an AVR,
which means this is going to be a significant opportunity to learn. Because I
didn't have the space for an ISP header, I'll probably develop most of the
firmware on an Arduino or Adafruit '32u4 breakout board to avoid having to
constantly unplug the ATtiny25. That will speed up development time, I hope.

I did make one mistake in this circuit. I had a half-baked idea that a 10uF
capacitor could power the RTC during battery changes. I have absolutely no
basis for my belief that that capacitor is large enough to power the RTC
during the 30 seconds it'd take to change the battery, but even if it were, I
neglected to put a diode in the circuit to stop the ATtiny from quickly
draining the capacitor. This probably means that changing the battery will be
disruptive. Fortunately, I expect the lifetime of the battery to exceed the
useful lifetime of the board (remember, this is for a friend's children who
aren't yet old enough to read a clock but are likely to respect a color-coded
admonition to stay in bed, and I'm sure that in a year they'll have grown out
of that phase).

