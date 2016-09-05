---
layout: page
title: Multi-Channel ADPCM CODEC
progressbar:
  color: "#F36E21"
---

During the Spring Semester of 2016 I took a class called *Advanced Topics: Digital Systems Design*.
This class, although an extension of [cell layout](/projects/cell_layouts/) course, was completely
different in content. The course focused on a semester-long design project to build a 
32 Channel ADPCM CODEC (MCAC) SoC.

I also wrote an IEEE paper on this design which can be found at the [bottom of the page](#IEEE)!

The top-down design methodology was used to design an RTL database of an MCAC based on the
ITU standards: [G.726](https://www.itu.int/rec/T-REC-G.726/en){:target="_blank"} and 
[G.711](https://www.itu.int/rec/T-REC-G.711/en){:target="_blank"}.
The entire database including the testbenches was written in Verilog. All modules were designed,
synthesized, and verified at the RTL and netlist level. Various verification strategies were used
including Verilog testbench modeling, test vector checking, and software modeling. An entire software
model of the ADPCM algorithm was written in C to generate bit exact input and output test vectors.

The final design was comprised of both and encoder and decoder which each contained:
an [OpenCores Amber ARM core](http://opencores.org/project,amber){:target="_blank"},
bus arbiter, clock generation module, time domain multiplexed (TDM) input and output modules, and a hardware co-processor.
C code was written and cross-compiled for the Amber core to manage the chip's I/O as well as some of the simple logic
for the ADPCM algorithm. The co-processor was responsible for the computational intensive parts of the algorithm. 

There were several issues encountered during the design of the MCAC. The most problematic issue our team
encountered was a timing issue. The MCAC specification was to operate on 32 channels with an 8 *kHz* frame sync which
only allows about 3.9 *&#956;s* of processing time per channel. However, in the initial design the
algorithm was taking around 15 *&#956;s*! The solution that ended up working was to fully-optimize the C
code part of the algorithm. This included "flattening" the code to remove unnecessary jumps as well as creating
look up tables (LUTs) for functions with a lot of `for` loops. Code was written to brute force the possible
inputs to various functions and create an array containing the results. Because the memory available was not
as big as an issue as the timing, this method was able to reduce the time sufficiently.

One last issue with the LUTs was encountered: during system simulations some errors were found and the root cause was
determined to be because the LUT accesses were retrieving the wrong value for a few address ranges. For these address
ranges the value was hard-coded directly in-line and the LUTs were avoided. This completely resolved the issue. The reason
why the LUT accesses were failing was never determined.

I wrote an IEEE describing the system created in much more detail. I put a lot of time into
this paper and I would highly recommend giving it a read!

<a name="IEEE"></a>

***

{:.text-center}
## <i class="fa fa-file-text-o" aria-hidden="true"></i> My IEEE Paper <i class="fa fa-file-text-o" aria-hidden="true"></i> 

{:.text-center}
[Designing a Multi-Channel ADPCM CODEC Using a Top-down Approach](/static/cjg_mcac_ieee.pdf){:target="_blank"}
