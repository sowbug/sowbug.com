+++
date = "2007-07-24T14:34:27+00:00"
title = "sowbug.org pwned"
+++



The reason I recently switched blog software and moved some stuff around on my
site is that my server got hacked. Here's the story.

I've been running a colocated server in some form or another for many years,
and have gotten lucky until now in avoiding exploits. I have always run some
version of Red Hat or Fedora Core, and have kept it updated with rhn, apt,
yum, or yum-updatesd. But there are a couple packages on my system that aren't
distributed by Fedora, so they aren't updated by those services. One such
package is Webmin. I thought I had checked the "keep Webmin updated" checkbox
on its admin page, but apparently I didn't. So I've been running a version of
Webmin from 2005 for the past couple of years, and as it turns out, that was a
bad thing.

I could go into way too much detail about how the hacking occurred, but it's
actually not that interesting. Here are the highlights:

  * On July 15, someone used what I'll call the "shell" exploit in Webmin to execute a few commands as root. This attacker downloaded and ran a Perl script that connected to another server out on the web, opening an interactive terminal. He then turned off Bash history and did who knows what, but evidence shows he changed ssh and sshd back to their default configurations, and then patched at least one other Webmin exploit on my system (in an attempt to maintain his own exclusive ownership of my server).
  * On July 19, someone _else_ logged in as one of my users and installed a crude port scanner. The reason he was able to do this was twofold and somewhat serendipitous. First, the earlier attacker reconfigured sshd to allow password logins -- previously only RSA authentication would have worked. Second, some time before July 15 the second attacker used _another_ Webmin exploit (the "unauthenticated" exploit) to take my /etc/shadow file and crack at least one password in it using a brute-force dictionary attack. In other words, the first attack enabled the second, weaker attack.
  * Reconstructing what happened caused me to discover that my /etc/shadow file (including other interesting system files) have been repeatedly stolen by various attackers since early 2006. Sigh. But because of my sshd configuration nobody was able to do anything with the information until the July 15 attacker broke in. I suspect the password in question has been cracked several times by several different people, but nothing came of it because my system didn't use passwords.

Fortunately, I don't keep anything that's both interesting and nonpublic on
the server, so getting root on it didn't enable access to anything private.
And because I keep nightly backups with a Grandfather-Father-Son rotation
scheme, I was able to rebuild it fairly quickly without data loss, and was
able to determine exactly what the attackers had done to the system by
comparing before-after snapshots.

No doubt, I felt violated. But I took some comfort in learning that of the
fellow geeks I polled who also ran their own servers on the web, 100% of them
had also experienced at least one successful attack.

