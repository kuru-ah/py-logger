from logging import Logger, config, getLogger
from pathlib import Path


def initialize_logger(name: str, logs_dir_path=None, console_level='INFO', log_level='INFO') -> Logger:
    '''
    initialize_logger is function to create a logger instance with standard settings.

    Parameters
    ----------
    name : str
        Logger name.
    logs_dir_path : _type_, optional
        Output folder of log files, by default None. (If None set "../logs/")
    console_level : str, optional
        Level of output to console, by default 'INFO'.
    log_level : str, optional
        Level of output to log file, by default 'INFO'.

    Returns
    -------
    Logger
        Logger instance with standard settings.
    '''

    # Log directory.
    if logs_dir_path is None:
        logs_dir = Path(__file__).parent.parent.joinpath('logs')  # ../logs
    else:
        logs_dir = Path(logs_dir_path)
    if not logs_dir.is_dir():
        logs_dir.mkdir()

    # Logger configuration
    logger_conf = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'NOTSET',
        },
        'loggers': {
            name: {
                'level': 'NOTSET',
                'handlers': ['console_handler', 'rotating_file_handler'],
            },
        },
        'handlers': {
            'console_handler': {
                'level': console_level,
                'formatter': 'console_formatter',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
            },
            'rotating_file_handler': {
                'level': log_level,
                'formatter': 'file_formatter',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': logs_dir.joinpath('app.log'),
                'mode': 'a',
                'encoding': 'utf-8',
                'maxBytes': 1048576,
                'backupCount': 10
            }
        },
        'formatters': {
            'console_formatter': {
                'datefmt': '%Y/%m/%d %H:%M:%S',
                'format': '%(levelname)-8s %(asctime)s; %(message)s'
            },
            'file_formatter': {
                'datefmt': '%Y/%m/%d %H:%M:%S',
                'format': '%(levelname)-8s %(asctime)s %(filename)s::%(name)s::%(funcName)s::%(lineno)s; %(message)s'
            }
        }
    }

    # Create logger
    config.dictConfig(logger_conf)
    logger = getLogger(name=name)

    return logger
