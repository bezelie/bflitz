#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Demo Code : 
# 

# モジュールのインポート
from time import sleep     # ウェイト処理
import bezelie             # べゼリー専用モジュール
import subprocess          # 外部プロセスを実行するモジュール
from random import randint
import sys                 # 引数を取得するために必要

# セッティング
ttsJpn = "exec_talkJpn.sh" # 日本語発話シェルスクリプトのファイル名
ttsEng = "exec_talkEng.sh" # 英語発話シェルスクリプトのファイル名
bez = bezelie.Control()               # べゼリー操作インスタンスの生成

# メインループ
if len(sys.argv)>1:
  comm1 = str(sys.argv[1])
  if randint(1,2)==1:
    print ("speak to people")
    r = randint(1,4)
    if r == 1:
      cmds = ['sh',ttsEng, 'hello-human-beings'] # 
    elif r == 2:
      cmds = ['sh',ttsEng, 'how-are-you?'] #
    elif r == 3:
      cmds = ['sh',ttsEng, 'my-name-is-bezelie'] #
    else:
      cmds = ['sh',ttsEng, 'nice-to-meet-you'] #
    proc = subprocess.Popen(cmds, stdout=subprocess.PIPE) # コマンドの呼び出し
    sleep(0.5)
    bez.moveYaw(1,0)
    sleep(0.5)
    bez.movePitch(1,0)
    sleep(0.2)
    bez.moveRoll(1,20)
    sleep(0.5)
    bez.moveRoll(1,-20)
    sleep(0.5)
    bez.moveRoll(1,0)
    sleep(0.5)
    proc.communicate() # コマンド実行プロセスが終了するまで待機
  else:
    print ("spkeak to master")
    r = randint(1,4)
    if r == 1:
      cmds = ['sh',ttsEng, 'Hi-master'] # 
    elif r == 2:
      cmds = ['sh',ttsEng, 'may-I-help-you?'] #
    elif r == 3:
      cmds = ['sh',ttsEng, 'you-look-great!'] #
    else:
      cmds = ['sh',ttsEng, 'I-love-you'] #
    proc = subprocess.Popen(cmds, stdout=subprocess.PIPE) # コマンドの呼び出し
    bez.moveYaw(1,20)
    sleep(1)
    bez.movePitch(1,20)
    sleep(0.5)
    bez.moveRoll(1,20)
    sleep(0.5)
    bez.moveRoll(1,0)
    sleep(0.5)
    proc.communicate() # コマンド実行プロセスが終了するまで待機
