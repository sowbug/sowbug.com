+++
date = "2012-02-01T11:20:06-08:00"
title = "More than you ever wanted to know about electrical characteristics of JTAG"
+++



A few days ago I posted a [very confused question](/post/16730593812/jtag-tck-
active-low) about JTAG signals. Here is my less confused answer.

![Cup or
Face?](http://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Cup_or_faces_paradox.svg
/300px-Cup_or_faces_paradox.svg.png)

You've surely seen the cup-or-face picture before, where some see two people
looking at each other, and others see a single white chalice in the middle.
Both groups are correct, and fortunately everyone can easily tell their brains
to see the other image, too. That's what happened with me and JTAG signals. I
saw this:

  1. Write TDI/TMS.
  2. Set TCK.
  3. Wait.
  4. Clear TCK.
  5. Wait.
  6. Read TDO.

And the code I originally wrote probably would have worked just fine like
this. But it didn't, so I scoured the web looking for working examples (none
of which was both working and targeted toward the Arduino, unfortunately).
Most were some variation of this:

  1. Read TDO, write TDI/TMS.
  2. Clear TCK.
  3. Set TCK.

Which seemed to be out of whack with the spec (if not the spec then
[XAPP058](http://www.xilinx.com/support/documentation/application_notes/xapp058.pdf)).
I conformed my code; it still didn't work. I permuted the bit-banging code
madly. It still didn't work. I found subtle logic bugs that didn't matter,
because it still didn't work after I fixed them. I was ready to see five
fingers when [O'Brien](http://en.wikipedia.org/wiki/1984) held up his hand.

As you already know from prior entries, the [voltage
fiasco](/post/16828497482/5-0-3-3) was the answer. My code would never have
worked with the hardware running at 5 volts instead of the required 3.3. But
in my experience, the nice thing about debugging code in an impossible
situation is that by the time you figure out and solve the thing that was
making it impossible, _the rest of the code is absolutely perfect_ because
you've debugged the living daylights out of it.

Now that I have working hardware and have been able to run some experiments,
I've started seeing the cup instead of the faces. It's not that TCK's signals
are inverted (active-low); it's that the master divides the work into two
categories:

  1. Stuff I care about.
  2. Everything else.

Its job is to write out TDI/TMS before TCK goes high, and to read TDO after
TCK goes low. But it's OK for the work relative to TCK's edges to overlap. For
example, I can write TDI, then clear TCK, then set TCK, because _TDI was still
set before TCK's rising edge_. It just looks weird because it seems like the
code is saying "set TDI before TCK's _**falling**_ edge." Nope, TDI and TCK's
falling edge have absolutely nothing to do with each other. Taking the
transitive closure of dependencies, yes, TDI and TCK's falling edge are
related in the sense that TCK's rising edge comes before its falling edge, but
other than that, the code is free to rearrange itself in a sensible fashion as
long as it respects those constraints. (There is one timing characteristic,
TDOXZ, that I am still convinced is a typo in XAPP058.) Taking out the "wait"
steps from the original sequence, looking at it as a circle rather than a line
of steps, and reordering slightly in that "sensible fashion," it ends up like
this:

  1. Read TDO and write TDI/TMS, in any order.
  2. Set TCK.
  3. Clear TCK.

… which is exactly what most implementations on the web do. _QED_.

