---
layout: page
title: "The Design of a Custom 32-bit RISC CPU and LLVM Compiler Backend"
description: "My graduate project"
progressbar:
  color: "#F36E21"
---

***

As a partial requirement for my Master's degree in Electrical Engineering
I completed a research-based graduate project. To combine my love of hardware design
and computer science, I decided to design a simple 32-bit RISC CPU and write a
compiler backend able to target it using [LLVM](http://llvm.org/){:target="_blank"}.

The link to the published work can be found [below](#paper). If you want a TL;DR,
the abstract is below. If you just want to see the code, go check it out on
[GitHub](https://github.com/connorjan/llvm-cjg){:target="_blank"}!

### Abstract

*Compiler infrastructures are often an area of high interest for research. As the
necessity for digital information and technology increases, so does the need for
an increase in the performance of digital hardware. The main component in most 
complex digital systems is the central processing unit (CPU). Compilers are
responsible for translating code written in a high-level programming language to
a sequence of instructions that is then executed by the CPU. Most research in
compiler technologies is focused on the design and optimization of the code
written by the programmer; however, at some point in this process the code must
be converted to instructions specific to the CPU. This paper presents the design
of a simplified CPU architecture as well as the less understood side of
compilers: the backend, which is responsible for the CPU instruction generation.
The CPU design is a 32-bit reduced instruction set computer (RISC) and is
written in Verilog. Unlike most embedded-style RISC architectures, which have a
compiler port for GCC (The GNU Compiler Collection), this compiler backend was
written for the LLVM compiler infrastructure project. Code generated from the
LLVM backend is successfully simulated on the custom CPU with Cadence Incisive,
and the CPU is synthesized using Synopsys Design Compiler.*

<a name="paper"></a>

***

{:.text-center}
## <i class="fa fa-file-text-o" aria-hidden="true"></i> My Graduate Paper <i class="fa fa-file-text-o" aria-hidden="true"></i> 

{:.text-center}
[The Design of a Custom 32-bit RISC CPU and LLVM Compiler Backend](http://scholarworks.rit.edu/theses/9550/){:target="_blank"}
