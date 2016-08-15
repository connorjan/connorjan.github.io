---
layout: page
permalink: /olympics/
title: Olympic Rings
---

<script>
var listtt = [];
function num(dots, gaps, list) {
  for (i = 0; i < dots / 2; i++) {
    var m = Math.random();
    if (m > 0.5) {
      listtt.push("1");
    } else {
      listtt.push("0");
    }
  }
  for (i = 0; i < gaps; i++) {
    listtt.push("<font style='opacity: 0;'>#</font>");
  }
  for (i = 0; i < dots / 2; i++) {
    var m = Math.random();
    if (m > 0.5) {
      listtt.push("1");
    } else {
      listtt.push("0");
    }
  }
  listtt.push("<br>");
}
function ring(x){
  var b = "";
  num(6,0,x);
  num(10,0,x);
  num(8,6),x;
  num(6,8,x);
  num(6,11,x);
  num(6,11,x);
  num(6,14,x);
  num(6,14,x);
  num(6,14,x);
  num(6,14,x);
  num(6,11,x);
  num(6,11,x);
  num(6,8,x);
  num(8,6,x);
  num(10,0,x);
  num(6,0,x);
  var b = "";
  for(i=0;i<x.length;i++){
      b = b + (x[i]);
  }
  document.write("<div class='right'>");
  document.write(b);
  document.write("</div>");
  listtt = [];
}

setInterval(function() {
  document.body.innerHTML = "";
  document.write("<style>body { text-align: center; background: #000; font-family: monospace; color: #fff; font-size: 20px; line-height: 12px; margin-top: 50px; } .right { width: 230px; height: 200px; float: left; } .right:nth-child(1){color: blue;} .right:nth-child(2){color: #fff;} .right:nth-child(3){color: red;} .bottom-holder .right:nth-child(1){color: yellow;} .bottom-holder .right:nth-child(2){color: green;} .holder { width: 690px; height: 200px; margin: 0 auto; } .bottom-holder { width: 460px; height: 200px; margin: 0 auto; transform: translateY(-95px); }</style>");
  document.write("<div class='holder'>");
  ring(listtt);
  ring(listtt);
  ring(listtt);
  document.write("</div>");
  document.write("<div class='bottom-holder'>");
  ring(listtt);
  ring(listtt);
  document.write("</div>");
}, 50);

</script>