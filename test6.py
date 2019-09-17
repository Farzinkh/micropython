import network ##baraye vasl kardan nodemcu be wifi va dastresi be internet
import ujson ##formot ersal va daryaft request va response az server
import utime ##baray ejad delay va jologire az hang karcan
import gc ##moderiat hafeze
import urequests as requests ##baraye ertebat ba internet
from machine import Pin,ADC ##tanzem halet pin ha
adc=machine.ADC(0) ##taref pin analog
gc.enable()
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
  
connect()    
url='http://192.168.43.79:8000/delta/tele/led/'
dade={
'moisture':677
} ##dade ke ghast ersal on be server ra darem
dict={
} ##dictionary baraye daryaft response
while True:
    data=adc.read()##tabdel etelat az analog be digital
    ##response=requests.post(url,data=dade,headers={'Connection':'close'})
    send=requests.request('GET', url , json=dade , stream=False)
    ##response=requests.get(url)
    ##x=send.json()
    print(send.text)
    ##x=response.text
    ##dict=ujson.load(x)
    ##responses=ujson.load(response)
    ##response=requests.get(url)
    ##responses=response.json()
    ##print(response.text)
    ##state=responses["abas"]
    ##print(state)
    utime.sleep(3)
    send.close()
    gc.collect()


