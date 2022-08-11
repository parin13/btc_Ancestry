__author__ = 'parin'


class UserException(Exception):
    """
    Exception class for showing Exceptions to End User
    """
    def __init__(self, msg='Oops something went wrong!!!', code=500):
        self.code = code
        self.msg = msg
    def __str__(self):
        return repr(self.msg, self.code)

    pass