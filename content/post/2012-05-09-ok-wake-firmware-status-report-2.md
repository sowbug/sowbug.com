+++
date = "2012-05-09T09:01:26-07:00"
title = "OK Wake firmware, status report #2"
+++



Things are looking better.

I wrote a unit test suite that is buildable with regular GCC, so I was able to
get the arithmetic routines written quickly without coaxing tiny LEDs into
telling me the microcontroller's entire internal state. This worked well. I
didn't have to stub or mock out the hardware, but I could see doing that for a
more complex project.

I briefly dabbled in pure shift-based arithmetic (multiply by 205, shift right
11 times!) when I ran out of program space and took a hard look at the
assembly with avr-objdump -S. This didn't work out; doing mod 10 to convert
from decimal to BCD was eye-crossing and approaching the size of the avr-libc
mul/div libraries. Instead I took a different approach.

I hated the AVR310 reference I2C code for its size and seemingly needless
complexity, so I replaced it with Peter Fleury's awesomely tiny [I2C Master
library](http://homepage.hispeed.ch/peterfleury/group__pfleury__ic2master.html).
I couldn't believe that it worked perfectly on the first try. Since it uses
plain GPIOs and doesn't mess with the USI, I could even rework the circuit in
the future to move the button/INT functionality to the '25's INT0 pin, getting
more precise pin-change interrupt events in the bargain.

This got me well under 0x700 bytes, so I could once again easily afford to use
*, /, and % (I actually skipped %, preferring to multiply back the division
result and subtract from the original value).

Code's looking good and starting to feed solid.

