import logging
from typing import Dict


def get_basis_logger_config_parms() -> Dict:
    return dict(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d:%(levelname)s:%(module)s:%(funcName)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'

    )



def main():
    print(get_basis_logger_config_parms())



if __name__ == "__main__":
    main()
