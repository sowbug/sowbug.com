+++
date = "2012-03-18T14:00:06-07:00"
title = "RPio Prototype #1 sent to the fab!"
+++



![](http://67.media.tumblr.com/tumblr_m134vtMPC01qjj3vh.png)

We fixed one huge issue where we were sending the I2C pins through the
TXB0108, which would have ruined them except as GPIOs. Instead we're leaving
them as 3.3-volt I/O, but pulling them up to 4.7K, which should work for most
practical purposes. After that fix and a little more routing magic, it was
time to send them off to [Dorkbot](http://dorkbotpdx.org/wiki/pcb_order)!

We've gotten requests for a couple dozen RPios, which is a good sign
considering that we haven't tried too hard to spread the word, and especially
considering that nobody has received a Raspberry Pi yet. We're thinking about
how to accelerate the prototyping turnaround time (either making our own PCBs
or paying more for quicker fabrication), so that we can get real production
versions in your hands soon after you get your RPi. Stay tuned for ordering
information!

