from __future__ import annotations
from abc import ABC, abstractmethod

from ._api_etsy import ApiEtsy
from ._csv import Csv


class InventoryCreator(ABC):

    @abstractmethod
    def create_inventory(self, **kwargs):
        pass


class InventoryCsvCreator(InventoryCreator):

    def create_inventory(self, **kwargs) -> object:
        return Csv(**kwargs)


class InventoryEtsyApiCreator(InventoryCreator):

    def create_inventory(self, **kwargs) -> object:
        return ApiEtsy(**kwargs)



