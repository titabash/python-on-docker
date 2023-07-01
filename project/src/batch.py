import click
import json

"""
Write your module
Ex. import hoge
"""
from utilities.logger.logging import log, get_logger
from controller import hello_controller

logger = get_logger()


@log(logger)
def main_cmd(event={'default': 'value'}):
    result = hello_controller.main_batch_controller()
    print(result)
    return result


@click.command()
@click.option('--arg', '-o', default='{"data": "test"}')
def main(arg):
    """
    debug on local
    """
    arg = json.loads(arg)
    return main_cmd(arg)


if __name__ == "__main__":
    main()
