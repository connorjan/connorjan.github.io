---
layout: post
title: "My Co-op at Harris"
progressbar:
  color: "#E21D22"
tags:
  - co-op
---

This summer I worked for [Harris](https://www.harris.com/){:target="_blank" style="color: {{ site.data.colors.Harris }};"} down in Columbia, MD.
It was a great experience; I met some really nice people and learned a ton. Overall it was a fantastic co-op.

<!--more-->

My official title was *Computer Engineer*. Although many of the specifics of my co-op are company proprietary, 
I can explain the different skills that I used and learned while working there.
My project for the entirety of the co-op was to develop tools and methods to facilitate the reverse engineering effort of a fairly
advanced and complicated control unit.

Prior to this co-op, I did not have any formal experience with reverse engineering. I was familiar with some of the broader concepts
involved but nothing more. I think one of the most important things that I had to get a grasp of was the mentality that is required to
reverse engineer something to where there is scarcely information or documentation. I had to come up with ways of finding information
and figuring things out from a perspective I have never really been exposed to before. This was both challenging and very fun.

The control unit had a very large number of interfaces and parts that I had to consider. Luckily the control unit was comprised of
one main board and I had access to more than one of them. One task I completed was having some of the BGAs removed (with the
generous help of the SMT team) and then tracing the paths to different locations on the board. This helped me find some of the serial
interfaces that were either internal to the board or went out through a connector (such as UART, RS232, and JTAG).

In addition, I also developed some tools and scripts that would aid in the reversing effort. One of the tools most complicated tools I developed strongly
revolved around serial communication. It was written in Python and made use of [pySerial](https://pythonhosted.org/pyserial/){:target="_blank"}.
This tool was able to both receive and transmit serial packets.

A [Raspberry Pi](https://www.raspberrypi.org/){:target="_blank"} was chosen as the host for some of the tools that I developed because
it is small, portable, and runs Linux. It also has other interfaces that could potentially be used on the project in the future. I was
responsible for setting up the environment for the Raspberry Pi and configuring it so that it would meet the requirements for the project.

Some less technical (but still important) tasks I was responsible for included picking various components and parts that would aid in my effort,
then writing a purchase requisition to purchase the components. I also was able to lead weekly stand-up meetings to demonstrate my
progress on the project to my supervisors.

This co-op was such an invaluable experience, not only for the technical skills that I learned, but also for the leadership experience.
Even though I was primarily the only one working on the project, I still had to create tasks and think up solutions that would
help the project progress towards its overall goals. Reverse engineering is no easy task, but it can be extremely rewarding and is very fun.
