---
layout: page
title: High Altitude Balloon Instrumentation Platform
progressbar:
  color: "#0080FF"
banner:
  src: /static/habip_earth.jpeg
  height: 300px
  position: 40%
  text: HABIP
  textsize: 300%
  textcolor: white
---

During the 2016-2017 school year I participated in the
[Multidisciplinary Senior Design](https://www.rit.edu/kgcoe/seniordesign/){:target="_blank"}
program. I was on a team with 5 other EEs as well as 2 MEs to design an
instrumentation platform for a
[high altitude balloon](https://en.wikipedia.org/wiki/High-altitude_balloon){:target="_blank"}.
The main goals for the platform were to accomplish the following:

* Data acquisition (temperature, pressure, GPS)
* HD video and image captures
* Live NTSC analog video stream
* Live telemetry transmission over radio
* Z-axis reaction wheel control

The project was completed in 2 main phases: design, then build & implementation.
Each of which lasted for a complete semester. The design went through several
iterations over the course of the project, but the final project implemented
all of the necessary features and even exceeded some of the customer
requirements.

The final instrumentation platform contained the following features:

* 5 Raspberry Pis
* 4 HD Cameras
* 4 Analog NTSC Cameras
* 6 Custom PCB Designs
* 2 External Temperature and Pressure Sensors
* 1 Amateur 70cm TV Transmitter
* 1 Amateur 2m Amateur Radio Transceiver
* 1 APRS

Throughout the course of the project I was mainly responsible for leading the 
development of the embedded software as well as assisting in the design of the
custom PCB for the communications system.

This was the first experience I had with PCB design and I enjoyed it
thoroughly. The PCB included two major power management circuits for two
batteries, several I2C sensors (including a GPS), an analog video multiplexer,
and many connectors for the analog cameras, antennas, and several other signals
that went to other parts of the platform.

The software needed for the
communications system was mostly written in Python for the Raspberry Pi and was
responsible for controlling the Communications systems. This included
controlling power to the analog cameras and the analog on-screen display (OSD),
sending data to the OSD to be displayed on the live video transmission, 
transmitting/receiving data over the 2m Amateur Radio, communicating
with several sensors on an I2C bus, and also communicating to an MSP430 located
on another board over SPI.This was all extremely fun to write and it was
especially exciting to be writing code that would interact with our custom PCB.

The final platform was launched on April 29, 2017. The launch was very
successful. We launched from a parking lot at RIT at around 11:50 AM and the
platform landed near Syracuse at 1:20 PM. We successfully tracked the platform
for a majority of its flight through both the APRS and by the 2m Amateur Radio
Transceiver. The platform sustained some minor damages on landing, however was
in good condition considering it impacted while descending at roughly 20 MPH.

The entirety of the project was very fun. It was extremely satisfying to go from
just a list of customer requirements to an actual product that was functional by
the end of the course. I learned a lot about the life-cycle of a product and
think it was a great experience.

## External Links

* [GitHub Repo](https://github.com/TightSquad/HABIP){:target="_blank"}
* [School Project Website](http://edge.rit.edu/edge/P17104/public/Home){:target="_blank"}
* [Team Technical Paper]({{ site.url }}/static/habip_paper.pdf)
