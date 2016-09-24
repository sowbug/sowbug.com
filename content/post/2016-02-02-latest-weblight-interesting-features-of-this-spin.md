+++
date = "2016-02-02T10:58:41-08:00"
title = "latest weblight interesting features of this spin"
+++


![](http://67.media.tumblr.com/c5b0788ceaab574c40cab4e5dcb8064c/tumblr_o1xopt63tL1qly645o1_1280.jpg)  

Latest [WebLight](https://github.com/sowbug/weblight).

Interesting features of this spin are that it’s 2.0mm thickness (still a
little thin but operational), and two-sided ([thanks to Passerby for circuit
tip](http://electronics.stackexchange.com/questions/209941/two-sided-
connectorless-usb-on-a-pcb/209949)).

There are two bugs. One, the board was too wide. I forgot to resize it after
removing the metal connector from the layout. So I filed down the edges around
the USB connector, and it’s fine. Two, part of the top ground plane got
disconnected from the rest, so the left LED’s ground is floating. Weirdly
enough, it works fine, except that it can’t communicate reliably with the
right LED, so the right LED flickers. A bodge wire fixed that, and if I
manufacture any more from this batch of boards, I think I can run that wire
underneath the LED assemblies.

Except for the two errors, which are now fixed in the latest layout, I think
this version could be the one that gets produced at scale.

