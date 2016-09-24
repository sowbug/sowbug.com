+++
date = "2012-01-26T11:20:05-08:00"
title = "Found a good base for an XSVF player"
+++

 [Found a good base for an XSVF player](https://github.com/ben0109/XSVF-
Player)  

Small world. Ben over at the [Papilio
Forums](http://www.gadgetfactory.net/gadgetforum/index.php?topic=277) had
almost the same needs as mine: wants to program an XC9572XL, prefers not to
buy overpriced, single-purpose cables. So he adapted the XAPP058 reference
code to a Papilio, cleverly using the desktop machine as a conduit between the
potentially large xsvf file and the firmware.

I didn't try to get Ben's code running on the Papilio, because I have a
different strategy in mind. I have ported the device portion to the Arduino,
and I'm going to rewrite the tiny C-based desktop client in Python. It would
be odd for someone to have a CPLD but _not_ have an Arduino within arm's
reach, and while every hobbyist _should_ have a Papilio (hi Jack!), it's less
common. As for the command-line tool, it's straightforward I/O, which means
Python's the perfect choice to get Mac/Windows/Linux/wristwatch support for
free. Last night I got the Arduino communicating with the C client just enough
for the Arduino to start sending debug messages telling me it was very
confused about its purpose in life. Tonight I hope to get it able to program
something on the '9572, and then I'll have a known-good toolchain against
which to develop the Python client.

Just a bit of pontificating about **using the right tool for the job**. It
makes me sad when projects with a cross-platform audience use .BAT files, and
it makes me sad any time I see C/C++ where cycle-for-cycle performance isn't
an issue. For shell scripts, use Bash. Install [Cygwin](http://cygwin.com/) if
your favorite OS is one of the… one that doesn't know Bash. And for pretty
much every other desktop tool you can think of, consider Python rather than C.
People reflexively think of C as the go-to language for portability, but at
the tool level where you care more about how to open a nonblocking serial port
rather than the endianness of an int, Python remains portable where C starts
spewing out #ifdefs.

Anyway, back to the topic. When this project is done, any maker will be able
to program a Xilinx CPLD with the hardware and OS he or she already has. No
more ridiculous $50 cables.

