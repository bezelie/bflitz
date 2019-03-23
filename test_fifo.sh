#! /bin/bash
# FIFO(First In First Out)=名前付きファイルの使いかた

# イベントデバイス名の指定
EVDEV=/dev/input/event2

# 一時ディレクトリの作成と FIFO パスの指定
FIFODIR=$(mktemp -d) 
# mktempは一時ファイルを作成するコマンド。
# mktempに-d をつけるとファイルの代わりにディレクトリを作成できる。
# このときのパーミッションは700になる。
FIFOFILE=${FIFODIR}/ab_shutter

# FIFOの作成
mkfifo "${FIFOFILE}"
# 一時ディレクトリの中にab_shutterという名のFIFO（名前つきPIPE）を作る

# Ctrl-C で終了したときに、一時ディレクトリを消去する
#trap 'rm -rf ${FIFODIR}' 2

# イベントデバイスの監視のために evtest をバックグラウンド実行
# 実行結果は FIFO に出力する
echo "step1"
evtest --grab "${EVDEV}" > "${FIFOFILE}" 2>&1 &
echo "step2"
# 2>&1=標準エラー出力を標準出力にマージする
# evtest --grab "${EVDEV}" > shutter.txt 2>&1

# FIFO から1行読み込んで処理を行う
read -r line
echo "${line}"
