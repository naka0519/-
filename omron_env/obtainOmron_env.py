from bluepy import btle
from omron_env_broadcast import ScanDelegate
from datetime import datetime, timedelta
# import request

def obtainOmron_env_Light():
    # 時刻の取得
    date = datetime.today()
    # 分単位で出力
    masterDate = date.replace(second=0, microsecond=0)
    if date.second >= 30:
        masterDate += timedelta(minutes=1)

    #omron_env_broadcast.pyのセンサ値取得デリゲートを、スキャン時実行に設定
    scanner = btle.Scanner().withDelegate(ScanDelegate())
    #スキャンしてセンサ値取得（タイムアウト2秒）
    scanner.scan(2.0)
    #試しに照度を表示
    print(scanner.delegate.sensorValue)

    # 明るさから人感センサとして0,1(boolean)を返す処理をする
    humansensor = False # 人感センサflag
    if scanner.delegate.sensorValue['Light'] >= 50:
        humansensor = True 
    else:
        humansensor = False
    return humansensor

if __name__ == "__main__":
    obtainOmron_env_Light()