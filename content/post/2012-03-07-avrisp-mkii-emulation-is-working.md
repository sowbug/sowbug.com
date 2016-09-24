+++
date = "2012-03-07T14:00:06-08:00"
title = "AVRISP mkII emulation is working"
+++



Using my USPtinyISP, I burned the LUFA CDC bootloader to my 32u4. Then I
bootloaded [Dean](http://fourwalledcubicle.com/)'s LUFA-based AVRISP mkII-
compatible ISP firmware onto it. Finally, I used the 32u4 masquerading as a
mkII to read and set fuses on an ATtiny13a.

What does this mean? It means that when the AVR programmer boards arrive from
Laen, I ought to be able to quickly build basic firmware for them. Exciting!

