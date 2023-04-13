from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer

from goods.report_generation.adapters.base import BaseReportAdapter


class PDFReportAdapter(BaseReportAdapter):

    def _get_doc(self):
        return SimpleDocTemplate(self.file_path, pagesize=letter)

    def _get_header(self):
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']

        return Paragraph(self.title, header_style)

    def _get_table(self, data):
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ]))
        return table

    def generate(self):
        doc = self._get_doc()
        header = self._get_header()
        line = Spacer(1, 20, 500)
        table = self._get_table(data=self.data)

        elements = [
            header,
            line,
            table,
        ]
        doc.build(elements)

        return self.file_path
