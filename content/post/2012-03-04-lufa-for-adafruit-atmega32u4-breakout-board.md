+++
date = "2012-03-04T14:05:00-08:00"
title = "LUFA for Adafruit ATmega32u4 Breakout Board"
+++



[LUFA](http://fourwalledcubicle.com/LUFA.php) is pretty amazing. If you're
into that kind of thing, you can make your USB-capable AVR microcontroller be
100 virtual serial ports, all communicating with other, all at once. I'm not
sure why it took me a few hours to get even one virtual port to appear, but
once I followed [my own steps](/post/16644998284/) to restore my ['32u4
breakout board](http://www.adafruit.com/products/296) to factory-fresh
condition, it worked nicely. Here are my notes:

  * To build any or all of the whole tree, get the source and then  
**  
make MCU=atmega32u4 F_CPU=16000000 BOARD=ADAFRUITU4 FLASH_SIZE_KB=32
BOOT_SECTION_SIZE_KB=4  
**  
You'll get various errors about missing joysticks, buttons, and ADC channels,
and you'll have to hack and slash the code to pretend your board has a
joystick (I used rand() % 4 to simulate someone flipping around the joystick
wildly) or whatever else is missing. You might decide to give up and build
just one or two sub-projects.

  * To load a demo or project onto your board, cd into the right directory and  
**  
make program MCU=atmega32u4 AVRDUDE_PROGRAMMER=avr109
AVRDUDE_PORT=/dev/wherever_your_board_shows_up  
**  
You'll need to reset your board so the bootloader is running during this step.

  * On my machine (a Mac), I kept System Information open to the USB section, and kept hitting command-R to see what my computer thought was attached to it.

I'm fiddling with LUFA to get ready for the [AVR
programmer](/post/18568875922/)'s arrival in a week or so. I don't expect to
have ported an ISP by then, but at least I can have a simple CDC serial port
saying "hello, world!"

