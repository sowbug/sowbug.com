+++
date = "2012-09-23T09:01:00-07:00"
title = "Arduino sketch for WS2801-non-clone SM16716"
+++



I got a strand of 50 LED lights from "someone in China." They were advertised
as being WS2801-based, but they didn't work with Arduino sketches for that
chip.

So now I have a 49-light strand, a sacrificial light that I had to rip apart
to find the chip identifier ("SM16716"), and [an Arduino
sketch](https://github.com/sowbug/sm16716) that proves that they work. Thank
you, Google Translate, for help with the Chinese-only datasheet for the 16716.

![](http://67.media.tumblr.com/tumblr_mat8hnaDe51qjj3vh.jpg)

By the way, there is a probably great library,
[FastSPI](http://code.google.com/p/fastspi/), that supports many chipsets
including the 16716. Unfortunately, it just didn't work for my Uno/strand
combination, and I'm not sure why (the code looks right). I'll probably debug
that code and submit a patch.

