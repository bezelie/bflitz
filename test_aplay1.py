#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Test Code : スピーカーテスト
# wavファイル「Front Center」をaplayで再生する。

# モジュールのインポート
from time import sleep                # ウェイト処理
import subprocess                     # 外部プロセスを実行するモジュール
import sys

# メインループ
def main():
  try:
    while (True):
      subprocess.call("aplay -l", shell=True)
      subprocess.call("aplay -D plughw:0,0 Front_Center.wav", shell=True)
      # plughw:の後の２つの数字が、カード番号とデバイス番号に合っていることを確認してください。
      sleep(0.5)
  except KeyboardInterrupt:
    print (' 終了しました')
    sys.exit(0)

if __name__ == "__main__":
    main()
