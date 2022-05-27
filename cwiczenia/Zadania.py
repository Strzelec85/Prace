from progressbar import ProgressBar
import time
x=0
bar = ProgressBar(maxval=10)
bar.start()
time.sleep(x)
x = 2
bar.update(x)
time.sleep(2)
x += 2
bar.update(x)
time.sleep(2)
x += 2
bar.update(x)
time.sleep(2)
x += 2
bar.update(x)
time.sleep(2)
bar.finish()
print("Zrobione!")