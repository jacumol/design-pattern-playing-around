from __future__ import annotations
from abc import ABC, abstractmethod

class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def inventory_check(self) -> str:
        pass

    @abstractmethod
    def invoice(self) -> str:
        pass

    @abstractmethod
    def notify_client(self) -> str:
        pass

