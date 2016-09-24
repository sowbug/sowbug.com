+++
date = "2012-04-29T09:47:22-07:00"
title = "Awesome work on JTAGWhisperer!  Been reading all about this project and ran into a hitch. First my setup...  I'm using an Arduino Duemilanove with 4 channel bidirectional logic level converter and trying to program my Taio xilinx Coolrunner II (XC2C64A).  I get the ready to send output, and then confirmation that the device is ready.  After that it freezes after sending 32 bytes, no matter what xsvf I try and program to the CPLD.  TDO is high at 3.3v on the CPLD, but just hangs.  Any thoughts?"
+++



When I was debugging this thing, the Arduino serial connection (which uses
software flow control, a.k.a. no flow control) was getting confused or falling
behind. Try setting both sides to a very low bitrate (like 9600 or 2400).

Do you have a logic analyzer? That was invaluable in isolating problems.

Are you sure that the target board doesn't have any jumper/power requirements?
My board needed two power sources: one for the core, and one for the I/O.

The smallest possible XSVF is one asking for the device ID and ending. That
one's also attractive because it doesn't involve writing (which can be very
finicky about voltage levels).

Be sure your XSVFs are generated specifically for your chip. The ones in the
repo are for a XC9572XL, which is incompatible.

That's all I can think of right now.

