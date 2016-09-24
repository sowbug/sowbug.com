+++
date = "2012-09-10T23:18:12-07:00"
title = "Like A G35 v1.0 is at Laen's!"
+++



Just submitted the design to the fancy new [OSH Park](http://oshpark.com/)
site. This is my first time using the site since Laen turned the Dorkbot PDX
service into it. The site has a bug or nit here or there, but the previewing
feature is very nice.

As expected, I ditched the RTC feature. But I kept the IR receiver. There are
terminal blocks for three G35 strands, up to three independent WS2801 strands,
and ample power for all passed directly through the fuseless micro-USB power-
only connector. How many lights the Arduino processor itself can drive remains
to be seen. The board is completely passive; there isn't even a capacitor on
it. The major challenge was making sure everything fit without bumping on the
metal USB jacket of pre-Leonardo Arduinos.

The [EAGLE files](https://github.com/sowbug/like-a-g35) are on GitHub.

