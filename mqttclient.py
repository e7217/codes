from paho.mqtt import client as mqtt, subscribe, publish
import time


def on_connect(client, userdata, flags, rc):
    print ('connected')

def on_message(client, userdata, msg):
    print ('msg-topic : ', msg.topic)
    print ('msg-payload : ', msg.payload)
    print ('msg-timestamp : ', msg.timestamp)
    print ('msg-properties : ', msg.properties)

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(host='e7217.synology.me', port=1884)

# client.loop_forever()
client.loop_start()
client.publish(topic='/23234', payload='hello mqtt')
client.subscribe(topic='#')
time.sleep(10)
client.loop_stop()

