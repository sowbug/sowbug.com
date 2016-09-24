+++
date = "2012-01-20T11:20:05-08:00"
title = "address and data bus lines are now connected"
+++


![](http://66.media.tumblr.com/tumblr_lxx8dcu2kK1qly645o1_1280.jpg)  

Address and data bus lines are now connected between the '595s and the SRAM.
The breadboard has gotten unworkable. It's time to take a different approach.
Choices:

  * Move to protoboard and do permanent wiring underneath with headers on top for further experimentation.
  * Split out into two or more breadboards with ribbon connectors between them. This isn't actually any better than what I have now, but it'd be a chance to refactor the wiring and IC arrangement.
  * Fire up EAGLE and redo the circuit as a schematic, then route it and ship it off to be manufactured, maybe by [DorkbotPDX](http://dorkbotpdx.org/wiki/pcb_order) if the timing works out right and I'm patient, or somewhere else if I want to spend more money and get it faster.
  * Sit and wait for the Papilio One to arrive (which I ordered a couple weeks ago), and in theory enjoy working mostly in software until I run into BRAM limits.

