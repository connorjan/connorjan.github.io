---
layout: default
permalink: index.html
title: Home
---

# Welcome!

I am fifth year Electrical Engineering student currently 
attending <a href="http://rit.edu" target="_blank">Rochester Institute of Technology</a>. I am currently
working on my both my BS and MS degree planning to graduate with both this May! 

Last Semester I was on <a href="http://www.rit.edu/co-op.html" target="_blank">co-op</a> working at 
<a href="https://www.harris.com/" target="_blank">Harris</a>. And I can't believe I'm actually writing this,
but I am now looking for a full time position for after this school year!

See more [about me here.](/about) Also check out [my projects](/projects) or [blog](/blog)!

{% if site.twitter_widget_id %}
<div class="text-tweets">
<div class="tweets">
<a class="twitter-timeline"
  data-dnt="true"
  width="600"
  height="250"
  href="https://twitter.com/{{ site.owner.twitter }}"
  data-widget-id="{{ site.twitter_widget_id }}"
  data-tweet-limit="2"
  data-chrome="noheader nofooter noborders noscrollbar transparent">
  Recent Tweets</a>
</div>
<script>
    !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");
</script>
</div>
{% endif %}
