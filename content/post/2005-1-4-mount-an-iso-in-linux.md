+++
date = "2005-01-04T14:35:00+00:00"
title = "Mount an ISO in Linux"
+++



As root:

mkdir /mnt/iso  
mount -o loop -t iso9660 yourcd.iso /mnt/iso

