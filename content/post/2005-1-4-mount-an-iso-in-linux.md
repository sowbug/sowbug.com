+++
date = "2005-01-04T14:35:00+00:00"
title = "Mount an ISO in Linux"
+++

\--- title: Mount an ISO in Linux mt_id: 155 layout: post date: 2005-01-04
14:35:00 +00:00 \---

As root:

mkdir /mnt/iso  
mount -o loop -t iso9660 yourcd.iso /mnt/iso

