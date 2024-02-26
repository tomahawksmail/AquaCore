#!/bin/bash
while true
do
source /home/orangepi/.virtualenvs/AquaCore/bin/activate && python /home/orangepi/AquaCore/syssensors.py && deactivate
sleep 900 # 15 min
done

