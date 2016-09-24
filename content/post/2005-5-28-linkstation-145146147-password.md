+++
date = "2005-05-28T23:04:43+00:00"
title = "Linkstation 145/146/147 password"
+++

\--- title: Linkstation 145/146/147 password mt_id: 175 layout: post date:
2005-05-28 23:04:43 +00:00 \---

I wanted to add a few features to my Linkstation HD-H120LAN, but the newer
versions of the 1.4x firmware are password-protected and don't have the same
vulnerabilities as earlier versions that allowed hobbyists to tinker with
them.

So this is what I did. _(These instructions assume you're already experienced
with Linkstation/Kuro Box hacking.)_

  * Download the 145_13 firmware update and extract firminfo.txt, ramdisk.image.gz, and vmlinux.gz from the firmimg.bin in it.
  * gunzip ramdisk.image.gz and mount it using `sudo mount -o loop ramdisk.image /mnt/linkstation/`.
  * cd to /mnt/linkstation/bin, and move unzip to real_unzip.
  * Add a new unzip with the following contents:
    
         #!/bin/bash
     echo "$*" >> /cmdline
     `real_unzip $*`

  * chmod a+x unzip
  * umount the image and gzip -9 it back up again.
  * Using setsum from the Kuro/Linkstation GPL toolchain, create a new firmimg.bin: ` linux-2.4.17_mvl21-sandpoint/arch/ppc/boot/utils/setsum/setsum firminfo.txt vmlinux.gz -r ramdisk.image.gz -o firmimg.bin`
  * Flash firmimg.bin to /dev/fl3.
  * Replace the original firmimg.bin in the firmware update download and re-run HD-HLAN FWUpdate.exe.
  * When the setup is done, telnet into the Linkstation and cat /cmdline.
  * See the command line used to unzip image.dat: `-P NFM_TUPSBHFNFM_TUPSBHF /mnt2/image.zip -d /mnt2 `

I confirmed the password works with 145_13, 146_10, and 147\. Have fun.

