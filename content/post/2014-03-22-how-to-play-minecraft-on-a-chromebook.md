+++
date = "2014-03-22T15:09:00-07:00"
title = "How to play Minecraft on a Chromebook"
+++



**First Time**

  1. Get your Chromebook into [Developer Mode](http://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices).
  2. Install [Crouton](https://github.com/dnschneid/crouton). This guide will assume the installation command you use is **sudo sh -e ~/Downloads/crouton -t unity -r saucy** and that when you are asked for a new username/password, you enter **user**/**user**.  

  3. **sudo apt-get install gnome-terminal** (to avoid going crazy)
  4. ** **sudo apt-get install **python-software-properties software-properties-common**
  5. **sudo add-apt-repository ppa:minecraft-installer-peeps/minecraft-installer**
  6. **sudo apt-get update**
  7. **sudo apt-get install minecraft-installer**
  8. Just to be sure you start from a good place, reboot your Chromebook at this point.

**Each Time**

  1. Power up your Chromebook.
  2. Type Control-D at the scary screen or wait 30 seconds.
  3. Sign in as yourself or guest or whoever. Doesn't matter.
  4. Control-Alt-T to get into crosh (or better install the [Crosh Window](https://chrome.google.com/webstore/detail/crosh-window/nhbmpbdladcchdhkemlojfjdknjadhmh) utility and use that).
  5. **shell**
  6. **sudo enter-chroot**
  7. **startunity**
  8. Click on the Ubuntu circle in the upper-left and start typing **minecraft**. The icon should appear. Click on it.
  9. Play Minecraft.
  10. To switch back and forth between your Linux and ChromeOS environments, use control-alt-shift-back/forward (where back/forward are either the keys between esc and refresh on your Chromebook keyboard, or else F1 and F2 on your standard PC keyboard).

