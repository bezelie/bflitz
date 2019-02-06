#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Test Code : USBマイクテスト
# USBマイクの音をarecordで録音し、aplayで再生する。

# モジュールのインポート
from time import sleep                # ウェイト処理
import subprocess                     # 外部プロセスを実行するモジュール
import sys

# メインループ
def main():
  try:
    while (True):
      subprocess.call("arecord -l", shell=True)
      print ("３秒間の録音を開始します")
      subprocess.call("sudo arecord -d 3 -D hw:1,0 -r 44100 -f S16_LE test.wav", shell=True)
      # hw:の後の２つの数字が、カード番号とデバイス番号に合っていることを確認してください。
      sleep(3)
      print ("録音終了")
      sleep(1)
      print ("録音した音を再生します")
      subprocess.call("aplay -D plughw:0,0 test.wav", shell=True)
      sleep(4)
  except KeyboardInterrupt:
    print (' 終了しました')
    sys.exit(0)

if __name__ == "__main__":
    main()
