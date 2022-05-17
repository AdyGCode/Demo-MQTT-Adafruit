# MQTT and MongoDB Demo (Adafruit)

This project demonstrates a simple MQTT Pub-Sub system that stores data in an external
MongoDB database. The MQTT broker used is adafruit.io's free service.

The data published is 'faked' using randomised 'temperatures' from two 'locations', inside
and outside an address.

## Requirements

Requirements are given in the [requirements.txt](requirements.txt) file.

Use `pip install -r requirements.txt` to install the required packages.

## Services Used

This project uses a free MQTT broker service and the free MongoDB Atlas service that allows
for testing of a small sharded MongoDB cluster.

### MQTT Brokers

The following brokers provide free services for testing / low data volume:

- test.mosquitto.org
- broker.hivemq.com
- iot.eclipse.org

Adafruit.io ([https://io.adafruit.com/](https://io.adafruit.com/)) provides a secured low 
volume free service that may be upscaled to larger volumes of data/events by subscription.

### MongoDB Free Service

TODO: Add details of creating free service account

## References and Readings

The following articles were used to assist in the creation of this example code:

- [MQTT Beginners Guide - Medium - Code & Dogs](https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4)
- [How to use MQTT in Python (Paho) - EMQX](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python?msclkid=fcb9d9bbcffb11ec9c672d70a8558bcd)
- [How to Use The Paho MQTT Python Client for Beginners - Steve's Internet Guide](http://www.steves-internet-guide.com/into-mqtt-python-client/)
- [Python Database Programming with MongoDB](https://voiptuts.com/python-database-programming-with-mongodb)
- [Python Database Programming with MongoDB for Beginners - Developer.com - Phil Hajjar](https://www.developer.com/languages/python-mongodb/)
- [Python and MongoDB Database Development - Developer.com - Phil Hajjar](https://www.developer.com/database/python-mongodb-no-sql/)
- [How to Use Python with MongoDB](https://www.mongodb.com/languages/python)


## Plans

- add testing 
- add flask based front end
- organise into sections using folders
