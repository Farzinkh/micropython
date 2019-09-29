import network ##baraye vasl kardan nodemcu be wifi va dastresi be internet
import ujson ##formot ersal va daryaft request va response az server
import utime ##baray ejad delay va jologire az hang karcan
import gc ##moderiat hafeze
import urequests as requests ##baraye ertebat ba internet
from machine import Pin,ADC ##tanzem halet pin ha
adc=machine.ADC(0) ##taref pin analog
gc.enable()
led=Pin(2,Pin.OUT) 
button=Pin(0,Pin.IN)
motora1=Pin(12,Pin.OUT)
motorb1=Pin(13,Pin.OUT)
led.value(1)
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
    led.value(0)
    utime.sleep(1)
    led.value(1)
    utime.sleep(1)
    pass
  print("Connection successful")  
     
url='http://192.168.43.79:8000/delta/tele/led/'
value_list=[300,500,800,1024]
 ##list baraye tahlil rotobat
state_list=['waterlogged','dranch','damp','dry']
 ##list baraye tahlil rotobat
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
counter=0
while True:
  if button.value() == 0:
    while True:
      led.value(1)
      connect() 
      data=adc.read()##tabdel etelat az analog be digital
      for m in value_list:
        if data<=m: 
          state=state_list[counter]
          break
        else:
          counter+=1
      dade={'moisture':data,'state':state}##dade ke ghast ersal on be server ra darem
      dade_dic=ujson.dumps(dade)
      ##response=requests.post(url,data=dade,headers={'Connection':'close'})
      send=requests.request('POST', url, data=dade_dic,headers=headers, stream=False)
      ##print(send.status_code)
      ##response=requests.get(url)
      x=send.json()
      x=x['state']
      if x=='on':
        while data>300
          motora1.value(1) 
          motorb1.value(0)
          utime.sleep(0.2)
          data=adc.read()
      else  :
        motora1.value(0) 
        motorb1.value(0)
      utime.sleep(1)
      send.close()
      counter=0
      gc.collect()
  else: 
    led.value(0)
    ## press flash button to run
    pass




