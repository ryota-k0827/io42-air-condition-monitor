# io42-air-condition-monitor

## 概要
- HAL IO42 後期評定課題
- 温湿度センサーで取得したデータをWebSocketを用いて、クライアントへ送信します。
- 取得したデータはjson形式で記録されているため、過去のデータも閲覧可能。

## 環境
- Raspberry Pi 3 Model B
- DHT11 温湿度モジュール

```console
$ python -V
Python 3.9.2

$ lsb_release -a
No LSB modules are available.
Distributor ID: Raspbian
Description:    Raspbian GNU/Linux 11 (bullseye)
Release:        11
Codename:       bullseye
```

## セットアップ

### ラズパイにリポジトリをクローン
```console
$ cd $HOME/work
$ git clone git@github.com:ryota-k0827/io42-air-condition-monitor.git
```

### ライブラリをインストール
```console
$ cd $HOME
$ git clone https://github.com/adafruit/Adafruit_Python_DHT.git
$ cd Adafruit_Python_DHT/
$ sudo python3 setup.py install
$ pip install websockets
```

### クライアント側のリポジトリをクローン
```console
$ cd $HOME/html && git clone git@github.com:ryota-k0827/io42-air-condition-monitor-web.git
```

### 実行
```console
$ cd $HOME/work/io42-air-condition-monitor
$ python main.py
```
