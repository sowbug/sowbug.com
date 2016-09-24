+++
date = "2012-01-23T14:51:52-08:00"
title = "this is the version of the papilio one as built by"
+++

 ![](/tumblr_files/tumblr_ly8jejz9XD1qly645o1_1280.jpg)  

This is the version of the [Papilio One](http://papilio.cc/) as built by
[SeeedStudio](http://www.seeedstudio.com/). It's possible that versions built
by other manufacturers are slightly different; it's open-source hardware, so
in theory many people might build it. These notes are for Linux (Ubuntu 11.10
in my case).

  * The headers arrive separate from the board. You'll need to cut off sections with wire cutters, and you should expect and plan to sacrifice one pin per cut. Then if you're at all aesthetically motivated, sand down the rough edge with garnet sandpaper before soldering to the board.
  * Attaching to a VGA monitor and USB is easy enough; no surprises there. But you'll immediately wish you had a DB9-friendly joystick (buy an old Atari 2600 joystick on eBay if you want the intended hardware).
  * The first thing you'll want to do is put something on the Papilio/Arcade Wing. The [GitHub repository](https://github.com/GadgetFactory/Papilio-Arcade/) contains the stuff you need, but if you want it to work on Linux, start with [my fork](https://github.com/sowbug/Papilio-Arcade/).

The following instructions assume you're using my fork and are trying to get
Pac-Man to run on your new Papilio Arcade Wing.

  1. **cd pacman_rel004_sp3e_papilio**. All the remaining directories are relative to that one.
  2. **cd romgen_source** and build the executable: **g++ romgen.cpp -o romgen**
  3. Find Pac-Man ROMs matching those described in the top of the file scripts/merge_roms_pacman. You want the bootleg version that runs on Galaxian hardware, called Puckman. Put them in roms/.
  4. **cd scripts**
  5. **./merge_roms_pacman**

Now you've created a Xilinx bitfile that will run Pac-Man, and the next set of
instructions loads it.

  1. Download [the loader](https://github.com/GadgetFactory/Papilio-Loader/zipball/Papilio_Loader_V1.5) (that's a fragile link, sorry). We'll assume that you've managed to put papilio-prog into your path (look in the zipfile in Helper_App/linbin).
  2. **sudo apt-get install libftdi-dev**. This lets papilio-prog talk to the FTDI USB chip on the Papilio.
  3. Make sure your Papilio is plugged via USB and the VGA monitor it's connected to is on.
  4. **papilio-prog -f bit_files/pacman_on_pacman_hardware_p1_500K.bit**
  5. Within about 1500 milliseconds your VGA monitor will start running Pac-Man.

