<<<<<<< HEAD
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, title, content_list):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph(title, styles['Title']))
    elements.append(Spacer(1, 12))

    for item in content_list:
        elements.append(Paragraph(item, styles['Normal']))
        elements.append(Spacer(1, 10))

=======
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(filename, title, content_list):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph(title, styles['Title']))
    elements.append(Spacer(1, 12))

    for item in content_list:
        elements.append(Paragraph(item, styles['Normal']))
        elements.append(Spacer(1, 10))

>>>>>>> 937145374ef1cb54abd7cc95f7939691e2e304be
    doc.build(elements)