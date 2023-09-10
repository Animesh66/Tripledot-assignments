import logging
import time
from pathlib import Path

class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        """
        This utility method is used to geerate log files when running the test.
        This log files will be generated in the Log folder in the root directory.
        The log file names will be in the name of time stamp.
        """
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        current_dir = Path().absolute().parent
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = f"{current_dir}/Logs/log{curr_time}.log"
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
