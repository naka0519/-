from bluepy import btle
import logging
import subprocess
import datetime as dt
import time

# 使用しているビーコン
Beacon_Macaddr = "04:0d:84:7a:60:d2"

def restart_hci0(masterdate):
    #passwd = 'パスワードを入力'
    #subprocess.run(('sudo','-S','hciconfig','hci0','down'), input=passwd, check=True)
    #subprocess.run(('sudo','-S','hciconfig','hci0','up'), input=passwd, check=True)
    subprocess.run(('sudo','-S','hciconfig','hci0','down'), check=True)
    subprocess.run(('sudo','-S','hciconfig','hci0','up'), check=True)
    logging.error(f'restart bluetooth adapter [date{str(masterdate)}]')

def scanBeaconRssi():
    masterdate = dt.datetime.now()
    rssi = 0
    # エラーログの設定
    logging.basicConfig(filename="/home/pi/workdir/Otohime/Insert-music-when-you-are-in-a-bath-room/log/SensorErr.log", level=logging.INFO)

    scanner = btle.Scanner(0) # 0であること!!
    try:
        devices = scanner.scan(2, passive=True)

        for device in devices:
            if (device.addr == Beacon_Macaddr):
                rssi = device.rssi
                print(rssi)

                # csvに書き込み
                # with open('/home/pi/workdir/Otohime/Insert-music-when-you-are-in-a-bath-room/Beacon_rssi.csv', 'a') as f:
                #     writer = csv.writer(f)
                #     writer.writerow([rssi])

    except btle.BTLEManagementError:
        logging.error(f'BTLEManagementError: [date{str(masterdate)}]')
        time.sleep(0.5)
        scanBeaconRssi()
    except:
        restart_hci0(masterdate)
        time.sleep(0.5)
        scanBeaconRssi()

    return rssi


if __name__ == "__main__":
    scanBeaconRssi()