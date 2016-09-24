+++
date = "2012-04-06T09:00:59-07:00"
title = "Emulating a 6809 in a slow ARM mcu"
+++



As a thought experiment I'm wondering about a different approach to Project
8821. The
[STM32F407VGT6](http://www.st.com/internet/evalboard/product/252419.jsp) is a
168MHz ARM Cortex M4 processor with plenty of flash and RAM to handle Joust.
Could it emulate a 1MHz 6809, drive resistor-ladder analog video, and output
sound? I bet the answer's yes.

