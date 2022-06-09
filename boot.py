try:
  import usocket as socket
except:
  import socket
import network
from machine import Pin
import dht
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'stormlight'
password = 'qweasd123'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

dht_pin = dht.DHT11(Pin(4)) # Uncomment it if you are using DHT11 and comment the above line