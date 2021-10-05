import csv
import os
import logging
from abc import ABC
from csq.custom_exceptions import ReadException


class AbstractClass(ABC):
    def __init__(self):
        self.logger = self._get_logger()

    def _get_logger(self):
        logger = logging.getLogger(self.__class__.__name__)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('[%(asctime)s]-[%(name)s]-[%(levelname)s]: %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)
        return logger

    def _load_file(self, file: str) -> list:
        file_abs = os.path.abspath(file)
        self.logger.info(f'Reading {file}')
        print(file_abs)

        out_list = []
        try:
            with open(file, 'r') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=',')
                for row in csv_reader:
                    if len(row) == 1:
                        out_list.append(*row)
                    else:
                        out_list.append(row[0])
        except Exception as e:
            raise ReadException(f'Failed trying to read: {file}', e)
        return out_list

