from pandas import read_csv


class Csv:
    filename = None
    data = None

    def __init__(self, filename):
        self.filename = filename

    def set_data(self):
        self.data = read_csv(self.filename)

