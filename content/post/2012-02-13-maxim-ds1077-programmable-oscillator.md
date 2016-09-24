+++
date = "2012-02-13T14:04:05-08:00"
title = "Maxim DS1077 Programmable Oscillator"
+++



The [Maxim DS1077](http://www.maxim-ic.com/datasheet/index.mvp/id/3359) is a
programmable oscillator. Instead of ordering different oscillators for each
different project you have, you get just one on a [SparkFun breakout
board](http://www.sparkfun.com/products/9116) and program it, using I2C, for
whichever frequency you need.

![](http://66.media.tumblr.com/tumblr_lzbbrywayk1qjj3vh.jpg)

And in fact, after some stumbles on my part, yes, it works.

**Things I Learned About the DS1077, The Hard Way**

  1. The [I2C interface](http://en.wikipedia.org/wiki/I%C2%B2C) (a.k.a. TWI or two-wire interface) depends on someone (i.e., you) to pull SCK and SDA high. Toss some pull-up resistors on those lines. I think there's something cool going on with this protocol that I might be able to exploit for 8821's bus arbitration. Must read more.
  2. The [Bus Pirate](http://dangerousprototypes.com/bus-pirate-manual/) doesn't turn on its power supply until you tell it to. This is very much a feature, not a bug.
  3. SDA and SCK are not interchangeable. I hope you didn't need the internet to tell you that; I almost did.
  4. The Bus Pirate's MOSI connection isn't labeled for I2C, but it's what drives the SDA line. This makes sense (master-out, slave-in) but I had to look it up to be sure.
  5. When you're at your wits' end and not understanding why your lines are full of random glitches, _try changing the wires_. Sometimes even simple things like wires can be no good!

For posterity, here's the Bus Pirate sequence I used to program my DS1077 with
an approximately 4.03MHz signal on OUT1, with the two CTRL inputs disabled:

HiZ&gt;m  
…  
4\. I2C  
…  
  
(1)&gt;4  
I2C mode:  
1\. Software  
2\. Hardware  
  
(1)&gt;2  
Set speed:  
1\. 100KHz  
2\. 400KHz  
3\. 1MHz  
(1)&gt;1  
Ready  
  
I2C&gt;W  
POWER SUPPLIES ON  
  
I2C&gt;[ 0xb0 0x0d 0b00001000 ] **(Don't write every change to EEPROM)**  
I2C START BIT  
WRITE: 0xB0 ACK  
WRITE: 0x0D ACK  
WRITE: 0x08 ACK  
I2C STOP BIT  
  
I2C&gt;[ 0xb0 002 0b00011000 0b00000000 ] **(Use just the 10-bit frequency
divider)**  
I2C START BIT  
WRITE: 0xB0 ACK  
WRITE: 0x02 ACK  
WRITE: 0x18 ACK  
WRITE: 0x00 ACK  
I2C STOP BIT  
  
I2C&gt;[0xb0 1 0b00000111 0b11000000] **(Write 31 (133MHz/(31+2)) to
divider)**  
I2C START BIT  
WRITE: 0xB0 ACK  
WRITE: 0x01 ACK  
WRITE: 0x07 ACK  
WRITE: 0xC0 ACK  
I2C STOP BIT  
  
I2C&gt;[0xb0 0x3f] **(Write out the settings to EEPROM)**

By the way, this is my first time using the Bus Pirate for a project. I've
tried a couple times but bounced off because of v4/v3 incompatibility pains.
I'm not in love with the interactive serial-terminal interface. But I do
appreciate the idiot-proofing, such as starting up with all signals in high-
impedance mode. That'll keep me from destroying my equipment someday, for
sure.

