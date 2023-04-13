from .pdf import PDFReportAdapter

adapters = [PDFReportAdapter]


def get_adapter_class(report_format):
    for adapter in adapters:
        if adapter.is_format_supported(report_format):
            return adapter


__all__ = ['get_adapter_class']
