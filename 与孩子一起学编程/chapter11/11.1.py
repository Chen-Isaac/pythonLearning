import time
x = int(input("Countdown timer: How many?"))
for i in range (x, 0, -1):
    print i
    time.sleep(1)
print "BLAST OFF!"
