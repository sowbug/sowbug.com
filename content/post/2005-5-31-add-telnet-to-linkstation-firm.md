+++
date = "2005-05-31T21:28:53+00:00"
title = "Add telnet to Linkstation firmware"
+++



[ This tarball](http://www.sowbug.org/mt/archives/mod_ls_firmware.tar.gz)
contains the Linkstation telnet binary and a script that inserts the binary
into a Linkstation 1.4x firmware installer and configures inetd to run telnetd
at system startup. Read the instructions at the top of the shell script. I
haven't actually tested to see if this works, but if it doesn't it shouldn't
take much more effort to fix it.

This approach saves bandwidth compared to downloading a new 37 megabyte
installer for each tiny change.

