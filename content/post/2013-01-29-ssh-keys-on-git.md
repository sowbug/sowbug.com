+++
date = "2013-01-29T21:17:39-08:00"
title = "SSH keys on Git"
+++



Long ago on a Q&amp;A site I used to frequent, I asked why GitHub didn't let
me associate a single SSH public key with two accounts. I had a work account
and a personal account on GitHub, I wanted to use them both on one computer,
and it's a pain in the neck to get Git to use the right one of multiple SSH
keys to connect to a single host. (It's solvable; you have to change your ssh
configuration to define different Hosts, each with a different key, that
resolve to the same hostname, and then tell Git to connect to a Host rather
than a hostname.) I imagined that GitHub should be able to say that if I'm
connecting to Repository X with Key A, I'd be recognized as Person M, but I'd
be recognized as Person N with the same key in Repository Y. Why couldn't
GitHub do this?

I got a perfectly reasonable answer right away on the Q&amp;A site that GitHub
uses SSH to tell who you were, so it can't be done from a technical
perspective. I found the answer wanting, though - why did GitHub use SSH? Why
couldn't the SSH identity map to a different concept? Wasn't this SSH-owns-
identity thing a big price to pay?

I got the answer while reading [Pro Git](http://git-scm.com/book/en/Git-on-
the-Server-The-Protocols). It turns out that Git doesn't know anything about
authentication, and SSH is the only practical wrapper protocol that allows
write access to a repository. (The other protocols are local file access, the
completely anonymous Git protocol, and HTTP, but none easily allows
authenticated access.) So it's likely that on a given server, the git process
is running as "you" (whoever you are who ssh'ed into the server), and the
sysadmin has set up standard Unix permissions on the .git repo directory to
control who has read/write access. Thus Git read/write operations are
automatically permitted or not without a single line of code in Git. Very
Unix-y.

Does this mean that my original feature request (SSH Key A means you're Person
M in Repo X and Person N in Repo Y) is impossible? No; there is probably a way
to map an SSH user to a specific machine user based on contextual clues like
the directory you're trying to access. But the way it is today, where SSH Key
M means you're Person M only and nobody else, is a lot easier from the
perspective of someone hacking together a young service like GitHub and making
a bunch of shell scripts that set access properly across repositories.
Moreover, it avoids the edge case where Person M joins Person N's company and
now has access to Repo Y, so the already-weirdish heuristic to determine who
you are breaks down. The higher-level solution GitHub came up with,
Organizations, solves the problem more elegantly without requiring (or
allowing) a single person to assume multiple identities on the system.

