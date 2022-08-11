import sys,os
from os.path import dirname, join, abspath
from common_utils.helpers import common_ut as common_util, custom_exception
import common_utils.logger

log_dir = "/var/log/bitgo"
log_category="scrupt"

logger = common_utils.logger.MyLogger(log_dir, log_category)


import datetime


def main():
    """
    Entry Point
    :return:
    """
    try:
        print ("BEst Wishes ")
        raise

    except Exception as e:
        error = common_util.get_error_traceback(sys, e)
        logger.error_logger(error)
        raise



if __name__ == '__main__':
    main()