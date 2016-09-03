---
layout: page
title: RISC 521
---

During my Fall 2015 semester I took a course called *Design of Computer Systems*. Throughout this course I
learned about various computer system architectures and advanced computing design techniques. The Fall section code
is EEEE-521 (hence this page's title of 'RISC 521').
*Some* of the topics covered in these courses were:

- Pipelining
- SIMD
- VLIW
- Loop unrolling
- Multi-core and parallel computing
- Cache & cache coherency

Each course was accompanied by a lab as well. The lab for the Fall course lab consisted of writing a relatively simple RISC
CPU in Verilog. The instruction set architecture (ISA) was given to each of the students with varying parameters. My particular
parameters were:

- 4 stage pipeline with data dependency stall logic
- 14-bit wide registers and instruction words
- Von Neumann memory architecture
- 4-way set associative L1 cache memory
	* 8 words per block
	* 4 blocks per set

In addition to the HDL design of the CPU, an assembler was written in the language of our choice. Because I had
[already written](https://github.com/connorjan/RISC-Assembler#risc-assembler){:target="_blank"} an assembler in C++
I decided to write one in python. This can be found [on my GitHub](https://github.com/connorjan/RISC521-Assembler){:target="_blank"}!
This was an extremely fun project and I ended up making an even better one (which is explained in more detail on the page about
the [RISC 721](/projects/risc_721)).

Read about the continuation (and more advanced version) of this course [here](/projects/risc_721)!
