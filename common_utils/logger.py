import os
import datetime
import logging

class MyLogger:
    """
    Class For Handling Logging
    """
    def __init__(self, directory, category):
        try:
            self.category = category
            str_date = str(datetime.date.today()).replace('-', '_')
            file_path = os.path.join(directory, str_date + '.txt')
            logging.basicConfig(
                filename=file_path,
                filemode='a',
                format='%(asctime)s,%(msecs)d | %(name)s | %(levelname)s | %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                level=logging.INFO
            )
            self.logger = logging.getLogger()

        except Exception:
            print('Logging Failure')
            raise

    def msg_logger(self, msg):
        self.logger.info('-'*100)
        self.logger.info(msg)

    def error_logger(self, error):
        self.logger.error('-' * 100)
        self.logger.error(error)

        # models.insert_sql(self, 'error_logs', {
        #     'error_id': common_util.get_uuid(),
        #     'category': self.category,
        #     'error': error[:1000]
        # })

