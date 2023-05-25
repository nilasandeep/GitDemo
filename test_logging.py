import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)

#file location comes from parent logging
    fileHandler = logging.FileHandler('logfile.log')
#logfile.log is the log file name, this file will be created and all logs will be directed there

#create an object for formatter
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

#passing formatter object to fileHandler to get the connection between formatter and logger thru fileHandler
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #need to pass filehandler object to this addhandler method.filehandler is just file location

#debug, ifo, warning...is the order, if we want to see only error logs, then set the level as error and then you will see only error logs and critical logs
    logger.setLevel(logging.INFO) #will show logs starting info to  ritical, will skip debug
    logger.debug("A debug statement is executed")
    logger.info("An info statement is executed")
    logger.warning("something is in warning mode")
    logger.error("A major error occured")
    logger.critical("Critical issue")

