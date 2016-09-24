+++
date = "2012-01-27T11:20:06-08:00"
title = "i feel like neo when the plug gets yanked out of"
+++


![](http://67.media.tumblr.com/tumblr_lygws6N0jG1qly645o1_250.jpg)  

I feel like Neo when the plug gets yanked out of his head: "I know JTAG."
Except I really don't, and it took three days instead of three seconds.

JTAG is a little like SPI. You send bytes to the slave, the slave does
something with them, and then you get bytes back. The protocol is clocked by
the master, and you shift TDI bits out as you're reading in TDO bits. But as
far as I can tell, the timing is intolerant compared to SPI, at least on the
XC9572XL that I'm trying hard not to destroy. The slightest change in clock
pulse width gets the incoming TDO bits completely out of sync. [Ben's
code](http://www.sowbug.com/post/16531649193/found-a-good-base-for-an-xsvf-
player) shows a lot of hard work on his part getting this timing exactly right
for his Papilio, but the adjustments need to be redone for Arduino. I'm
getting more handy with a logic analyzer; my favorite trick to date is the
"debug line" that sets an extra pin high when a certain interesting event is
about to happen, making it very easy to scroll to the right part of the logic
timeline. It's the equivalent to sticking a debug printf into software. I
doubt I'm the first person to invent that one.

