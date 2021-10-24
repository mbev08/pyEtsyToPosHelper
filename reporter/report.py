from abc import abstractmethod
from pandas import DataFrame


class Report:
    target_path = None
    raw_data = None
    formatted_data = []
    columns = []

    def __init__(self, target_path, data=None):
        self.target_path = target_path
        self.raw_data = data

    @abstractmethod
    def set_columns(self): ...

    @abstractmethod
    def create_formatted_line(self, data): ...

    def set_data(self, data):
        self.raw_data = data

    def add_formatted_row(self, line):
        print(line)
        self.formatted_data = self.formatted_data.append(line, ignore_index=True)

    def initiate_dataframe(self):
        self.formatted_data = DataFrame(columns=self.columns)

    def write_results(self):
        self.formatted_data.to_csv(self.target_path, index=False)

    @abstractmethod
    def create(self): ...





