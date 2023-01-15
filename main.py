# -*- coding: utf-8 -*-
import sys

# local modules
import config
from socket_server import socket_server
from console_color import Color

  
if __name__ == "__main__":
  try:
    socket_server(config.HOST_NAME, config.PORT_NUM)
  except KeyboardInterrupt:
    print(Color.RED + "終了しています" + Color.END)
    sys.exit(0)