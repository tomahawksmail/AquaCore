import subprocess


subprocess.Popen(["gpio", "mode", "6", "in"]) #Button
subprocess.Popen(["gpio", "mode", "6", "down"]) #Button

### R2 ###
subprocess.Popen(["gpio", "mode", "19", "out"]) #01
subprocess.Popen(["gpio", "mode", "14", "out"]) #02
subprocess.Popen(["gpio", "mode", "12", "out"]) #03
subprocess.Popen(["gpio", "mode", "11", "out"]) #04
subprocess.Popen(["gpio", "mode", "2", "out"])  #05
subprocess.Popen(["gpio", "mode", "5", "out"])  #06

### R1 ###
subprocess.Popen(["gpio", "mode", "10", "out"]) #01
subprocess.Popen(["gpio", "mode", "13", "out"]) #02
subprocess.Popen(["gpio", "mode", "15", "out"]) #03
subprocess.Popen(["gpio", "mode", "16", "out"]) #04
subprocess.Popen(["gpio", "mode", "25", "out"]) #05
subprocess.Popen(["gpio", "mode", "24", "out"]) #06
subprocess.Popen(["gpio", "mode", "26", "out"]) #07
subprocess.Popen(["gpio", "mode", "27", "out"]) #08
### PWM ###