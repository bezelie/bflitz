#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Study Code : jsonファイルの使いかた
# jsonファイルを読み込んで、表示する

import json                   # jsonファイルを扱うモジュール

trimJson = "data_trim.json"   # 設定ファイル

f = open (trimJson,'r')
data = json.load(f)

print (data['data1'][0]['pitch'])
print (data['data1'][0]['roll'])
print (data['data1'][0]['yaw'])
