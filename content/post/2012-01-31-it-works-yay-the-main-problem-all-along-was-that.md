+++
date = "2012-01-31T19:22:53-08:00"
title = "it works yay the main problem all along was that"
+++

 ![](/tumblr_files/tumblr_lyp2qaheTD1qly645o1_1280.jpg)  

It works! Yay! The main problem all along was that I was running the board at
5 volts, not the 3.3 volts it needs. It was able to respond to JTAG commands
at the higher voltage, but it correctly reported that it couldn't write its
flash memory under those conditions.

I still need to update the README for the [JTAG
Whisperer](https://github.com/sowbug/JTAGWhisperer), but the code in the
repository should work right now. Hooray!

