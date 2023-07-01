from abc import ABC, abstractmethod


class HelloRepository(ABC):
    @abstractmethod
    def find(self):
        pass
