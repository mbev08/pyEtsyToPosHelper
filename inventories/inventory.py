from __future__ import annotations
from abc import ABC, abstractmethod


class Inventory(ABC):
    config = dict()
    config_data_type = dict()
    inventory = list()

    def __init__(self, **kwargs):
        self.set_config(**kwargs)

    def set_config(self, **kwargs):
        self.validate_config(**kwargs)

        for key, value in kwargs.items():
            if key in self.config_data_type.keys():
                self.config[key] = self.__convert_config_val_per_type(value, self.config_data_type[key])

    @staticmethod
    def __convert_config_val_per_type(config_value, data_type):
        if data_type == list:
            config_value = config_value.split(',')
            print(config_value)
        else:
            config_value = data_type(config_value)

        return config_value

    def get_config(self, key):
        try:
            return self.config_data_type[key](self.config[key])
        except KeyError:
            raise Exception(f"Config key, {key}, does not exist or not set for inventory type.\n Config: {self.config}")

    @abstractmethod
    def validate_config(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def set_inventory(self):
        pass

    def get_inventory(self):
        return self.inventory

