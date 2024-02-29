#!/usr/bin/env python
#-*- cording: utf-8 -*-

import pygame.mixer
import time

def playMusic():
    # ファイルPath
    MusicPath = "/home/pi/workdir/Otohime/Insert-music-when-you-are-in-a-bath-room/music_folder"
    # 音楽ファイル名（ランダムにしたい）
    MusicTitle = "/sample1.mp3"
    # mixerモジュールの初期化
    pygame.mixer.init()
    # 音楽ファイルの読み込み
    pygame.mixer.music.load(MusicPath + MusicTitle)
    # 音楽再生、および再生回数の設定(-1はループ再生)
    pygame.mixer.music.play(-1)

    time.sleep(30)
    # 再生の終了
    pygame.mixer.music.stop()

if __name__ == "__main__":
    playMusic() 