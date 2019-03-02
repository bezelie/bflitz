#! /bin/bash

sh exec_talkEng.sh "Start"
python3 demo_remote1.py

# イベントデバイス名の指定
EVDEV=/dev/input/event3

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
trap 'rm -rf ${FIFODIR}' 2

# イベントデバイスの監視のために evtest をバックグラウンド実行
# 実行結果は FIFO に出力する
evtest --grab "${EVDEV}" > "${FIFOFILE}" 2>&1 &
# 2>&1=標準エラー出力を標準出力にマージする
# evtest --grab "${EVDEV}" > shutter.txt 2>&1

# FIFO から1行読み込んで処理を行う
while read -r line ; do 
    # キーが離れたイベントを抽出し、キーの種類の文字列を切り出す
    UPKEY=$(echo "${line}" | grep 'EV_KEY.* value 0' | cut -d , -f 3)
    echo "${UPKEY}"
    case ${UPKEY} in
        # ENTER が押された場合
        *KEY_ENTER*)
            echo "[ENTER] Light on"
            python3 demo_remote1.py toPeople
            #sh exec_talkEng.sh "enter"
            ;;
        # VOLUME-UP が押された場合
        *KEY_VOLUMEUP*)
            echo "[VOLUP] Light off"
            python3 demo_remote1.py toMaster
            #sh exec_talkEng.sh "volume-up"
            ;;
    esac
done < "${FIFOFILE}"
