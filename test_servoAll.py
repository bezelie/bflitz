#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Test Code : サーボ動作テスト
# 16のサーボを順に右と左に回転させる。

# モジュールのインポート
from time import sleep                # ウェイト処理
import bezelie                        # べゼリー専用モジュール
import sys                            # 最後にsys.exit(0)するために必要

# セッティング
bez = bezelie.Control()               # べゼリー操作インスタンスの生成
#bez.moveCenter()                      # サーボをセンタリング
sleep(0.5)

# メインループ
try:
  print ("開始します")
  dutyMax = 490
  dutyMin = 110
  dutyCenter = 300
  id = 1
  degree = 80
  trim = 0
  max = 490     # 下方向の限界
  min = 110     # 上方向の限界
  speed = 1
  for id in range (0, 16):
    print (id)
    now = dutyCenter
    bez.moveServo(id, 0, trim, max, min, speed, now)
    now = int((dutyMin - dutyMax) * (0 + trim + 90) / 180 + dutyMax)
    sleep(0.2)
    bez.moveServo(id, degree, trim, max, min, speed, now)
    now = int((dutyMin - dutyMax) * (degree + trim + 90) / 180 + dutyMax)
    sleep(0.2)
    bez.moveServo(id, -degree, trim, max, min, speed, now)
    now = int((dutyMin - dutyMax) * (-degree + trim + 90) / 180 + dutyMax)
    sleep(0.2)
    bez.moveServo(id, 0, trim, max, min, speed, now)
    sleep(0.5)
except KeyboardInterrupt:
  print ("  終了しました")
  sys.exit(0)
