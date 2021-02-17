from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Iterable
from dateutil.parser import parse
from datetime import datetime

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    @abstractmethod
    def is_due(self):
        pass

class DeadlinedReminder(ABC, Iterable):
    @abstractmethod
    def is_due(self):
        pass

class DateReminder(DeadlinedReminder):
    def __init__(self, text, date):
        self.date = parse(date, dayfirst=True)
        self.text = text
    def __iter__(self):
        text = self.text
        formatted_date = self.date.isoformat()
        return iter([text, formatted_date])
    def is_due(self):
        if self.date <= datetime.now():
            return True
        else:
            return False
