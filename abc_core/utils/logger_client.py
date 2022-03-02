import logging
from typing import Dict


def get_basis_logger_config() -> Dict:
    format = (
        "%(asctime)s.%(msecs)03d:%(levelname)s:%(module)s:%(funcName)s:%(message)s",
    )
    return dict(
        level=logging.INFO,
        format=format,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
