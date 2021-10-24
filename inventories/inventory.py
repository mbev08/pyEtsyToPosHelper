from __future__ import annotations
from abc import ABC, abstractmethod


class Inventory(ABC):
    config = dict()
    config_datetype = dict()

    def __init__(self, **kwargs):
        self.config = self.set_config(**kwargs)

    def set_config(self, **kwargs):
        if self.validate_config(**kwargs):
            return kwargs

    def get_config(self, key):
        try:
            return self.config_datetype[key](self.config[key])
        except KeyError:
            raise Exception(f"Config key, {key}, does not exist or not set for inventory type.\n Config: {self.config}")

    @abstractmethod
    def validate_config(self, **kwargs) -> bool:
        pass

    @abstractmethod
    def set_inventory_counts(self):
        pass

    @abstractmethod
    def get_inventory_counts(self):
        pass

