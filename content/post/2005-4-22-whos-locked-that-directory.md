+++
date = "2005-04-22T14:28:35+00:00"
title = "Who's locked that directory?"
+++



To figure out why you can't unmount a busy directory, try this:

`fuser /mnt/share`

You'll get back the process ID of the responsible party.

