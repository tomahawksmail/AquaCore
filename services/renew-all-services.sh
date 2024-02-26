#!/bin/bash
sudo systemctl stop syssensors.service
sudo systemctl disable syssensors.service
sudo rm /etc/systemd/system/syssensors.service




sudo ln -s /home/orangepi/AquaCore/services/syssensors.service /etc/systemd/system/syssensors.service
sudo systemctl start syssensors.service
sudo systemctl enable syssensors.service
sudo systemctl daemon-reload
sudo systemctl reset-failed