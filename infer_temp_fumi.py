import sys
from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT
import json

# local modules
from console_color import Color

# global value
import global_value as g

def infer_temp_fumi(gpio_pin: int, json_file_name: str):
  # while True:
  # get infer data
  while True:
    g.humidity, g.temperature = DHT.read_retry(DHT.DHT11, gpio_pin)
    g.humidity = int(g.humidity)
    g.temperature = int(g.temperature)
    # 異常な値なら再取得
    if (g.humidity > 90) or (g.temperature > 50):
        print("- error:", g.humidity, g.temperature)
        sleep(0.1)
        continue
    break
  
  # get now datetime
  date = datetime.now()

  # console
  print("\n+", date)
  print("| 湿度=",g.humidity, "%")
  print("| 温度=",g.temperature,"度")
  
  # write json
  now_data_dict = {"datetime": str(date), "temperature": g.temperature, "humidity": g.humidity}

  try: 
    with open(json_file_name, 'r') as f:
      data_dict: list = json.load(f)
  except (FileNotFoundError, json.decoder.JSONDecodeError):
    try:
      with open(json_file_name, 'w') as f:
        json.dump([], f)
      with open(json_file_name, 'r') as f:
        data_dict: list = json.load(f)
    except:
      print(Color.RED + "Error: JSONファイルの作成に失敗しました" + Color.END)
      sys.exit(0)
    
  data_dict.append(now_data_dict)
    
  with open(json_file_name, 'w') as f:
    json.dump(data_dict, f, indent=2)
    
  sleep(1)
    