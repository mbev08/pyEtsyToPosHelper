from pandas import read_csv
from pathlib import Path

from .inventory import Inventory


class Csv(Inventory):
    config_datetype = {
            'filename': Path,
            'directory': Path
        }

    def validate_config(self, **kwargs) -> bool:
        """
        Required config:
            - filename (Takes Priority)
            -- or
            - directory

        :param kwargs:
        :return:
        """

        try:
            kwargs['filename']
        except KeyError:
            try:
                kwargs['directory']
            except KeyError:
                raise Exception("Expecting 'filename' or 'directory' values; none were found")

        return 1


    def set_inventory_counts(self):
        pass

    def get_inventory_counts(self):
        pass


"""

class Csv(Inventory):
    filename = None
    data = None

    def __init__(self, filename):
        self.filename = filename

    def set_data(self):
        self.data = read_csv(self.filename)

"""