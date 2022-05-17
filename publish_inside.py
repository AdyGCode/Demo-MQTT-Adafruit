import json
import os
from random import randrange, uniform

import time
import sys
from Adafruit_IO import MQTTClient

import pymongo as pymongo
from dotenv import load_dotenv

load_dotenv(".ajg.env")

MQTT_BROKER = os.getenv('MQTT_BROKER')
MQTT_TOPIC = os.getenv('MQTT_TOPIC')
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_KEY = os.getenv('MQTT_KEY')
MQTT_PORT = os.getenv('MQTT_PORT')
MQTT_CLIENT = os.getenv('PUB_0_MQTT_CLIENT')

DELAY_TIME = 5


def handle_connect(client):
    # Subscribe to changes on the feed.
    print('Connected to Adafruit IO!')
    client.subscribe(MQTT_TOPIC)


def handle_disconnect(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)


def handle_subscribe(client, userdata, mid, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print(f"Subscribed to {MQTT_TOPIC} with QoS {granted_qos[0]}")


def handle_message(client, userdata, message):
    """
    Callback function used to work with messages received from the
    MQTT broker.

    :param client:
    :param userdata:
    :param message:
    :return:
    """
    print(f"Message: {message} from {client}")


# Create an MQTT client instance (
client = MQTTClient(MQTT_USERNAME, MQTT_KEY, MQTT_BROKER, False)

client.on_connect = handle_connect
client.on_disconnect = handle_disconnect
client.on_subscribe = handle_subscribe
client.on_message = handle_message

client.connect()

# The first option is to run a thread in the background so you can
# continue
# doing things in your program.
client.loop_background()
# Now send new values every 10 seconds.
print(
    f"Publishing a new message every {DELAY_TIME} seconds (press "
    f"Ctrl-C to quit)...")
while True:
    date_time = time.time()
    # Fake sensor data for testing
    randNumber = round(uniform(20.0, 21.0), 2)
    data = {
        'location': 306,
        'device': 'temp0577',
        'address': {
            'building': '1',
            'street': '30 Aberdeen St',
            'suburb': 'PERTH'
        },
        'data': {
            'date_time': date_time,
            'temp': randNumber
        }
    }
    jsonData = json.dumps(data)
    client.publish(MQTT_TOPIC, jsonData)
    print(f"Just published {randNumber} to topic {MQTT_TOPIC}")
    time.sleep(DELAY_TIME)
