#IBM Watson IOT Platform
#pip install wiotp-sdk
import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "fc9jlj",
        "typeId": "device",
        "deviceId":"12345"
    },
    "auth": {
        "token": "1234567890"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if m=='sprinkleron' :
        print('sprinkler is on')
    else :
        print('sprinkler is off')
    

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(0,60)
    hum=random.randint(0,60)
    Soilmoisture=random.randint(0,10)
    myData={'Temperature':temp, 'Humidity':hum, 'Soilmoisture':Soilmoisture}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    if(Soilmoisture<=5 & temp>=20 & hum<=11):
        print('Sprinkler ON')
    else :
        print('Sprinkler OFF')
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
