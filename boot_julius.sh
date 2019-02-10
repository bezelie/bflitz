#!/bin/bash
# Julius（キーワード認識版）をモジュールモードで起動
# ALSADEV="plughw:1,0" /usr/local/bin/julius -w /home/pi/bezelie/dev_edgar/chatEntity.dic -C julius.jconf -module &
ALSADEV="plughw:1,0" julius -w chatEntity.dic -C julius.jconf -module
echo "Julius's Process ID = "$!
# /dev/nullはlinuxの特殊ファイルで、何も出力したくない時に指定する。
# $! = シェルが最後に実行したバックグラウンドプロセスのID
exit 0
