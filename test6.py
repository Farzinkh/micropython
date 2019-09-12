import network ##baraye vasl kardan nodemcu be wifi va dastresi be internet
import ujson ##formot ersal va daryaft request va response az server
import utime ##baray ejad delay va jologire az hang karcan
import gc ##moderiat hafeze
import urequests as requests ##baraye ertebat ba internet
from machine import Pin,ADC ##tanzem halet pin ha
adc=machine.ADC(0) ##tabdel dade aeryale be digital
gc.enable()
s=network.WLAN(network.STA_IF) ##sazekar client kardan mothole
s.active(True)
s.connect('Anonymous','6339tktz6z') ##ssid va password wifi
url='http://192.168.43.79:8000/delta/tele/led'
dade={
'state':'gogol'
} ##dade ke ghast ersal on be server ra darem
dict={
} ##dictionary baraye daryaft response
dade=ujson.dumps(dade) ##seralize kardan dade be form json
while True:
  ##response=requests.post(url,data=dade,headers={'Connection':'close'})
  response=requests.get(url , data=dade)
  print(response.text)
  ##x=response.text
  ##dict=ujson.load(x)
  ##responses=ujson.load(response)
  ##response=requests.get(url)
  ##responses=response.json()
  ##print(response.text)
  ##state=responses["abas"]
  ##print(state)
  utime.sleep(3)
  response.close()
  gc.collect()
