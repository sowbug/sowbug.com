+++
date = "2012-02-15T14:00:05-08:00"
title = "Wanted: CLI EDA"
+++



That's command-line interface electronic design automation.

I'm surprised that hardware engineers design schematics and circuit boards
graphically. By that I mean that they drag shapes around in a GUI editor.
Behind the scenes all the polygons and line segments are being represented
much more simply as Component A, Pin 1 being connected to Component B, Pin 2,
or Component C at position (X, Y) on the surface of the board. Nobody in
software design seriously uses graphical editors to make software, and if they
do, it still gets checked into source control as plain-text, diff-able files.

As you can probably tell, I've gotten sick of
[EAGLE](http://www.cadsoftusa.com/), and my evening investigating
[KiCad](http://kicad.sourceforge.net/) did not go well, partly because I tried
it on OS X. I'm intrigued by [gEDA](http://www.gpleda.org/), because the
project origins suggest it has been designed by people who appreciate the
modularity of Unix tools. The gEDA-generated, human-readable design files of
the [Diavolino](http://www.evilmadscientist.com/article.php/diavolino) suggest
that it's close to what I have in mind.

I don't know the first thing about autorouting algorithms, but I wonder
whether schematic and PCB layout could be looked at as a constraint-solving
problem. Component A scores higher when it's placed toward the middle of the
board, Capacitor B's traces can't be longer than N millimeters from Component
C's Vcc/GND pins, etc. A friend suggested I look at
[Minion](http://minion.sourceforge.net/), which seems to be in the right
ballpark. I think it'd be cool to edit a bunch of text source-code files (just
like VHDL!), compile them, see a PNG of the schematic and/or PCB, and then
spit out Gerbers when satisfied. I could fit circuit design more closely into
the software-design workflow I've gotten accustomed to.

