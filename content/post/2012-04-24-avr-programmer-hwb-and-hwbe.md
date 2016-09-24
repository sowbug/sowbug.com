+++
date = "2012-04-24T09:04:18-07:00"
title = "AVR Programmer, /HWB, and HWBE"
+++



I made a minor error in 1.0 of the circuit. I was so proud of myself for
noticing that external pullup resistors were redundant when the AVR's internal
pullups were activated that I neglected to put a pullup on /HWB. This is the
pin that, when the HWBE fuse is programmed, should be high to run normal
application code on reset, and low to start the bootloader. Instead I'm seeing
the bootloader always running on reset, meaning that the BOOT solder jumper
does nothing.

This makes sense in retrospect. The datasheet says that all pins return to
their default states on reset, and for PORTE pins, that's tristated. So my
/HWB is floating, and the AVR is consistently reading a low logic level.

Adafruit (and software) to the rescue! They modified LUFA's
[BootloaderCDC](https://github.com/adafruit/lufa-
lib/commits/master/trunk/Bootloaders/CDC/BootloaderCDC.c) to time out the
bootloader after a few seconds. Plus they added a nice breathing LED feature,
so at least bootloader mode (even if unwanted) is pretty. This means that on
reset, you get _both_ the bootloader and the programmer; you just have to wait
a moment for the programmer to appear. This is fine, because for most use
cases (plugging in the board to USB) it goes straight to the programmer,
skipping the bootloader.

In the next rev of the circuit I'll add the pullup so that the BOOT jumper
does something. But the software change means the 1.0 board is functional.
Cool!

**Update: I wrote to Atmel Support (knowing that Dean was on duty) and got a marvelously complete response:**

> Dear Mike,  
>  
> That is correct; the AVR pins are tri-stated during the reset procedure, and
as a result no pull-up is applied to the HWB pin while it is sampled. As a
result, you will need to add an external pull-up (or, to invert the logic,
pull-down) to this pin to ensure that the correct behavior is applied every
time the chip is reset. There is no way to specify that the pull-up is to be
enabled during the reset procedure on the HWB pin.  
>  
> One possible solution to this is to disable the HWBE fuse, and instead
program the BOOTRST fuse. This will unconditionally start the AVR's bootloader
every time the device is reset (regardless of reset source). Inside the
bootloader as part of the initialization procedure you can enable the pull-up
on the HWB pin and sample the value manually, jumping to the user application
if the pin is not in the desired state via a software-jump to location 0x0000.
An example of this procedure is shown in the LUFA DFU bootloader, when
compiled for the XPLAIN board, although this uses an unrelated JTAG pin as the
trigger to stay in or leave the bootloader.  
>  
> Best Regards,  
> Dean Camera  
> Atmel Technical Support Team

