from .pdf import PDFReportAdapter


adapters = {
    'pdf': PDFReportAdapter,
}

__all__ = ['PDFReportAdapter']