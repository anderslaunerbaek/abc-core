"""
"""

from confluent_kafka.serializing_producer import SerializingProducer

from abc_core.kafka.config import config
from abc_core.kafka.log import get_logger
from abc_core.kafka.registry import get_latest_topic_schema, get_schema_registry_client
from abc_core.kafka.serializer import get_serilizer_string_avro

TOPIC: str = "alp_msg"
logger = get_logger(name=__name__)


def on_delivery(err, msg) -> None:
    """_summary_

    Args:
        err (_type_): _description_
        msg (_type_): _description_
    """
    if err:
        logger.error(f"Msg failed delivery: {err}.")
    else:
        logger.info(
            f"Msg delivered to {msg.topic()} [{msg.partition()}] @ {msg.offset()}."
        )


def main():
    """_summary_"""
    logger.info("Get schema registry client.")
    schema_registry_client = get_schema_registry_client(
        config=config["schema_registry"]
    )
    logger.info(f"Get schema for topic {TOPIC}.")
    value_schema = get_latest_topic_schema(schema_registry_client, topic=TOPIC)

    logger.info(f"Add kafka configuration with `get_serilizer_string_avro()`.")
    kafka_config = config["kafka"] | get_serilizer_string_avro(
        schema_registry_client, value_schema
    )

    logger.info("Get `SerializingProducer()`.")
    producer = SerializingProducer(kafka_config)

    for i in range(100):
        producer.produce(
            topic=TOPIC,
            key=str(i),
            value={"ID": str(i), "VALUE": (i + 3)},
            on_delivery=on_delivery,
        )

    logger.info("Flush producer.")
    producer.flush()


if __name__ == "__main__":
    main()
