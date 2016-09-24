+++
date = "2001-08-07T13:31:28+00:00"
title = "Windows Programming Tips"
+++



### Wise guidelines to follow when working on team programming projects

#### Be friendly to team members who don't know your code as intimately as you
do or who shouldn't need to be familiar with it

Choose filenames that do not include magic words like "error," "warning," or
"project." When a build engineer (or you when the build engineer has gone
home) needs to find certain events in a build log such as all errors in a
50-project product build, it helps not to turn up false positives like
"errordisplay.h."

When choosing file and target names, make life easy for your fellow grepping
developer. For example, if your team is working on the Foo Project and you've
chosen FP as the prefix for your file and target names (FPMain.c,
FPDocument.h, FPHelper.exe), avoid names that will turn up in every search
(FP.DLL, fp.c, fp.h).

Use a consistent commenting style. If you usually type pending(miket): fix
this, never type pending (miket): fix this. Sometimes, comments are the only
element of source code that enables someone else to find every area affected
by a code change. If you think of comments as grep-friendly tags rather than
just notes to yourself, they'll become a reliable (though last-ditch) method
to locate important parts of code.

#### Anticipate the questions and needs that product marketing and QA will
have

Decide what's going to be user-visible and what won't be, and keep a clear
distinction between the two.  If there's any possibility that the product name
will change at the last minute from Foo to Bar (and that **always** happens),
you as an engineer should be able to say the following:

> _Yes, we can make that change by modifying one header file and three
resource scripts. No code will change. No build steps will change. In fact,
this job is perfect for our junior engineer who started on Monday. I will tell
him or her the names of the header file and the resource scripts, and he or
she will be able to do this task without knowing anything at all about our
code._

Along the same lines, there will be some items that will always be hard to
change, such as a shared library filename that is a dependency for every other
binary in your released product.  Choose filenames in a way that avoids their
being tightly wedded to a brand or product name. Most modern operating systems
provide a way for files to describe themselves nicely (MacOS and Windows give
you standardized version resources, for example).  That's where the brand
names, product names, trademarks, descriptions, and any other user-visible
text should go.

And finally, a tip particular to Windows: seriously consider using GUIDs as
registry key names. The Windows Registry is a shadowy area between user-
visible and opaque binary parts of a product. Somehow, though it's the most
dangerous part of the system for a non-engineer to manipulate, every product
manager and QA tester seems to know how to type "regedit" at a command prompt
and start browsing the Registry "just to see what's there." This is exactly
like a product manager opening a hex editor and looking at a binary file "just
to see what's there," but the reason that never happens is because Windows
doesn't ship with any nice friendly-looking GUI hex editors. There are many
examples of registry keys in the current Windows Registry where the current
product name doesn't match the product name in the Registry, and each of those
surely caused a conniption at some software company when the product manager
or QA started logging bugs about how the registry key still had the old
product name. A GUID avoids this problem. It's exactly what an engineer needs:
a guaranteed unique path to find certain data pertaining to a software
project, and using a GUID instead of a product name makes sure that nobody
mistakenly believes it's anything more than that.

#### Learn how to use your source control system

Don't use branching or tagging technology in your source control system as
_product_ version control.  If you find yourself branching the tree and having
to copy and paste your code changes to two or more live branches repeatedly,
it's likely you're misusing the system.  What you've effectively done is asked
the system to handle an extra dimension -- not just a history of changes
within a series of files, but also multiple series of files, which by now have
only an incidental relationship to each other (as opposed to the traditional
use of branching, which is to preserve the state of the 1.0 product to allow
maintenance releases, while work continues on the 1.1 release. Once the 2.0
product is begun and it's meant to be a clean break from the 1.0 product, it
makes more sense to start a brand-new source tree).

### Windows programming tips

_Platform SDK_: All the free stuff you need to develop for Windows. Get this,
a text editor, a compiler, and a linker, and you can develop Windows programs.
The Platform SDK is usually more up-to-date than the subset of tools,
libraries, and header files you get with Visual Studio, so it makes sense to
have both Visual Studio and the Platform SDK installed on your system.

_dumpbin.exe_: a utility that comes with Visual Studio and is also available
in the Platform SDK. This thing extracts useful information from binary images
(.exe, .dll, .cpl). Two invaluable functions are disassembling binaries and
seeing which functions they export.

_depends.exe_: a utility that comes with Visual Studio and is also available
in the Platform SDK. GUI-based; tells you lots of good stuff about binary
images. A normal installation of Visual Studio usually registers this
application to handle certain filetypes, such as DLLs, so opening a DLL from
Windows Explorer takes you right to Depends.

_.map file_: lists the addresses where interesting things start in a binary
image. If a program crashes at a particular address, you can use the map file
to guess which function it was in where it crashed (and you can disassemble
the binary with dumpbin to find the exact instruction).

_Why do I get these weird debug assertion failures saying my heap's corrupted
when I know it isn't?_ Chances are you're using different versions of the C
runtime library within the same process (e.g., foo.exe is compiled with the
debug multithreaded DLL runtime, and a dependency, bar.dll, was compiled with
debug multithreaded).

(Not a Windows programming tip): _God damn it, I just pressed send by mistake
before I finished that e-mail. Can you help me?_ No, but next time you might
want to start getting in the habit of putting the addressee in last, assuming
you're using an e-mail client that lets you tab around from field to field.
Then you **can't** send the e-mail until you really mean it.

