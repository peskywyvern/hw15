# Write a context manager Logger that provides an object for logging data and
# writing it to a file.
# Logger must have log method that takes any value and writes it into a file
# A filename must be specified when calling context manager.
# You must provide a timestamp (just use time.time()) for every new line
# in file.


import time


class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(f'files/{self.filename}', 'a')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def write(self, value):
        self.file.write(f'[{time.time()}]   {value} \n')


# example:
with Logger('log1.txt') as logger:
    logger.write(12 + 14)
    logger.write('Hello World')
    logger.write(True)

# this code must create log1.txt file with the following structure:
# [timestamp] 26
# [timestamp] Hello World
# [timestamp] True
#
# where timestamp is the result of time.time() call
