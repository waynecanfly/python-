'''
author: chaofanyang
descrption: 日志类模板
'''
import logging
import logging.handlers

from logging.handlers import RotatingFileHandler


class Logger:

    def __init__(self, log_file_path : str, logger_name: str):
        self.__logger = logging.getLogger(logger_name)
        self.__logger.setLevel(logging.DEBUG)

        handler = RotatingFileHandler(log_file_path, maxBytes=10000, backupCount=1, encoding='utf-8')
        logging.root.handlers = [handler]  # werkzeug日志重定向到文件
        logging_format = logging.Formatter(
            '[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)s - %(funcName)s()][msg]%(message)s'
        )
        handler.setFormatter(logging_format)

    def get_log(self):
        return self.__logger


Logger = Logger(log_file_path='path', logger_name='name')  # 实例化