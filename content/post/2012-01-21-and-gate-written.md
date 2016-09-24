+++
date = "2012-01-21T17:04:35-08:00"
title = "AND gate written"
+++



I got something to build in the Xilinx ISE:

    
    
    library IEEE;
    use IEEE.STD_LOGIC_1164.ALL;
    
    entity foo is
        Port ( port0 : in  STD_LOGIC;
               port1 : in  STD_LOGIC;
               port_out : out  STD_LOGIC);
    end foo;
    
    architecture Behavioral of foo is
    begin
     port_out <= port0 and port1;
    end Behavioral;

All it does is (in theory) set a high voltage on one pin when a high voltage
is set on two other pins. But it's a start.

