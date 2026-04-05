#!/usr/bin/env python3
"""
PDF Generator Utility for TCS NQT Preparation Materials
Generates professional-looking PDFs with proper formatting
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether
)
from reportlab.lib import colors
from datetime import datetime
import os


class TCSNQTPDFGenerator:
    """Generate professional PDFs for TCS NQT preparation materials"""

    def __init__(self, output_path, title, subject):
        self.output_path = output_path
        self.title = title
        self.subject = subject
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        self.doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=0.75 * inch,
            leftMargin=0.75 * inch,
            topMargin=1 * inch,
            bottomMargin=0.75 * inch
        )
        self.styles = getSampleStyleSheet()
        self.story = []
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Create custom styles for better formatting"""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Title'],
            fontSize=24,
            textColor=colors.HexColor('#1a237e'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='Question',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#212121'),
            spaceAfter=10,
            spaceBefore=15,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='Option',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=20,
            spaceAfter=5,
        ))

        self.styles.add(ParagraphStyle(
            name='Answer',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#1b5e20'),
            leftIndent=20,
            spaceAfter=5,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='Explanation',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=20,
            spaceAfter=15,
            alignment=TA_JUSTIFY
        ))

        self.styles.add(ParagraphStyle(
            name='TopicHeader',
            parent=self.styles['Heading1'],
            fontSize=16,
            textColor=colors.HexColor('#0d47a1'),
            spaceAfter=20,
            spaceBefore=30,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='SubtopicHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#1565c0'),
            spaceAfter=15,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='CodeBlock',
            parent=self.styles['Normal'],
            fontSize=9,
            fontName='Courier',
            leftIndent=20,
            spaceAfter=10,
            spaceBefore=5,
            backColor=colors.HexColor('#f5f5f5'),
        ))

        self.styles.add(ParagraphStyle(
            name='Tip',
            parent=self.styles['Normal'],
            fontSize=10,
            leftIndent=20,
            spaceAfter=10,
            textColor=colors.HexColor('#e65100'),
            fontName='Helvetica-Oblique'
        ))

        self.styles.add(ParagraphStyle(
            name='SectionIntro',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=12,
            alignment=TA_JUSTIFY,
            textColor=colors.HexColor('#424242')
        ))

    def add_cover_page(self):
        """Add professional cover page"""
        self.story.append(Spacer(1, 2 * inch))
        self.story.append(Paragraph(self.title, self.styles['CustomTitle']))
        self.story.append(Spacer(1, 0.5 * inch))
        self.story.append(Paragraph(
            f"<b>{self.subject}</b>",
            ParagraphStyle('CoverSubtitle', parent=self.styles['Heading2'], alignment=TA_CENTER)
        ))
        self.story.append(Spacer(1, 0.3 * inch))
        info_text = (
            f'<para alignment="center">'
            f'<b>TCS NQT Preparation Material</b><br/>'
            f'Generated on: {datetime.now().strftime("%B %d, %Y")}<br/>'
            f'</para>'
        )
        self.story.append(Paragraph(info_text, self.styles['Normal']))
        self.story.append(PageBreak())

    def add_topic_header(self, topic_name, description=None):
        """Add a topic header"""
        self.story.append(Paragraph(topic_name, self.styles['TopicHeader']))
        if description:
            self.story.append(Paragraph(description, self.styles['SectionIntro']))
            self.story.append(Spacer(1, 12))

    def add_subtopic_header(self, subtopic_name):
        """Add a subtopic header"""
        self.story.append(Paragraph(subtopic_name, self.styles['SubtopicHeader']))

    def add_question(self, q_number, question_text, options=None,
                     answer=None, explanation=None, difficulty=None,
                     source=None):
        """Add a question with options, answer, and explanation"""
        elements = []

        meta_parts = []
        if difficulty:
            meta_parts.append(f"[{difficulty}]")
        if source:
            meta_parts.append(f"<i>(Source: {source})</i>")
        if meta_parts:
            elements.append(Paragraph(
                f"<b>Q{q_number}.</b> " + " ".join(meta_parts),
                self.styles['Normal']
            ))

        elements.append(Paragraph(
            f"<b>Q{q_number}.</b> {question_text}" if not meta_parts else question_text,
            self.styles['Question']
        ))

        if options:
            for opt_key, opt_value in options.items():
                elements.append(Paragraph(
                    f"<b>{opt_key})</b> {opt_value}",
                    self.styles['Option']
                ))

        if answer:
            elements.append(Spacer(1, 8))
            elements.append(Paragraph(
                f"<b>Answer:</b> {answer}",
                self.styles['Answer']
            ))

        if explanation:
            elements.append(Paragraph(
                f"<b>Explanation:</b> {explanation}",
                self.styles['Explanation']
            ))

        self.story.append(KeepTogether(elements))
        self.story.append(Spacer(1, 15))

    def add_formula_section(self, formula_name, formula, description=None):
        """Add a formula with description"""
        elements = []
        elements.append(Paragraph(f"<b>{formula_name}</b>", self.styles['Question']))
        elements.append(Paragraph(
            f"<font name='Courier'>{formula}</font>",
            self.styles['Normal']
        ))
        if description:
            elements.append(Paragraph(description, self.styles['Explanation']))
        self.story.append(KeepTogether(elements))
        self.story.append(Spacer(1, 12))

    def add_text(self, text, style='Normal'):
        """Add a paragraph of text"""
        self.story.append(Paragraph(text, self.styles[style]))
        self.story.append(Spacer(1, 8))

    def add_tip(self, tip_text):
        """Add a tip/note"""
        self.story.append(Paragraph(f"Tip: {tip_text}", self.styles['Tip']))

    def add_code_block(self, code_text):
        """Add a code block"""
        self.story.append(Paragraph(
            code_text.replace('\n', '<br/>').replace(' ', '&nbsp;'),
            self.styles['CodeBlock']
        ))

    def add_table(self, data, col_widths=None):
        """Add a formatted table"""
        table = Table(data, colWidths=col_widths)
        style = [
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1976d2')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1),
             [colors.white, colors.HexColor('#f5f5f5')])
        ]
        table.setStyle(TableStyle(style))
        self.story.append(table)
        self.story.append(Spacer(1, 15))

    def add_page_break(self):
        """Add a page break"""
        self.story.append(PageBreak())

    def generate(self):
        """Generate the final PDF"""
        self.doc.build(self.story)
        print(f"PDF generated successfully: {self.output_path}")


if __name__ == "__main__":
    # Quick test
    pdf = TCSNQTPDFGenerator(
        output_path="test_output.pdf",
        title="TCS NQT Test PDF",
        subject="Test Generation"
    )
    pdf.add_cover_page()
    pdf.add_topic_header("Sample Topic", "This is a test")
    pdf.add_question(
        q_number=1,
        question_text="What is 2 + 2?",
        options={'A': '3', 'B': '4', 'C': '5', 'D': '6'},
        answer="B) 4",
        explanation="Basic arithmetic: 2 + 2 = 4",
        difficulty="Easy"
    )
    pdf.generate()
