from abc import ABCMeta, abstractmethod
from collections.abc import Iterable

class DeadlineMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due():
        pass