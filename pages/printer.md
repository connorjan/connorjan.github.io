---
layout: page
permalink: /printer/
title: Printer
---

If only there was a [shortcut](https://repl.it/DEeI){:target="_blank"}

```python
#!/usr/local/bin/python3
startPage = 105
endPage = 208
pagesOnSlide=4

front = []
back = []

counter = 0
for i in range(startPage, endPage+1):
	if counter < pagesOnSlide:
		front.append(str(i))
	else:
		back.append(str(i))
	
	counter += 1
	if counter == pagesOnSlide*2:
		counter = 0

print("FRONT:")
print(",".join(front))

if str(endPage) in front and back:
	print("\nWARNING, REMOVE LAST PAGE BEFORE PRINTING BACKS!")
	
if back:
	print("\nBACK:")
	print(",".join(back))
```

You really don't want to know.

Trust me.