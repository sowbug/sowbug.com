+++
date = "2012-02-07T11:20:06-08:00"
title = "my goodness id forgotten how hard it is to solder"
+++

 ![](/tumblr_files/tumblr_lz0h5gpID71qly645o1_1280.jpg)  
The three boards, before
assembly.![](/tumblr_files/tumblr_lz0h5gpID71qly645o2_1280.jpg)  
WORST SOLDER BRIDGES
EVER![](/tumblr_files/tumblr_lz0h5gpID71qly645o3_1280.jpg)  
Board #1 working, next to proud sibling  

My goodness I'd forgotten how hard it is to solder surface-mount devices. But
I did it, and one of three XC9572XL breakout boards is working. Rehash of
experience in approximate order of occurrence:

  * Wanted to work on a different, software project tonight, but the boards arrived in the mail and they were so purple that I had to work on them right away.
  * I don't understand how any SMD component could be smaller than 0603. Seriously, they make 0204, but 0603 almost floats if I breathe in the same room as it.
  * Dangerous Prototypes, you're good guys and all, but did you really put the three inline LEDs in different polarities? I burned up one and reworked four in the process of figuring that out.
  * Despite triple-checking, I put the 10K resistors where the 2Ks go. More rework.
  * To remove solder bridges from gull-wing QFP leads, clean the tip, flux the heck out of the bridge, and press gently on it. Bam! [Ready to ship](http://www.youtube.com/watch?v=eg2hxpy--gg).
  * Did I say flux? Yes, flux is totally, utterly awesome for making solder just do the right thing.
  * Your CPLD breakout board will kinda sorta accept an XSVF if the 3.3-volt IO jumper is off. In fact, the kinda sorta acceptance is exactly the same as if you'd done a cold solder joint here or there, or maybe shorted a capacitor, or left some conductive flux on the board, or…. Anyway, after ruling all those things out you'll try the jumper and find that it programs perfectly well.

I'll finish the other two some other time. Right now, I'm so happy this first
one works!

