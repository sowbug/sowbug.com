+++
date = "2012-01-24T11:20:05-08:00"
title = "digilent nexys 2 running through its demo program"
+++

 ![](/tumblr_files/tumblr_lyb76woCv71qly645o1_1280.jpg)  

[Digilent Nexys 2](http://digilent.org/Products/Detail.cfm?Prod=NEXYS2)
running through its demo program. I completed a VHDL
[tutorial](http://www.echelonembedded.com/fpgaresources/) last night that
displayed the hexadecimal version of the first four switches acting as bits.
The Digilent Linux tools aren't so great, at least compared to the screenshots
of the Windows tools, but they do work after a little prodding.

It's odd that Digilent would consider their USB firmware proprietary, leading
to a lot of [inefficient](http://www.hackdaworld.org/cgi-
bin/awki.cgi/NexysFPGA)
[effort](http://www.sensicomm.com/main/projects/fpga/digilent_nexys_usb.shtml)
on the part of various [Linux](http://braiden.org/?p=59) [hackers](http://ixo-
jtag.sourceforge.net/nexys2-linux-howto.html) to reverse-engineer it. What
exactly is Digilent protecting? It's a bootloader for a $150 low-end design
tool, big deal. Someone should build an FPGA board like this with an
ATmega32u4 as the USB frontend. It'll look like an Arduino Leonardo to the PC,
but it'll have super powers.

