from ./play_music import py_audio
from ./beacon import scanBeacon
from ./omron_env import obtainOmron_env_Light

def main():
    try:
        while True:
            # ビーコンのRssiをトリガーとした場合
            '''
            rssi_now = scanBeacon.scanBeaconRssi()
            if (rssi_now < -15):
                py_audio.playMusic()
            '''
            # omron_envの照度をトリガーとした場合
            omron_env_Light = obtainOmron_env_Light()
            if (omron_env_Light):
                py_audio.playMusic()

    except KeyboardInterrupt:
        print("finished")


if __name__ == "__main__":
    main()