+++
date = "2012-05-25T08:54:00-07:00"
title = "New Project: Like A G35"
+++



Last year I took some good work by [Robert Sun
Quattlebaum](http://www.deepdarc.com/2010/11/27/hacking-christmas-lights/) and
others and made an [Arduino library](https://github.com/sowbug/G35Arduino)
that controls GE G35 Color Effects Christmas lights. For the 2011 season I
whipped up a quick perfboard using a [Teensy](http://pjrc.com/teensy/), and
since then I've wanted to build a more permanent board that I might leave up
year-round; after all, plenty of evenings call for fancy lighting. Why let
Christmas have all the fun?

Thus, a few days ago I started my latest project: [Like A
G35](https://github.com/sowbug/like-a-g35). It isn't much at the moment, but
if I start prototyping now (in May), it ought to be ready to go by the time I
want to deploy it (Halloween at the latest).

The circuit will be my first based on the ATmega32U4. I've worked on that chip
quite a bit via [Adafruit's breakout
board](http://www.ladyada.net/products/atmega32u4breakout/), but I've never
gotten around to a build with it. It'll be fairly simple:

  * Micro-USB socket for programming and power.
  * ISP6 header for initial programming (remember, the '32U4 isn't available in DIP).
  * Three 3-position terminal blocks to support up to three strands of lights.
  * A second two-position terminal block for alternate power.
  * A beefy voltage regulator (at least 6 amps if I want to support three strands).
  * An infrared receiver to change programs.
  * A PCF8523 real-time clock with battery backup to display different programs depending on time of year.
  * Pinouts for whichever GPIO pins are left on the chip.

In all likelihood I'll solder only the USB socket, the '32U4, and two of the
terminal blocks, because I have only two strands on my house, I prefer to
power directly through USB, and I won't get around to any RTC or remote
functionality. But in case other people want to build the board and use it for
other purposes, it'll be nice to have those other features optionally
available.

