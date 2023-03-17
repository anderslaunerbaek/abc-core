"""_summary_
"""
import os
import socket

config = {
    "schema_registry": {
        "url": os.getenv("SCHEMA_REGISTRY_URL", "http://dev.launer.dk:8081"),
    },
    "kafka": {
        "bootstrap.servers": os.getenv("BOOTSTRAP_SERVERS", "dev.launer.dk:29093"),
        # "security.protocol": "sasl_ssl",
        # "sasl.mechanism": "PLAIN",
        # "sasl.password": "admin",
        # "sasl.username": "admin",
        "client.id": socket.gethostname(),
    },
}
