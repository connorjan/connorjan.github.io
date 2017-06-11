---
layout: default
permalink: /
title: Home
---

# Welcome!

I am fifth year Electrical Engineering student currently 
attending [Rochester Institute of Technology](http://rit.edu){: target="_blank" style="color: #f36e21;"}.
I am currently working on my graduate paper which involves writing a custom
[LLVM](http://llvm.org/){:target="_blank"} backend for a custom CPU
architecture.

See more [about me here.]({{ site.url }}/about) Also check out
[my projects]({{ site.url}}/projects) or [blog]({{ site.url }}/blog)!

***

# Latest Post:

{% assign scalefactor = 80 %}
{% assign post = site.posts.first %}
{% include index_post.html %}
