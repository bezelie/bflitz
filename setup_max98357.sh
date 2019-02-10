#! /bin/bash
# MAX98357が使えるようにラズパイの設定を変えます。

echo "Step1=/etc/modprobe.d/raspi-blacklist.conf"
sudo sed -i -e 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/' /etc/modprobe.d/raspi-blacklist.conf
sudo sed -i -e 's/blacklist snd-soc-pcm512x/#blacklist snd-soc-pcm512x/' /etc/modprobe.d/raspi-blacklist.conf
sudo sed -i -e 's/blacklist snd-soc-wm8804/#blacklist snd-soc-wm8804/' /etc/modprobe.d/raspi-blacklist.conf
echo "Step2=/etc/modules"
# disable headphone audio
sudo sed -i -e 's/snd_bcm2835/#snd_bcm2835/' /etc/modules
echo "Step3=/etc/asound.conf"
sudo cp ~/bezelie/bflitz/asound-conf.txt /etc/asound.conf
echo "Step4=/boot/config.txt"
# add device tree overlay
sudo sed -i -e 's/dtparam=audio=on/#dtparam=audio=on/' /boot/config.txt
sudo sh -c "echo dtoverlay=hifiberry-dac >> /boot/config.txt"
sudo sh -c "echo dtoverlay=i2s-mmap >> /boot/config.txt"
echo "設定完了。再起動（sudo reboot）してください"

#SLOTS=slots=snd_soc_pcm1808_adc,snd_bcm2835
#cd
#sudo sh -c "echo options snd $SLOTS"
#sudo sh -c "echo options snd $SLOTS > /etc/modprobe.d/alsa-base.conf"
#sudo sed -i -e 's/snd-pcm-oss//' /etc/modules
# sudo sh -c "echo snd-pcm-oss >> /etc/modules"
#sudo sed -i -e 's/#dtparam=i2s=on/dtparam=i2s=on/' /boot/config.txt
#sudo sed -i -e 's/dtoverlay=pcm1808-adc//' /boot/config.txt
#sudo sh -c "echo dtoverlay=pcm1808-adc >> /boot/config.txt"
