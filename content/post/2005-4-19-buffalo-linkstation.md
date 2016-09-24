+++
date = "2005-04-19T19:38:55+00:00"
title = "Buffalo Linkstation"
+++



If you are having trouble updating the firmware on your [ Buffalo
Linkstation](http://www.buffalotech.com/products/product-
detail.php?productid=36&categoryid=10) or [ Kuro Box](http://kurobox.com/)
using Windows XP, try turning off your computer's firewall. The setup program
appears to use UDP in both directions, possibly sending and receiving on
different ports, and the default settings of the XP firewall interfere with
the traffic. I'm sure the setup program warns you somewhere to do this, but if
you're like me, you typically ignore all those warnings. Well, this time they
mean it.

