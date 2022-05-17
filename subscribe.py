import json
import os

# import time
import sys
from Adafruit_IO import MQTTClient

import pymongo as pymongo
from dotenv import load_dotenv

# do not put anything in the () to use the default .env file
load_dotenv('.ajg.env')

MQTT_BROKER = os.getenv('MQTT_BROKER')
MQTT_TOPIC = os.getenv('MQTT_TOPIC')
MQTT_CLIENT = os.getenv('SUB_MQTT_CLIENT')
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_KEY = os.getenv('MQTT_KEY')
MQTT_PORT = os.getenv('MQTT_PORT')

DB_TYPE = os.getenv('DB_TYPE')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')


def get_database():
    """
    Create DB client connection to MongoDB Server and Database

    :return: Database Connection
    """
    connection_str = f"{DB_TYPE}://{DB_USER}:{DB_PASS}@{DB_HOST}"
    db_client = pymongo.MongoClient(connection_str)
    return db_client[DB_NAME]


def handle_message(client, userdata, payload):
    """
    Callback function used to work with messages received from the
    MQTT broker.

    :param client:
    :param userdata:
    :param message:
    :return:
    """
    message_str = payload
    print(f"Message: {message_str} from {client}")
    data_dict = json.loads(message_str)
    db_client_database.test.insert_one(data_dict)


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


# Create connection to DB and MQTT broker
db_client_database = get_database()
print("Connected to MongoDB")

# Create an MQTT client instance (
client = MQTTClient(MQTT_USERNAME, MQTT_KEY, MQTT_BROKER, False)

client.on_message = handle_message
client.on_connect = handle_connect
client.on_disconnect = handle_disconnect
client.on_subscribe = handle_subscribe

client.connect()

# Start a message loop that blocks forever waiting for MQTT messages
# to be received.  Note there are other options for running the event
# loop like doing so in a background thread.
client.loop_blocking()
