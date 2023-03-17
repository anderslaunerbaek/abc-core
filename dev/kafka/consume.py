from dataclasses import dataclass

from confluent_kafka.deserializing_consumer import DeserializingConsumer

from abc_core.kafka.config import config
from abc_core.kafka.log import get_logger
from abc_core.kafka.registry import get_latest_topic_schema, get_schema_registry_client
from abc_core.kafka.serializer import Offset, get_deserilizer_string_avro

TOPIC: str = "alp_msg"
logger = get_logger(name=__name__)


@dataclass
class Model:
    ID: str
    VALUE: int


def main():
    """_summary_"""
    logger.info("Get schema registry client.")
    schema_registry_client = get_schema_registry_client(
        config=config["schema_registry"]
    )
    logger.info(f"Get schema for topic {TOPIC}.")
    value_schema = get_latest_topic_schema(schema_registry_client, topic=TOPIC)

    logger.info(f"Add kafka configuration with `get_serilizer_string_avro()`.")
    kafka_config = config["kafka"] | get_deserilizer_string_avro(
        schema_registry_client,
        value_schema,
        group_id="mygroup21",
        offset=Offset.EARLIEST,
    )

    logger.info(f"Get `SerializingProducer()` and subcribe to topic: {TOPIC}.")
    consumer = DeserializingConsumer(kafka_config)
    consumer.subscribe([TOPIC])

    while True:
        try:
            # SIGINT can't be handled when polling, limit timeout to 1 second.
            msg = consumer.poll()
            if msg is None:
                continue

            logger.info(
                (
                    f"Msg consumed from {msg.topic()} [{msg.partition()}] @ {msg.offset()} ->"
                    f" {Model(ID=msg.key(), **msg.value())}"
                )
            )
        except KeyboardInterrupt:
            break

    logger.info("Close consumer.")
    consumer.close()


if __name__ == "__main__":
    main()
