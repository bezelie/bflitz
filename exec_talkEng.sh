#!/bin/bash
# 音声合成（flite）起動スクリプト
VOICEDATA=/tmp/voice.wav
sudo flite -voice "slt" -o $VOICEDATA -t $1
aplay -D plughw:0,0 $VOICEDATA
#sudo rm -f $VOICEDATA
