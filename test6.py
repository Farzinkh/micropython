import network
import ujson
import utime
import gc
import urequests as requests
from machine import Pin,ADC
adc=machine.ADC(0)
gc.enable()
s=network.WLAN(network.STA_IF)
s.active(True)
s.connect('Anonymous','6339tktz6z')
url='http://192.168.43.79:8000/delta/tele/led'
dade={
'state':'gogol'
}
dict={
}
dade=ujson.dumps(dade)
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
 ## print(state)
  utime.sleep(3)
  response.close()
  gc.collect()


