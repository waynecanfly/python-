'''
author: chaofanyang
descrption: 日志类模板
'''
import logging
from logging import handlers

def Singleton(cls):
    """
    单例模式
    :param cls:
    :return:
    """
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            process_name = 'Zoom.exe'
            # 判读是否已经启动，启动就将进程杀死
            if proc_exist(process_name):
                # 通过进程名称杀死进程
                os.system('taskkill /f /im %s' % process_name)
                time.sleep(2)
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class Logger:
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
    }

    def __init__(self, log_file_path : str, logger_name: str, level='info', fmt='[%(asctime)s][%(levelname)s][%(pathname)s:%(lineno)s - %(funcName)s()][msg]%(message)s'):
        self.logger = logging.getLogger(logger_name)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        sh = logging.StreamHandler()  # 向屏幕输出
        sh.setFormatter(format_str) # 设置屏幕输出格式
        th = handlers.TimedRotatingFileHandler(filename=log_file_path, encoding='utf-8')
        th.setFormatter(format_str)
        self.logger.addHandler(sh)
        self.logger.addHandler(th)
