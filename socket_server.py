import websockets
import asyncio
from time import sleep
import json

# local modules
from console_color import Color

# global value
import config
from infer_temp_fumi import infer_temp_fumi
import global_value as g

def socket_server(host_name: str, port_num: int):
  # calls when a client connects
  async def accept(websocket, path):
    print(Color.GREEN + "クライアントと接続しました" + Color.END)
    
    while True:
      infer_temp_fumi(config.GPIO_PIN, config.JSON_FILE_NAME)
      # send websocket
      send_data = "temperature/" + str(g.temperature) + "/humidity/" + str(g.humidity)
      await websocket.send(send_data)
      print(Color.BLUE + "送信: " + send_data + Color.END)
        
  # init socket server
  start_server = websockets.serve(accept, host_name, port_num)
  print("---------------------------------------------")
  print("WebSocketサーバー起動中\n")
  print("Host: " + host_name)
  print("Port: " + str(port_num) + "\n")
  print("（終了時はxボタン、もしくはCtrl + C）")
  print("---------------------------------------------")
  
  # asynchronously wait for the server
  asyncio.get_event_loop().run_until_complete(start_server)
  asyncio.get_event_loop().run_forever()
  