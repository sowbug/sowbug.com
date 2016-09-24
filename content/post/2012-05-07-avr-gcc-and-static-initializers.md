+++
date = "2012-05-07T09:01:51-07:00"
title = "avr-gcc and static initializers"
+++



In the [avr-gcc FAQ](http://www.nongnu.org/avr-libc/user-manual/FAQ.html), the
question "Shouldn't I initialize all my variables?" gives a hint why your
nonzero static initializers aren't working:

> [G]lobal and static variables that have an initializer go into the .data
section of the file.

I had been seeing static variables without a declared assignment correctly
initialized to zero, but any nonzero initialization didn't seem to be doing
anything. But reading the FAQ led me to examine my makefile, where I found
this interesting section:

> `%.hex : main.obj  
>  $(OBJ2HEX) -j .text -O ihex $< $@`

Aha! So avr-gcc was likely putting the initialized variables into .data, but I
was omitting that section when generating the Intel hexfile. Adding another -j
section for .data fixed it.

