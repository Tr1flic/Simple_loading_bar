# Simple_loading_bar
It is exactly what it sounds like, it is a loading bar that you can integrate to other python projects.

Usage:
<pre>
<code>
import loading_bar
import time
for i in range(1263):
    loading_bar.progress(i, 1263)
    time.sleep(0.1)
print("Loading done!")
</code>
</pre>
