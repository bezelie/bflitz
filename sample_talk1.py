#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Sample Code : 音声合成サンプル
# 

# モジュールのインポート
from time import sleep                # ウェイト処理
import subprocess                     # 外部プロセスを実行するモジュール
import sys

# 変数
ttsJpn = "exec_talkJpn.sh" # 発話シェルスクリプトのファイル名
ttsEng = "exec_talkEng.sh" # 発話シェルスクリプトのファイル名

# メインループ
def main():
  try:
    while (True):
      subprocess.call("sh "+ttsJpn+" "+"こんにちわ", shell=True)
      sleep(1)
      subprocess.call("sh "+ttsEng+" "+"Hello World!", shell=True) # English
       # Other English Voices :kal awb_time kal16 awb rms slt
      sleep(1)
  except KeyboardInterrupt:
    print (' 終了しました')
    sys.exit(0)

if __name__ == "__main__":
    main()
