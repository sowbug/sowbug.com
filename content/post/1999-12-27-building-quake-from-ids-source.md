+++
date = "1999-12-27T14:36:26+00:00"
title = "Building Quake from id's source"
+++

\--- title: Building Quake from id's source mt_id: 3 layout: post date:
1999-12-27 14:36:26 +00:00 \---

If you'd like to compile Quake under Linux, [here's another tutorial (dead
link)](building_quake.html) from [Ralph Churchill](mailto:church@webzone.net).
I haven't tried it myself so please e-mail questions and comments to him.
Thanks, Ralph!

Also, to solve the mathlib.c freezing problem under MSVC 5.0, try compiling
the QuakeWorld version of the same file. That should work ok and you can just
copy the file into the WinQuake project. Also try removing lines 178 and 287
from the mathlib.c file (I haven't tried this myself so I don't know what
these lines are, but I have been told this makes it work).

#### December 26, 1999

Several people have written me about trouble getting the source to compile and
run using Visual Studio 5.0. The specific problems are:

    1\. Freezing during compilation of mathlib.c;

    2\. The QuakeWorld server freezes during runtime if compiled with the optimizations used in the VC6 project.

I don't have Visual Studio 5 so I can't reproduce these problems, but it makes
sense to create your own project (.dsp) and workspace (.dsw) files and
recreate the projects from scratch, because there may be a new option in VC6
that makes VC5 explode. Also make sure you have the latest Service Pack for VC
5, which you can get
[here](http://msdn.microsoft.com/vstudio/sp/vs97/default.asp).

If you know how to solve these problems, please write me and I'll post the
instructions here.

#### December 23, 1999

If you don't have MASM, [telefragged.com](http://www.telefragged.com) has a
[link](http://qsg.telefragged.com/tut/misc/compile.shtml) on how to get it. Or
just get it from [here](http://www.microsoft.com/ddk/download/98/BINS_DDK.EXE)
and find the file in the CAB file named BIN_WIN98_ML.EXE, and rename that to
ml.exe. Then continue with step 1 below.

This is how to get a fully functional copy of WinQuake working if you have
MASM:

1\. Install MASM if you haven't already, and add the MASM611\bin path so that
Visual Studio 6.0 can see it.

2\. Open the WinQuake workspace and set to the debug configuration. _This is
important because both the release and debug configurations of WinQuake rely
on the debug version of gas2masm!_

3\. Compile. It should work just fine.

4\. Now switch to the release configuration of the WinQuake project. Compile.
Done.

I am working on a version of the .s files in WinQuake that will compile under
[NASM](http://www.web-sites.co.uk/nasm/), but I haven't figured out how to
integrate NASM with Visual Studio 6.0. If you know how to do this, please let
me know in comments. The next step, of course, is getting it to compile under
a totally free development environment, but I know
[lots](http://www.inside3d.com/qip/home.shtml) of people are already working
on that.

#### December 22, 1999

This is how to get a marginally functional copy of WinQuake working without
MASM (but I don't think there's any reason to do this since you can get MASM
for free [here](http://www.microsoft.com/ddk/download/98/BINS_DDK.EXE)):

1\. Download the
[source](ftp://ftp.cdrom.com/pub/idgames/idstuff/source/q1source.zip) from
[ftp.cdrom.com](ftp://ftp.cdrom.com) or wherever else and unzip into some
directory somewhere.

2\. Open the WinQuake project from Visual Studio 6.0.

3\. In quakedef.h, modify line 65 which defines id386 to be 1. You want this
constant defined as 0. This is the project-wide constant that says "we are
compiling for an Intel processor and we have provided hand-optimized code from
Michael Abrash that must be compiled with an assembler."

4\. Move all the .s files within the project to a new project folder called
"Assembly files" or something like that. Then right-click that project folder,
select "settings...," and check the box that says "Exclude file from build."
These are all the files that you need MASM to compile, so what we're doing
here is setting them aside for now but not actually removing them from the
project.

5\. Add nonintel.c to the project.

6\. In sys_win.c, comment out lines 273 and 291, which cause the following
empty functions to be included:  Sys_SetFPCW(), Sys_PushFPCW_SetHigh(),
Sys_PopFPCW(),  MaskExceptions(). These are some of the functions that would
have been implemented in the .s files that we took out.

7\. In sys_win.c, add the following empty functions:

void Sys_HighFPPrecision (void)  
{  
}  
  
void Sys_LowFPPrecision (void)  
{  
}

8\. Compile. You'll get a couple warnings about functions that might not
return required results, but that's ok.

9\. Move the file WinQuake.exe that's now in the Release folder into some
other folder on your drive, and copy the ID1 folder from your Quake 1 folder
into that folder (this is just like how it already is in your Quake 1 folder).
Run it. It should work. You'll see the textures wig out from time to time and
draw gray instead of the right texture. Since the functions we stubbed out in
steps 6 and 7 all deal with particular ways to round floating-point numbers
and deal with NAN problems, I'm sure that the reason we're seeing buggy
drawing code is because it relied on these functions.

Note: After running WinQuake my Windows Start button turns blue and the
taskbar doubles its height. Go figure.

