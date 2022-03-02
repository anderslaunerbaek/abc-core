import logging
from typing import Dict


def get_basis_logger_config() -> Dict:
    return dict(
        level=logging.INFO,
        format=(
            "%(asctime)s.%(msecs)03d:%(levelname)s:%(module)s:%(funcName)s:%(message)s"
        ),
        datefmt="%Y-%m-%d %H:%M:%S",
    )
