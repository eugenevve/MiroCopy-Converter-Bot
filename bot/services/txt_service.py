import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm


def txt_to_pdf(input_path: str, output_path: str):
    font_name = "Roboto"
    font_file = "Roboto-Regular.ttf"
    font_path = os.path.join("assets", font_file)

    if not os.path.exists(font_path):
        font_path = font_file

    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font not found: {font_file}")

    pdfmetrics.registerFont(TTFont(font_name, font_path))

    c = canvas.Canvas(output_path, pagesize=A4)
    doc_title = os.path.basename(output_path)
    c.setTitle(doc_title)
    width, height = A4

    # text settings
    font_size = 11
    line_height = 14
    margin = 20 * mm
    current_y = height - margin
    max_text_width = width - (2 * margin)

    current_y = height - margin
    c.setFont(font_name, font_size)

    try:
        with open(input_path, 'r', encoding='utf-8-sig') as f:
            for line in f:
                text = line.rstrip()

                if not text:
                    current_y -= line_height
                    continue

                # improved line breaks (90 characters for Roboto 11pt)
                max_chars = 90
                chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
                chunks = simpleSplit(text, font_name, font_size, max_text_width)

                for chunk in chunks:
                    # if the text has reached the bottom of the page
                    if current_y < margin:
                        c.showPage()
                        c.setFont(font_name, font_size)
                        current_y = height - margin

                    c.drawString(margin, current_y, chunk)
                    current_y -= line_height

        c.save()
    except Exception as e:
        raise e
