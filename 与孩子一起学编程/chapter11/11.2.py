import time
x = int(input("Countdown timer: How many?"))
for i in range (x, 0, -1):
    print i,
    for j in range (i):
        if j == i-1:
            print "*"
        else:
            print "*",
    time.sleep(1)
print "BLAST OFF!"
