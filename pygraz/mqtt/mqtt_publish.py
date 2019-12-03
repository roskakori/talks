"""
Simple MQTT publisher to send a single message and exit.
"""
import argparse
import logging

from paho.mqtt import client

_log = logging.getLogger("mqtt_publish")


def _parsed_arguments():
    parser = argparse.ArgumentParser(__name__, "publish mqtt message")
    parser.add_argument(
        "--client",
        "-c",
        metavar="CLIENT",
        default="test_publisher",
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
        "--qos",
        "-q",
        metavar="QUALITY",
        default=0,
        choices=(0, 1, 2),
        type=int,
        help="MQTT quality of service, default: %(default)s",
    )
    parser.add_argument("topic", metavar="TOPIC", help="MQTT topic to publish to")
    parser.add_argument("message", metavar="MESSAGE", help="MQTT message to to publish")
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    arguments = _parsed_arguments()

    try:
        _log.info("connecting to MQTT broker %s:%d", arguments.broker, arguments.port)
        mqtt_client = client.Client(arguments.client)
        try:
            mqtt_client.connect(host=arguments.broker, port=arguments.port)
            _log.info(
                'sending message to topic "%s" with qos=%d: %s',
                arguments.topic,
                arguments.qos,
                arguments.message,
            )
            mqtt_client.publish(arguments.topic, arguments.message, arguments.qos)
            _log.info("message successfully sent")
        finally:
            mqtt_client.disconnect()
    except KeyboardInterrupt:
        _log.info("interrupted by user")
    except Exception as error:
        _log.error(
            "cannot send message to %s:%d: %s", arguments.broker, arguments.port, error
        )
