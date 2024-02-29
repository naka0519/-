import py_audio
import scanBeacon

def main():
    try:
        while True:
            # トリガーとして、ビーコンのRssiを取得
            rssi_now = scanBeacon.scanBeaconRssi()
            if (rssi_now < -15):
                py_audio.playMusic()

    except KeyboardInterrupt:
        print("finished")


if __name__ == "__main__":
    main()