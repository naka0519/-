from bluepy import btle
from omron_env_broadcast import ScanDelegate
from datetime import datetime, timedelta
import requests

#現在時刻を取得
date = datetime.today()
#現在時刻を分単位で丸める
masterDate = date.replace(second=0, microsecond=0)
if date.second >= 30:
    masterDate += timedelta(minutes=1)

#omron_env_broadcast.pyのセンサ値取得デリゲートを、スキャン時実行に設定
scanner = btle.Scanner().withDelegate(ScanDelegate())
#スキャンしてセンサ値取得
scanner.scan(5.0)

######Googleスプレッドシートにアップロードする処理######
#センサ値がNoneでないときのみアップロード
if scanner.delegate.sensorValue is not None:
    #デバイス名
    deviceName = 'f601 omron'
    #POSTするデータ
    data = {
        'DeviceName': deviceName,
        'Date_Master': str(masterDate),
        'Date': str(date),
        'SensorType': str(scanner.delegate.sensorValue['SensorType']),
        'Temperature': str(scanner.delegate.sensorValue['Temperature']),
        'Humidity': str(scanner.delegate.sensorValue['Humidity']),
        'Light': str(scanner.delegate.sensorValue['Light']),
        'UV': str(scanner.delegate.sensorValue['UV']),
        'Pressure': str(scanner.delegate.sensorValue['Pressure']),
        'Noise': str(scanner.delegate.sensorValue['Noise']),
        'BatteryVoltage': str(scanner.delegate.sensorValue['BatteryVoltage'])
    }
    #APIのURL
    url = 'https://script.google.com/macros/s/AKfycbx8w-87bDy52e2pO7xMFHSiVQxsuPbhnrA8ZRXahOjA1NV-5AQ/exec'
    #APIにデータをPOST
    response = requests.post(url, data=data)
    #print (data["Temperature"])