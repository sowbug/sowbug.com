+++
date = "2012-01-19T11:20:05-08:00"
title = "the 595 loading code worked on the first try"
+++


![](http://66.media.tumblr.com/tumblr_lxvn8sQ9kM1qly645o1_1280.jpg)  

The '595 loading code worked on the first try, which I can explain only
because I found the cascading shift-register logic unintuitive at first, until
I realized I got to make up the rules about endianness, data/address order,
etc., and at that point I had the whole sub-project fully in mind. Usually a
great time to bang out a few dozen lines of code!

On the screen you can compare the bytes to be loaded ($12, $12, $12, $0e, $fe)
with the lower nibbles implied by the logic analyzer ($2, $2, $2, $e, $e) and
confirm they match up. I haven't tested the address lines yet. We're getting
close to hooking up ROM (or SRAM that's not writeable) to the '09!

