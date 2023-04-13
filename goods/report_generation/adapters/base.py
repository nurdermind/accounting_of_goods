import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Union
from datetime import datetime

from django.conf import settings

class BaseReportAdapter(ABC):
    report_root_path = Path(settings.BASE_DIR) / 'goods' / 'reports'

    def __init__(self, title: str, data: List[List[Union[str, int]]], section: str = 'default'):
        self.title = title
        self.data = data

        self._section_path = self.report_root_path / section
        os.makedirs(self._section_path, exist_ok=True)

        self._file_path = self._section_path / f"{self.title}_{datetime.now()}"

    @abstractmethod
    def generate(self, ):
        pass

    @property
    def file_path(self):
        return str(self._file_path)

    @file_path.setter
    def file_path(self, value: str):
        self._file_path = Path(value)
