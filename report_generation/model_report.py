import datetime
from typing import List

from django.contrib.contenttypes.models import ContentType

from .base_report import BaseReport


class ModelReport(BaseReport):

    def __init__(self, report_format: str, old_instance, new_instance, lookup_fields: List[str]):
        super(ModelReport, self).__init__(report_format)
        self._old_instance = old_instance
        self._new_instance = new_instance
        self.lookup_fields = lookup_fields

        model_content_type = ContentType.objects.get_for_model(new_instance)

        self._instance_model_name = model_content_type.model
        self._instance_name = model_content_type.name

        self.title = f"Report for changes \"{self._instance_name}\""

    def generate(self):
        data = [["Property", 'Before', 'Now']]

        for field in self.lookup_fields:
            data.append([field, getattr(self._old_instance, field), getattr(self._new_instance, field)])

        adapter = self._get_adapter(
            title=self.title,
            data=data,
            section=self._instance_model_name
        )

        return adapter.generate()
