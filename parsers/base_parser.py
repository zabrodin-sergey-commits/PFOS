from abc import ABC, abstractmethod

from models.document import Document


class BaseParser(ABC):

    @abstractmethod
    def can_parse(self, text: str):
        pass

    @abstractmethod
    def parse(self, document: Document):
        pass