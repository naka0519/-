from bluepy import btle
from omron_env_broadcast import ScanDelegate
import pandas as pd
from datetime import datetime, timedelta
import csv
import os

#omron_env_broadcast.pyのセンサ値取得デリゲートを、スキャン時実行に設定
scanner = btle.Scanner().withDelegate(ScanDelegate())
#スキャンしてセンサ値取得（タイムアウト5秒）
scanner.scan(5.0)
#試しに照度を表示
# print(scanner.delegate.sensorValue)
# print(type(scannersystemctl.delegate.sensorValue))


#pandasでcsvに記録データを保存
# indexに時刻を設定
date = datetime.today()
masterDate = date.replace(microsecond=0)
# 列に属性のカラムを設定
# col = ['SensorType', 'Temperature', 'Humidity', 'Light', 'UV', 'Pressure', 'Noise', 'Discomfort', 'WBGT', 'BatteryVoltage']
scan_data = pd.DataFrame(scanner.delegate.sensorValue, index=[masterDate])

# print(scan_data)
# scan_data = scan_data.to_csv("omron_env_scandata.csv")
# scan_data = scan_data.to_csv("omron_env_scandata.csv", mode="a", header=False, index=[masterDate])
# fileの作成、追加を自動で行うように書き換えた
os.chdir("/home/pi/workdir/a19tn026")
with open("omron_env_scandata.csv", mode="a") as f:
    scan_data.to_csv(f, header=f.tell()==0, index=[masterDate])
