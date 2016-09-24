+++
date = "2012-02-02T11:20:06-08:00"
title = "TTL Voltage and Current Cookbook Recipe"
+++



Now that I'm able to [do something](/post/16850810843/) with this CPLD, I've
been concerned about replacing $10 of discrete logic chips with a $2 chip that
needs $8 of level shifters. Though the Xilinx XC9572XL is a fairly modern
3.3-volt device, I know its I/O pins are 5-volt tolerant, meaning that I can
send in a 5-volt signal from my circa-1980s 5-volt 6809E. But the '72's
_output_ voltage is selectable at either 3.3v or 1.8v, and not 5v. And [as
established earlier](/post/16828497482), 5 volts do not equal 3.3 volts. What
to do? Some inspired laziness ("maybe it'll just work") led me to read the '09
datasheet, and then do a bit more general research.

And I have concluded that yes, maybe it'll just work. TTL logic levels define
a low as zero to 0.8 volts, and a high as 2 to 5 volts. Why not exactly zero
and exactly five? Well, there needs to be some margin for error. We software
engineers like to think of pure concepts like binary zeroes and ones. But on
the oscilloscope, real-world logic values sometimes look like a [nervous
driver on a twisty road at
night](http://www.xilinx.com/support/documentation/application_notes/xapp429.pdf).
(Sorry, that link is a PDF, but it nicely illustrates what the 45- and
90-degree angles in datasheets really look like.) So low is a range, and high
is a range, and 3.3-volt digital logic values are entirely consistent with
5-volt ranges. It's… as if… (concentrating very hard now)… when The Powers
That Be wanted to move to lower-voltage - and thus lower-power - electronics,
they _didn't come up with a new standard so much as pick tighter tolerances
for the old one_. 3.3 is almost exactly in the middle of the old 2- to 5-volt
range, and there's probably some other practical reason why it's easier to
generate 3.3 volts than 3.5 volts.

Anyway, speculative history lessons aside, I'm pretty sure the 6809E will
recognize signals from the 3.3-volt I/O lines of the CPLD. I'll wire something
up before committing it to a PCB, of course, but everything I've read suggests
this will work.

Here's the current ingredient list for Prototype Board #1:

  1. Two power supplies: 5 and 3.3 volts.
  2. 6809E.
  3. 128KB SRAM.
  4. MicroSD card slot.
  5. ATmega32u4.
  6. 16MHz crystal.
  7. XC9572XL.
  8. [DAC](http://en.wikipedia.org/wiki/Delta-sigma_modulation) for audio, with an audio jack.
  9. [DAC](http://en.wikipedia.org/wiki/Resistor_ladder) for video, with a video-out header.
  10. Game-control input header.
  11. [Placeholder for generating the digital side of the video signals.]

The '32u4 is the star of the show. I think it can do all these things:

  * As a [JTAG Whisperer](https://github.com/sowbug/JTAGWhisperer), program the CPLD during development.
  * Read the SD card and set up part of the SRAM as ROM from the perspective of the 6809E.
  * Assert the 6809E's reset line when everything's set up.
  * Handle all the 6821 game-control PIA duties.
  * Depending on what's left, maybe even output sound using PWM.

Meanwhile, the CPLD should be able to do this:

  * Manage the address and data bus.
  * Turn the 16MHz crystal into the '32u4's clock, and into the Q/E signals. I don't yet know whether a CPLD can turn a crystal into an oscillating signal.
  * In a dream world where I'm much smarter than I am, fit the Williams Special Chip blitter into the 72 macrocells.
  * Feed the digital video signals into the resistor ladder.

And of course the several-dozen other jobs I've forgotten. Phew!

