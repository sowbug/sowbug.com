+++
date = "2012-05-04T08:54:48-07:00"
title = "Don't make this mistake with Arduino streaming APIs"
+++



This happened to me. Don't let it happen to you.

  1. Write a constant somewhere, like Wire.write(0x06). In my case, this was sending an address to an I2C chip, but it could be Serial.write() or something else like that.
  2. Confirm everything's working great.
  3. Later on, change to Wire.write(0x00).
  4. Get a compile error about how the function signature is now ambiguous because zero can be any of multiple types.
  5. Be specific: Wire.write(0x00, HEX).
  6. Confirm everything's working great.
  7. Now copy your earlier code somewhere else: Wire.write(0x04, HEX).
  8. Your I2C device begins emitting lethal radiation focused on nearby kittens.

The mistake started with step 4 (misinterpreting the compile error) and its
fate was sealed with step 5. The problem is that the Arduino's print/println
methods are slightly different in that they take an optional format argument
as the second parameter if the first doesn't fit a single function signature.
The streaming APIs, on the other hand, take a pointer and a length. So my
Wire.write(0, HEX) was actually Wire.write(address 0, 16 bytes). In Step 6 I
just got lucky that whatever I wrote to the device didn't change behavior
much, but Step 7 my luck ran out.

**TL;DR: print takes a format specifier. Streaming libraries take a length. If you mix them up, it still builds.**

