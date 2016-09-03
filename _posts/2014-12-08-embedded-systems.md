---
layout: post
title: Embedded Systems Design
---

This semester (Fall 2014) I learned a lot about embedded systems design. It has been
one of the most fun and interesting classes that I have taken so far. 
The topics that I learned about were very practical, and it seemed like
everything that I learned can be easily applied to problems and applications.

<!--more-->

The lab section of the class was even more fun. Projects and programs were
written using both C and assembly for a microcontroller- specificially the
[MSP430](http://www.ti.com/product/msp430g2553){:target="_blank"}. 
This was a great microcontroller to practice with because it has a lot of hardware 
built in, but it is also used a fair amount in real projects as opposed to just 
learning environments.

The hardware in the microcontroller that was used:

- Temperature Sensor
- Timers
- ADC
- UART
- GPIO

In addition, I used an external 
<a href="http://www.ti.com/tool/430boost-sense1" target="_blank">capacitive touch board</a>
with the microcontroller. This capacitive touch sensor along with the LEDs
provided an easy way to input and output from the microcontroller. 

The final project was a large task. A program needed to be written to take inputs from both
the capacitive touch screen and from the GPIO pins, then modify them in software, then display 
the modified values back out onto the LEDs. Both C and assembly was used leading up to this 
project, and it was a lot of fun designing the program. 

The lab report for this project can be found here: <br>
<a href="/static/embedded_systems_report.pdf">Embedded Systems: Final Project Report</a>
