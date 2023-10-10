from abc import ABC, abstractmethod

class Payment(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """
    @abstractmethod
    def validate_identity(sefl) -> str:
        "This method is just to show the idea"
        pass

    @abstractmethod
    def validate_funds(sefl) -> str:
        "This method is just to show the idea"
        pass

    @abstractmethod
    def apply_payment(sefl) -> str:
        "This method is just to show the idea"
        pass