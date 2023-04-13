from abc import ABC, abstractmethod
from typing import List

from .adapters import adapters


class BaseReport(ABC):

    def __init__(self, report_format: str):
        self.report_format = report_format
        self._adapter_class = self._get_adapter_class()

    def _get_adapter_class(self):
        if self.report_format in adapters:
            return adapters[self.report_format]
        else:
            raise ValueError("Unknown report type")

    def _get_adapter(self, title: str, data: List[List[str]], section: str):
        return self._adapter_class(title=title, data=data, section=section)

    @abstractmethod
    def generate(self):
        pass
