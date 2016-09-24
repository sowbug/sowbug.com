+++
date = "2012-01-29T16:42:05-08:00"
title = "JTAG TCK: active-low?"
+++



Why does it seem like the JTAG clock signal is active low? Consider this
snippet from Xilinx's [XAPP058 source
code](https://github.com/sowbug/xapp058).

> /* toggle tck LH.  No need to modify this code.  It is output via setPort.
*/  
> void pulseClock()  
> {  
>     setPort(TCK,0);  /* set the TCK port to low  */  
>     setPort(TCK,1);  /* set the TCK port to high */  
> }

This means that when the clock isn't being pulsed, it's high. Right? If so,
why don't any [descriptions of JTAG's electrical
characteristics](http://en.wikipedia.org/wiki/Joint_Test_Action_Group#Electrical_characteristics)
say it's active low?

