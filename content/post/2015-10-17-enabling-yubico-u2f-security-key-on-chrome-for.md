+++
date = "2015-10-17T11:36:08-07:00"
title = "Enabling Yubico U2F Security Key on Chrome for Ubuntu 15.04"
+++



This works for the [blue FIDO U2F key](http://amzn.to/1jLwkVf).

Create a new file called **/etc/udev/rules.d/50-security-key.rules**:

`**SUBSYSTEMS=="usb", ATTRS{idVendor}=="1050", OWNER="root", GROUP="plugdev",
MODE:="0660"**`

Once that file is saved, **sudo udevadm control -reload-rules** and then
restart Chrome. Your security key, which previously was likely giving you a
“An unexpected error occurred [retry]” message, will now work.

I figured this out with the command **udevadm info -n /dev/usb/hiddev0 -a**,
inspecting the output to determine that other solutions on the web were
missing the S at the end of SUBSYSTEMS and ATTRS. For the assignment parts of
the udev rule, the values root/plugdev/0660 were correct.

