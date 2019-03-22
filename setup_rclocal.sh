#! /bin/bash
# 
# BASE=/home/pi/bezelie/bflitz
sudo sed -i -e "s|su -l pi -c $BASE/Remocon/start.sh \&||" /etc/rc.local
sudo sed -i -e "s|$BASE/poweroff.py \&||" /etc/rc.local
sudo sed -i -e 's/exit 0//' /etc/rc.local
sudo sh -c "echo $BASE/poweroff.py \& >> /etc/rc.local"
sudo sh -c "echo su -l pi -c $BASE/Remocon\/start.sh \& >> /etc/rc.local"
sudo sh -c "echo exit 0 >> /etc/rc.local"
