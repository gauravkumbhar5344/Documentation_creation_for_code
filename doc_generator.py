#from reportlab.platypus import SimpleDocTemplate, Paragraph

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_txt(content, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def generate_pdf(content, output_path):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(output_path)
    story = []

    for line in content.split("\n"):
        story.append(Paragraph(line.replace("<", "&lt;"), styles["Normal"]))

    doc.build(story)
