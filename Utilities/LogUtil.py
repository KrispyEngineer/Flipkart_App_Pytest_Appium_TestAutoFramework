import inspect
import logging


class Logger:
    @staticmethod
    def get_Logger():
        logger_name = inspect.stack()[1][3]  # fix this, we are not getting file name in the logss.
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler("..//Logs//logfile.log")

        logger.addHandler(file_handler)

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)

        return logger
