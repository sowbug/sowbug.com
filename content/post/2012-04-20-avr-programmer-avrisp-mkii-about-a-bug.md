+++
date = "2012-04-20T08:46:58-07:00"
title = "AVR Programmer, AVRISP mkII: About a bug"
+++



I had a good debugging session over the last few nights and want to write down
my notes here.

The [AVR Programmer](/post/19682029334/the-programmer-works) initially worked
with a target '328p, but it hung when programming a second build of the board,
and then again on a particular ATtiny13A that I was using for the [Hypna Go
Go](/post/20906913903/the-hypna-go-go). Oddly, it worked for another '13A that
I was using on the same project. The board was flaky, and as a result, I
couldn't keep my promise to myself to never again ISP-program another AVR
without a programmer I'd built myself.

A few nights ago, while getting ready for the latest and greatest version of
the board to arrive from the factory, I decided to take a look at what was
going on. I got out my [Saleae Logic](http://www.saleae.com/) and watched the
SPI traffic. Perfect… except that the target '13A never responded on MISO. I
swapped in a known-good programmer, confirmed it worked, but then saw that the
logic signal patterns were identical. _The target wasn't responding, but the
known-good programmer was programming it!_

I suspected bad logic probe connections… nope. They were fine.

Getting a bit frantic, I zoomed out in the Logic app, and immediately figured
out why the target wasn't responding. The first cycle through the
initialization sequence (the only cycle I'd been examining), it always failed.
But the second cycle succeeded, and I never saw this until I zoomed out.

Next question: why was the known-good good? I re-read the datasheet for the
'13A and saw that if the programmer couldn't guarantee SCK was low on target
powerup (which indeed applied in both my and the known-good programmer cases),
an alternate way to get into programming mode was to pulse /RESET high for a
bit. I could see the known-good doing this between the first bad and second
good cycles, and my firmware was doing the same thing, so what was the
difference?

Back to my programmer under the logic analyzer. Zoom out… and see that in fact
/RESET was staying low consistently. Aha! That's the problem. But why was it
happening?

It turns out that the LUFA code doesn't pulse /RESET by sending it high.
Instead it _tristates_ the pin. This makes sense because you want your
programmer to disconnect from the target when you're done so that /RESET can
go back high on its own. This is fine, except that my programmer has a
74AHC125 buffer between the '32u2 and the ISP outputs, and _a tristate output
entering the buffer leaves as a low logic signal_. This is why my programmer
wasn't pulsing /RESET, and it's why programming _sometimes_ worked if the
powerup sequence happened to be right, or if the chip in question (such as
most 328p's or some 13A's) happened to be a more tolerant sample.

Once I understood the problem, [the fix was easy](https://github.com/sowbug
/lufa-lib/commit/258ecc31c993826bf5c520699c38b9d8183b00cb). Change LUFA to
pulse /RESET with explicit logic levels, and insert buffer enable/disable code
at the appropriate places. So far, it's been running flawlessly.

