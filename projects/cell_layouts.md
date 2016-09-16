---
layout: default
title: 45 nm Standard Cell Library
banner:
  src: /static/CJG_DFFX1.png
  height: 300px
  position: 85%
  text: Standard Cell Library
  textsize: 300%
  textcolor: white
---
# 45 *nm* Standard Cell Library

During the Fall semester of 2015 I was enrolled in a class called *Design of Digital Systems*. This 
class introduced me to an entirely new stage of the digital design process I had never seen before:
cell layout design.

The class emphasized upon analytical and CAD based design methodologies equally starting from the
highest level of abstraction (RTL) to the physical implementation (layout) for many different cells.
The CAD tool used was 
[Cadence Virtuoso](https://www.cadence.com/content/cadence-www/global/en_US/home/tools/custom-ic-analog-rf-design/layout-design/virtuoso-layout-suite.html){:target="_blank"}.

Each cell was first specified in Verilog as the HDL language. Then an abstracted schematic was drawn
for the cell specifying its inputs and outputs. Once the schematic was complete the layout was drawn
using the layout editor. To verify the layout, DRC (design rule check) was used to be sure that the
layout conformed to the 45 *nm* standards for the foundry rule deck we were using. In addition, LVS (layout versus schematic)
was used to verify that the layout electrically matched to the schematic. The last step was to perform a
parasitic extraction for more accurate simulation for timing.

As the cells became more complicated, place and route tools were used to assist in the creation of
large circuits. The final cell that was designed was a 50-bit boundary scan register (BSR) to test
one of previously designed cells: a 16-bit adder. After the 50-bit BSR was designed, both the adder and BSR
were instantiated into a new project to test the adder. Using a mixed signal verification process with
a Verilog testbench was key to successfully verifying the design.

Check out my final report for the Virtuoso labs (which also includes 
data sheets for each cell designed throughout the course)
[here](/static/cjg_virtuoso_report.pdf){:target="_blank"}!
