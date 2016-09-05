---
layout: post
title: My Linux Experience
tags:
  - project
---

Three of my own recent projects have all involved linux in one way or the other. My website, my 
<a href="http://www.raspberrypi.org" target="_blank">Raspberry Pi</a>, and most recently, my custom 
<a href="http://owncloud.org" target="_blank">ownCloud server</a>.

<!--more-->

My website is hosted on a <a href="https://www.digitalocean.com" target="_blank">Digital Ocean</a> virtual server running CentOS, my Raspberry Pi 
is self-contained, and my ownCloud server is being hosted on a semi-old ASUS net-book (also running CentOS). There are
many pros and cons to each. 

Cloud hosting has been increasing in popularity recently, and for good reasons. It is extremely simple and easy to get 
a simple server started and running the server of your choice, and the maintenance is virtually worry-free. The performance 
is also usually decent for the price, depending on the provider. My website is hosted on a virtual machine on a SSD, and 
the speeds are more than satisfactory. The benefit to renting a virtual server, is that all access is granted through 
SSH and anything can be done on the server as opposed to services which host websites exclusively. 

The Raspberry Pi, though running Linux, is much different than my Digital Ocean server. Probably the most significant 
difference is the processor powering the Pi uses the ARM instruction set as opposed to the x86-64 instruction set (which
is more commonly used in computers). Many developers do not compile their programs for ARM which causes a
shortage of utilities available for the Pi. In addition, not many operating systems are available to choose from. 
Currently I am using my Pi as a VPN to access my home network remotely for files. 

Lastly is my net-book ownCloud server. This is running the newest version of CentOS 7. The ownCloud service is a custom, 
open source, virtual file manager and sync client. It is similar to the services provided by Dropbox, Box, and Mega, 
however it offers alternative functionalities. The biggest difference, in my situation, is that all of my files are stored 
on a drive that I can physically touch, making the files safer. The files are not only safer from hacks, but they are 
also safer in the sense that I will always have them, even if the servers are offline. Upload speed and download speed 
may suffer, depending on the connection speed where the net-book is located, but I am willing to sacrifice speed for 
safety. 

Overall I have become a bigger fan of Linux recently. I do not think that I will ever switch to using Linux on my own personal 
computer because of compatibility and familiarity reasons, but I do not think there is a better choice for setting up 
a server to do countless tasks, whether they be meaningful, or just for fun. 

