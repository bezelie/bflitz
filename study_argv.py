#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Learning Code : 引数の取得のしかた
# 

import sys
from time import sleep

print ("argv="+str(sys.argv))
print ("argv[0]="+str(sys.argv[0]))
num = len(sys.argv)
print (num)
if num > 1:
  print ("argv[1]="+str(sys.argv[1]))
  if str(sys.argv[1])=="roll":
    print ("rolling")

