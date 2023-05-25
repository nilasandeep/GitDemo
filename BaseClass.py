# class created as a utility for logging for using it across all tescases
import logging


class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.CRITICAL)

        return logger
# checktest_fixturesData file for the implimentaion of this utility
