+++
date = "2012-02-27T06:46:00-08:00"
title = "New Project: AVR Programmer"
+++



I've been trying to break the [Joust rebuild](/post/15856726973/project-8821)
project into meaningful chunks. My [recent attempt at designing a circuit for
manufacture](/post/17728637463/a-very-early-and-surely-broken-board-layout-on)
in EAGLE didn't pan out; it seemed both too big, because I hadn't yet
breadboarded all the sub-circuits as a single large circuit, and at the same
time too small, because it would have been little more than those simple sub-
circuits that I had successfully breadboarded. I'd have taken a lot of risk to
fabricate a fairly boring PCB.*

Rather than hem and haw about what exactly to build next for Project 8821, I
decided to take [Quinn](http://quinndunki.com/blondihacks/)'s approach and
gain experience building a tool that I knew for sure I'd need:

![](http://65.media.tumblr.com/tumblr_m01e9iv2Su1qjj3vh.png)

This is going to be an [AVR in-system programmer and XSVF
player](https://github.com/sowbug/avr-programmer). True, I could buy a USBtiny
clone for $10 on eBay or a [real one in kit
form](https://www.adafruit.com/products/46) for $26 shipped, and in fact I
have plenty of gizmos capable of programming AVRs, but I don't have anything
that can also program CPLDs, the [JTAG
Whisperer](https://github.com/sowbug/JTAGWhisperer) notwithstanding. The JTAG
Whisperer is great in a pinch, but I really need it to speak 3.3v and to not
require my Arduino, which is often enlisted in other projects.

And unlike any other AVR programmer I'm aware of, _**mine won't require that
frickin' ugly and gigantic 6-pin ISP ribbon cable**_. See that angled
footprint in the lower-right corner? It's going to have a _**socket**_
sticking out of it at a right angle, so it'll be a cinch to stick the board
directly onto the target without _**any cable whatsoever**_. (Actually, by
"whatsoever" I really mean it'll need just a mini-USB cable on the other end,
but those are so commonplace and compatible with other devices that I don't
consider it an inconvenience to keep one on my desk. So it doesn't really
count as a cable.)

I'll be sending this board out for manufacture shortly. I'm excited about it
because I honestly think it'll be a pretty darn good AVR programmer. I might
have a couple extra boards left over, so if you don't have your own programmer
and need one, leave a comment. I'll probably need one more rev of the PCB and
still have the small matter of writing the firmware, but I'd love to have
others using my creations!

**Update**: made some changes (VCC separate from 8u2 supply, VCC-5V header removed) after great suggestions from [frank26080115](http://www.reddit.com/user/frank26080115), who is also the creator of the [USnooBie](http://www.frank-zhao.com/usnoobie/). Thanks, Frank!

*"Boring" is a strong word. If I stuck a serial port on that board, it'd be at least as fascinating as any home computer that existed before the video-capable Apple ][. But I want to stay on project target; if I added a serial port, then I'd have to write 6809 software to _use_ it. Given my self-imposed project constraint of avoiding getting into 6809 software and instead treating the Williams ROMs as an invariant, the serial port wouldn't make sense. 

