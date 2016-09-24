+++
date = "2015-12-23T09:07:13-08:00"
title = "Request: hobbyist remote control"
+++



I want a device that looks nice enough to keep on a coffee table, that has a
small number of buttons, that emits well-documented RF signals in response to
those buttons, that has some kind of reasonable security story, and that is
manufactured in enough quantity that it’s cheap and not hard to find. This
would be a **hobbyist remote control**. It would allow me to build ugly
devices that I could hide in a cabinet, then control them with something not
ugly.

Today, here are my options:

  * Repurpose a universal remote. Build an IR receiver into my project. Pick some RC-5 codes. This solution fails because it's line-of-sight. And most universal remotes have an absurdly large number of buttons.
  * Use a 315/433MHz remote and receiver. [Here's one example](http://www.aliexpress.com/store/product/Free-Shipping-Universal-4-Channel-433mhz-RF-Wireless-Remote-Control-Module-2262-2272-Remote-Controler-Kit/1725790_32381477987.html). This is close to what I want, but the documentation isn't great, the security is probably poor, the appearance and form factor are not to my taste, and it's not clear whether I'd be able to buy another receiver that works with it (for starters, which of the [69 LPD433 channels](https://en.wikipedia.org/wiki/LPD433) does this one use? Probably 433.925MHz, but how do I know for sure?).
  * Use a phone and write a BLE app that talks to a BLE receiver. This is what all the cool kids are doing these days. But it doesn't help me when I'm at work and my visiting mother-in-law wants to [lower the blinds/turn on the Christmas tree/calibrate the flux capacitor].
  * Repurpose a quadcopter remote, many of which use the NRF24L01+. This fails many of my criteria, but I did spend some time researching how well that chip has penetrated the consumer market.

Does this device exist? If it did, would anyone but me buy it?

