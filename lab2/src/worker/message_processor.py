from abc import ABC, abstractmethod


class MessageProcessor(ABC):
    @abstractmethod
    def validate_message(self, message: str) -> bool:
        pass
