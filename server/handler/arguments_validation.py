import argparse

RESERVED_PORTS_NUMBER = 1024
BIGGEST_AVAILABLE_PORT = 65535


def init_args():
    """
    Initializes commandline arguments. Defines expected arguments. May cause parser errors in case of wrong arguments.
    :return: parsed arguments
    """
    parser = argparse.ArgumentParser(
        description='This is a server for messenger')

    parser.add_argument('--port',
                        type=int,
                        help='Optional int argument with port of server')

    args = parser.parse_args()
    validate_args(args, parser)
    return args


def is_valid_port(port):
    """
    Check port for correctness. It should be in range of allowed ports.
    :param port: port to be checked
    :return: boolean result of checking
    """
    if not isinstance(port, int):
        return False
    else:
        return RESERVED_PORTS_NUMBER < port <= BIGGEST_AVAILABLE_PORT


def validate_args(args, parser):
    """
    Validates commandline arguments
    :param args: command line arguments
    :param parser: ArgumentParser object
    """

    if args.port is not None and not is_valid_port(args.port):
        parser.error(
            "port is not valid. It should be in range from {} to {}. Except got: {} ".format(RESERVED_PORTS_NUMBER,
                                                                                             BIGGEST_AVAILABLE_PORT,
                                                                                             args.port))
