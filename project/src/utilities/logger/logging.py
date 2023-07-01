import inspect
import logging
from logging import StreamHandler, FileHandler, Formatter
from logging import INFO, DEBUG, NOTSET
import datetime
import os
from functools import wraps


class CustomFilter(logging.Filter):

    def filter(self, record):
        record.real_filename = getattr(record,
                                       'real_filename',
                                       record.filename)
        record.real_funcName = getattr(record,
                                       'real_funcName',
                                       record.funcName)
        record.real_lineno = getattr(record,
                                     'real_lineno',
                                     record.lineno)
        return True


def logger():
    log_format = '[%(asctime)s] %(levelname)s\t%(filename)s' \
                 ' - %(funcName)s:%(lineno)s -> %(message)s'
    d_today = datetime.date.today()
    stream_handler = StreamHandler()
    stream_handler.setLevel(INFO)
    stream_handler.setFormatter(Formatter(log_format))

    file_handler = FileHandler(
        f'{os.path.dirname(os.path.realpath(__file__))}/../../log/logging_{os.environ["MACHINE_ENV"]}_{d_today}.log'
    )
    file_handler.setLevel(DEBUG)
    file_handler.setFormatter(
        Formatter(log_format)
    )
    logging.basicConfig(level=NOTSET, handlers=[stream_handler, file_handler])
    logger = logging.getLogger(__name__)
    logger.addFilter(CustomFilter())
    return logger


def log(logger):

    def _decorator(func):

        # funcのメタデータを引き継ぐ
        @wraps(func)
        def wrapper(*args, **kwargs):

            func_name = func.__name__
            # loggerで使用するためにfuncに関する情報をdict化
            extra = {
                'real_filename': inspect.getfile(func) if inspect.getfile(func) is not None else "Flask",
                'real_funcName': func_name,
                'real_lineno': inspect.currentframe().f_back.f_lineno
            }

            logger.info(f'[START] {func_name}', extra=extra)

            try:
                # funcの実行
                return func(*args, **kwargs)
            except Exception as err:
                # funcのエラーハンドリング
                logger.error(err, exc_info=True, extra=extra)
                logger.error(f'[KILLED] {func_name}', extra=extra)
                raise
            else:
                logger.info(f'[END] {func_name}', extra=extra)

        return wrapper
    return _decorator
