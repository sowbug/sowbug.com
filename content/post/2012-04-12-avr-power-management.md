+++
date = "2012-04-12T08:55:00-07:00"
title = "AVR Power Management"
+++



I designed the [Hypna Go Go](https://github.com/sowbug/hypnagogo) schematic
and board quickly in one evening and sent it to be manufactured that night.
The next day I realized I'd forgotten to add a power switch, meaning I'd have
to remove the coin-cell battery every morning.

_Or I could solve the problem in software._ That's what I did.

You can read the code for yourself, but I took advantage of the fact that I
already had a momentary button between ground and PB4 on the ATtiny for
switching immediately into dream mode. The updated firmware starts out by
turning off all unneeded peripherals, such as the ADC and BOD, then turning on
a pin-change interrupt on PB4. Then it switches to the PWR_DOWN sleep mode. In
other words, putting in the battery starts up the device in a switched-off
state.

Pressing the button fires the interrupt, effectively turning on the device,
and it does all the setup it would have done normally. I refactored the button
code to manage all the relevant state inside the pin-change interrupt service
routine. Tapping the button goes straight into STATE_DREAM as before, but
holding it down for two seconds goes back into PWR_DOWN sleep mode, after a
blink sequence to confirm that it's really shutting off.

I haven't yet figured out how to measure microamp-level current draw in this
circuit, but if I'm doing it correctly, then I'm probably drawing less than
1uA in switched-off state. Even for a 40mAh CR1220 coin cell, that's a few
years, and it easily outweighs the cost and complexity of adding a physical
slider switch.

