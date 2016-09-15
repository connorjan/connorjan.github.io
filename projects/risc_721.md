---
layout: page
title: RISC 721
progressbar:
  color: "#F36E21"
---

During my Spring 2016 semester I took a continuation course called *Advanced Topics: Computer Systems Design* (EEEE-721).
This course was a continuation of the course explained [here](/projects/risc_521).

Many of the topics were the same as the previous course, however we delved into more detail for each topic we covered.
In addition we were required to do a research project on a computing topic of interest.
The topic I chose was *General Purpose Computing on GPUs* and the presentation can be viewed
[here](http://goo.gl/yqmjK5 "General Purpose Computing on GPUs"){:target="_blank"}!

The lab for this course was similar to the Fall section in that a custom RISC processor was designed in Verilog, however this design
was much more complicated. Additionally, instead of giving the instruction set architecture (ISA) to us, we first designed our own ISA
and then proceeded to design the processor. The ISA that I designed can be found [here](/static/cjg_RISC721_ISA.pdf "My ISA"){:target="_blank"}.

A quick overview of my ISA is:

- register/register data transfer
- 32-bit wide registers
- register file depth of 32 general purpose registers
- priority-encoded interrupt scheme with an interrupt vector table
- Memory mapped I/O
- 3 stage pipeline

In addition to what is described in the ISA, a custom L1 cache memory was designed. I designed the cache memory using a
relatively simple finite state machine. The purpose of designing the cache was to actually have multiple designs to 
see the difference between them. The two main designs were an 8-way set associative, and a fully associative cache.
Both designs had support for the following optimizations:

- Critical word first
- Hardware block pre-fetching
- Read priority over write on miss

The processor was designed in Altera Quartus and then testbenched in Modelsim. Once functioning, the design was tested on a
[Cyclone V FPGA](https://www.altera.com/products/boards_and_kits/dev-kits/partners/kit-terasic-cyclone-v-gx-starter.html#Overview){:target="_blank"}
using the memory mapped I/O to read from the switches and push buttons, and write output data to the LEDs and 7-segment displays. It
was very satisfying to see the design working in hardware compared to the simulations.

Similar to the [RISC 521](/projects/risc_521) lab, I wrote a custom assembler for this processor design. This was my favorite
part of the course. I could have just modified my [RISC-521 Assembler](https://github.com/connorjan/RISC521-Assembler){:target="_blank"}
however I decided to rewrite the assembler from scratch to make it much nicer. I was not completely satisfied with how the 521 assembler
turned out and I wanted to put the time into designing a proper one.

I am extremely proud of my [RISC-721 Assembler](https://github.com/connorjan/RISC-721-Assembler){:target="_blank"}. I designed the assembler
in Python using OOP methodology and made great use of inheritance. My assembler has many features as well as robust error checking
functionality for the user. An example assembly file written in my assembly language can be found [here](/static/Matrix_Assembly.png){:target="_blank"}.

The course was a lot of work and very challenging, however it caused me to think a lot and open my mind to some new methods of designing
both hardware and software.
