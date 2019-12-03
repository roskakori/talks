"""
Simple MQTT publisher to listen for multiple topics.
"""
import argparse
import logging

from paho.mqtt import client

_log = logging.getLogger("mqtt_subscribe")


def _parsed_arguments():
    parser = argparse.ArgumentParser(__name__, "publish mqtt message")
    parser.add_argument(
        "--client",
        "-c",
        metavar="CLIENT",
        default="test_subscriber",
        help="client ID to connect with, default: %(default)s",
    )
    parser.add_argument(
        "--broker",
        "-b",
        metavar="HOSTNAME",
        default="localhost",
        help="MQTT broker to publish to, default: %(default)s",
    )
    parser.add_argument(
        "--port",
        "-p",
        metavar="PORT",
        default=1883,
        type=int,
        help="MQTT broker port to publish to, default: %(default)s",
    )
    parser.add_argument(
        "--persistent",
        "-P",
        action="store_true",
        help="ask broker to preserve messages during disconnect",
    )
    parser.add_argument(
        "--qos",
        "-q",
        metavar="QUALITY",
        default=0,
        choices=(0, 1, 2),
        type=int,
        help="MQTT quality of service, default: %(default)s",
    )
    parser.add_argument(
        "topics",
        nargs="+",
        metavar="TOPIC",
        help="MQTT topic(s) to subscribe to and log messages from",
    )
    return parser.parse_args()


def on_message(_client, _user_data, message):
    _log.info('received message for topic "%s": %s', message.topic, message.payload)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    arguments = _parsed_arguments()

    try:
        _log.info("connecting to MQTT broker %s:%d", arguments.broker, arguments.port)
        mqtt_client = client.Client(
            arguments.client, clean_session=not arguments.persistent
        )
        try:
            mqtt_client.on_message = on_message
            mqtt_client.connect(host=arguments.broker, port=arguments.port)
            for topic in arguments.topics:
                _log.info('subscribing to topic "%s" with qos=%d', topic, arguments.qos)
                mqtt_client.subscribe(topic, arguments.qos)
            _log.info("waiting for messages, press Control-C to exit")
            mqtt_client.loop_forever()
        finally:
            mqtt_client.disconnect()
    except KeyboardInterrupt:
        _log.info("interrupted by user")
    except Exception as error:
        _log.error(
            "cannot subscribe to %s:%d: %s", arguments.broker, arguments.port, error
        )
