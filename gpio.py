# import subprocess
from subprocess import Popen, PIPE

Popen(["gpio", "mode", "6", "in"]) #Button
Popen(["gpio", "mode", "6", "down"]) #Button

### R2 ###
Popen(["gpio", "mode", "19", "out"]) #01
Popen(["gpio", "mode", "14", "out"]) #02
Popen(["gpio", "mode", "12", "out"]) #03
Popen(["gpio", "mode", "11", "out"]) #04
### U9 ###
Popen(["gpio", "mode", "2", "out"])  #01
Popen(["gpio", "mode", "5", "out"])  #02

### R1 ###
Popen(["gpio", "mode", "10", "out"]) #01
Popen(["gpio", "mode", "13", "out"]) #02
Popen(["gpio", "mode", "15", "out"]) #03
Popen(["gpio", "mode", "16", "out"]) #04
Popen(["gpio", "mode", "25", "out"]) #05
Popen(["gpio", "mode", "24", "out"]) #06
### U10 ###
Popen(["gpio", "mode", "26", "out"]) #01
Popen(["gpio", "mode", "27", "out"]) #02

### PWM ###



###gpio readall###
readall = (Popen(["gpio", "readall"], stdout=PIPE).communicate()[0].decode('UTF-8').split("\n"))
res  = []
for i in readall:
    i.split("|")
    print(i)
