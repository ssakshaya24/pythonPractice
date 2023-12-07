import time
count=3
for t in reversed(range(count+1)):
    if t>0:
        print(t,end=">>")
        time.sleep(1)
    else:
        print("Start")
