from __future__ import annotations
from abc import ABC, abstractmethod

from ._api import Api
from ._csv import Csv


class InventoryCreator(ABC):

    @abstractmethod
    def create_inventory(self, **kwargs):
        pass


class InventoryCsvCreator(InventoryCreator):

    def create_inventory(self, **kwargs) -> object:
        return Csv(**kwargs)


class InventoryApiCreator(InventoryCreator):

    def create_inventory(self, **kwargs) -> object:
        pass



