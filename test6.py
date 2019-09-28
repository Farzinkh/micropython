import network ##baraye vasl kardan nodemcu be wifi va dastresi be internet
import ujson ##formot ersal va daryaft request va response az server
import utime ##baray ejad delay va jologire az hang karcan
import gc ##moderiat hafeze
import urequests as requests ##baraye ertebat ba internet
from machine import Pin,ADC ##tanzem halet pin ha
adc=machine.ADC(0) ##taref pin analog
gc.enable()
led=Pin(2,Pin.OUT) 
##pinMode(0, INPUT_PULLUP)
button=Pin(0,Pin.IN)
def connect():
  ssid = 'Anonymous'
  password =  '6339tktz6z'    ##ssid va password wifi
 
  s = network.WLAN(network.STA_IF) ##sazekar client kardan mothole
 
  if s.isconnected() == True:
      print("Already connected")
      return
 
  s.active(True)
  s.connect(ssid, password)
  while s.isconnected() == False:
    print("connecting to wifi")
    utime.sleep(3)
    pass
  print("Connection successful")  
     
url='http://192.168.43.79:8000/delta/tele/led/'
dict={
} ##dictionary baraye daryaft response

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

while True:
  if button.value() == 0:
    while True:
      connect() 
      data=adc.read()##tabdel etelat az analog be digital
      dade={'moisture':data}##dade ke ghast ersal on be server ra darem
      dade_dic=ujson.dumps(dade)
      ##response=requests.post(url,data=dade,headers={'Connection':'close'})
      send=requests.request('POST', url, data=dade_dic,headers=headers, stream=False)
      ##print(send.status_code)
      ##response=requests.get(url)
      x=send.json()
      x=x['state']
      if x=='on':
        led.value(0)
      else  :
        led.value(1)
      ##dict=ujson.load(x)
      ##responses=ujson.load(response)
      ##response=requests.get(url)
      ##responses=response.json()
      ##state=responses["abas"]
      ##print(state)
      utime.sleep(1)
      send.close()
      gc.collect()
  else: 
    utime.sleep(0.5)        ## press flash button to run
    pass




