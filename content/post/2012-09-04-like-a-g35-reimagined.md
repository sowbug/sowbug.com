+++
date = "2012-09-04T19:17:29-07:00"
title = "Like A G35, reimagined"
+++



Three months away from electronics can sure clear one's mind! Maybe it was the
vaporized lead.

Rather than designing my Christmas-light controller project [Like A
G35](http://www.sowbug.com/post/23737105747/new-project-like-a-g35) as a
standalone AVR board, I have come to my senses and decided to make it an
Arduino shield instead. The first iteration of the board started with the
ATmega32U4, which is little more than an integrated Arduino in terms of
capabilities, so I wasn't adding any functionality by building the
microcontroller portion myself. All I was doing was indulging my DIY
tendencies. A shield reduces costs, design time, and risk, and it gives me
more surface area for terminal blocks.

Other than this blog post and a quick review of my earlier EAGLE files, I
haven't done any actual work. But when my kids started talking about Halloween
costumes this weekend, I realized that Christmas is right around the corner -
particularly at the slow pace of hobby electronics. Time to lay it out!

Current feature list:

  * An Arduino shield that might be slightly unusual in that the raw power will go directly to it rather than through the Arduino. This is because I'll want much higher current than the Arduino's built-in voltage regulator (or USB socket with 500mA fuse) can safely handle in order to power the lights.
  * As many sets of terminal blocks as I can fit on the shield. I was originally going to do just three-post blocks with the G35 positive/data/negative pinout, but I might instead do a four-post pinout adding a clock out for WS2801 light strands.
  * An IR receiver for remote control.
  * A real-time clock circuit that I doubt I'll ever populate. Given the limited program size of the ATmega328p, I honestly can't see how I'd be able to stuff enough light programs in to want to run it year-round.

Now that it's become a shield, this circuit is getting pretty simple. That's
good!

