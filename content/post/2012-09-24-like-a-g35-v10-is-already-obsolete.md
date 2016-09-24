+++
date = "2012-09-24T08:58:47-07:00"
title = "Like A G35 v1.0 is already obsolete"
+++



As discussed [earlier](/post/31323978178/like-a-g35-v1-0-is-at-laens), Like A
G35 should arrive soon from OSH Park. Even though it's not here yet, I already
know I blew it with the board design. The board will still work, but it could
be _so much better_.

In addition to the G35 protocol that I know and love, this board was supposed
to support the WS2801 protocol. It turns out that WS2801 happens to work
really well with hardware SPI, as do lots of other chips, such as the SM16716
and LPD8806, all of which are supported by the [FastSPI
project](http://code.google.com/p/fastspi/). Unfortunately, since I hadn't
played with any of these lights until this weekend, I didn't know this, so I
wasted the Arduino's hardware SPI on my 1.0 shield design. The shield will
handle short strands of WS2801 and friends, but it won't be as fast as a
hardware solution.

I'm probably going to wait for 1.0 to arrive so that I can get my home G35
lights going in time for Halloween (I'm thinking spooky orange and green
inchworms), but after that I'll revise the board to do proper WS2801 support
over the Arduino's pins 11 and 13. This will actually free up a lot of board
space, as I've since figured out that there isn't a real benefit to multiple
WS2801 outputs. Shifting all WS2801 lights on a single output is just as much
work as shifting on multiple outputs, whereas the G35 protocol needs multiple
outputs because one output can't handle more than 63 lights.

