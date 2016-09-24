+++
date = "2005-04-20T14:57:24+00:00"
title = "tar does bzip"
+++



This is embarrassing. For years I've extracted .tar.bz2 files by the two-step
"bunzip foo.tar.bz2 &amp;&amp; tar xf foo.tar" method, but it was annoying
that tar didn't know what to do with .bz2 archives and thus wasn't as
convenient as "tar xzf foo.tar.gz." Well, last night I discovered tar's -j
option, which does the same thing for bzipped archives as -z does for gzipped
archives. Hooray!

