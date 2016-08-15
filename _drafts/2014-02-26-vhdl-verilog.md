---
layout: post
title: VHDL vs. Verilog
---

Last semester I took a class and I learned VHDL and Verilog. I like them both but if I had to pick one favorite
I would probably pick Verilog. 

<!--more-->

The first reason is that Verilog is based on C. VHDL is based on Ada. 
I feel much more comfortable with C, and it is also used in more applications.  

As an extremely simple example, here is a simple full adder in VHDL:

```vhdl
LIBRARY ieee ;
USE ieee.std_logic_1164.all ;

ENTITY FullAdder IS
	PORT ( Cin, x, y : IN  STD_LOGIC ;
		s, Cout 	 : OUT STD_LOGIC);
END FullAdder;

ARCHITECTURE LogicFunc OF FullAdder IS
BEGIN
	s 	 <= x XOR y XOR Cin ;
	Cout <= (x AND y) OR (Cin AND x) OR (Cin AND y) ;
END LogicFunc ;
```

And here is the same adder in Verilog:

```verilog
module FullAdder (Cin, x, y, s, Cout);
	input Cin, x, y;
	output s, Cout;

		assign s = (x ^ y ^ Cin)
		assign Cout = ((x & y) | (x & Cin) | (y & Cin))
endmodule
```

Even without the Library includes in the VHDL code, the Verilog is still 3 lines shorter.
Not to mention the Verilog is easier to read and decode. This is one reason
why I like Verilog better than VHDL.