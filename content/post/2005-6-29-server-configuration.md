+++
date = "2005-06-29T15:18:32+00:00"
title = "Server configuration"
+++



Some of what I've done to my new server so far. By the way, it's Fedora Core
2. I'm running Core 2 because Core 3 and later pretty much require yum rather
than apt, and yum is a real resource hog and won't reasonably work in 64MB of
DRAM.

  * As root: crontab -e, then add `25 3 * * * apt-get update && apt-get -y dist-upgrade`.
  * Create a backup script on a different machine with several lines resembling this:   
`rsync -az -vv --sparse --stats --delete --rsh=ssh root@<hostname>:/home .`  
I put the public key for the archiving machine in root's
.ssh/authorized_keys2, so that the script can log in automatically without
needing to know root's password.

  * `apt-get install ImageMagick ImageMagick-perl` (note that they're case-sensitive!)

I'll update this entry as I do more stuff.

