﻿+++
date = "2012-01-18T16:44:05-08:00"
title = "this is getting ridiculous its time to make a"
+++


![](http://65.media.tumblr.com/tumblr_lxvmzg7w9E1qly645o1_1280.jpg)  

This is getting ridiculous. It's time to make a PCB or move to FPGA, because
I'm running out of breadboard space. On the near side of the breadboard are
three '595s, forming serial-to-parallel address and data latches to load up
the SRAM. The data '595 is leftmost, the low byte of the address is in the
middle, and the high byte is on the right. To the right of the third '595 is
another ATtiny13a (my first project with two AVRs in a single circuit!). It's
latching the bits into the '595s, telling them it's OK to copy their registers
to the outputs, and then when the three bytes are ready, setting a strobe
signal that will tell the SRAM to use the address/data values to set a byte in
itself. The two halves of the breadboard don't talk to each other yet. Next
step is to hook the '595s to the SRAM.
