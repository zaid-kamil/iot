import machine
import BlynkLib
import network
import machine



#define BLYNK_TEMPLATE_ID "TMPLu7tUZeC0"
#define BLYNK_DEVICE_NAME "NodeMcu"
#define BLYNK_AUTH_TOKEN "WSdGH8Yd4qgVwdT0TuME1o1ZvZ9SPgoe"

WIFI_SSID = 'Digi'
WIFI_PASS = 'digievt132'
BLYNK_AUTH = 'WSdGH8Yd4qgVwdT0TuME1o1ZvZ9SPgoe'

wifi = network.WLAN(network.STA_IF)
if not wifi.isconnected():
    print("Connecting to WiFi...")
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASS)
    while not wifi.isconnected():
        pass

print('IP:', wifi.ifconfig()[0])

blynk = BlynkLib.Blynk(BLYNK_AUTH,insecure=True)
led = machine.Pin(2, machine.Pin.OUT)
led.on()
servo1 = machine.PWM(machine.Pin(0), freq=50)
servo2 = machine.PWM(machine.Pin(5), freq=50)

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')

@blynk.on("V0")
def v3_write_handler(value):
    print(f'Current slider 1 value: {value} {type(value)}')
    servo1.duty(int(value[0]))


@blynk.on("V1")
def v3_write_handler(value):
    print('Current slider 2 value: {}'.format(value[0]))
    servo2.duty(int(value[0]))


@blynk.on("V2")
def v1_write_handler(value):
    print('Current button value: {}'.format(value[0]))
    if value[0] == '0':
        led.on()
    elif value[0] == '1':
        led.off()



def runLoop():
    while True:
        blynk.run()
        machine.idle()

# Run blynk in the main thread
runLoop()

# You can also run blynk in a separate thread (ESP32 only)
#import _thread
#_thread.stack_size(5*1024)
#_thread.start_new_thread(runLoop, ())

