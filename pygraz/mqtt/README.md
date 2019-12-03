# MQTT with Python

These are the slides and example code for a lightning talk given at the
PyGRAZ meetup on 2019-12-03.

## Setup

Setup a new virtual environment and activate it:
```bash
python3 -m venv venv
. venv/bin/activate
```

Upgrade pip:
```bash
pip install --upgrade pip
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Run a MQTT server

Run a moquitto MQTT server via docker using the default configuration and
listening for MQTT messages on port 1883:
```bash
docker run -it -p 1883:1883 -p 9001:9001 eclipse-mosquitto:1.6
```

## Subscribe and publish messages

Subscribe to all topics:

```bash
python3 mqtt_subscribe.py "#"
```

Publish a message:

```bash
python mqtt_publish.py --qos=1 food_topic "What a tasty schnitzel!"
```

Subscribe and preserve messages on broker even if the subscriber is
temporarily offline when a new message is published. The publisher also needs
to use qos=1:
```bash
python3 mqtt_subscribe.py --persistent --qos=1 "#"
```

Both programs support multipl options, use `--help` to learn more.
