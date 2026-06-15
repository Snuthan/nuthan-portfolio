"""Generate professional resume PDF."""
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "resume.pdf"
IMG = ROOT / "assets" / "profile.png"


def build():
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
    )
    styles = getSampleStyleSheet()
    title = ParagraphStyle(
        "Title", parent=styles["Heading1"], fontSize=20, spaceAfter=4, textColor=colors.HexColor("#111111")
    )
    subtitle = ParagraphStyle(
        "Sub", parent=styles["Normal"], fontSize=9.5, textColor=colors.HexColor("#444444"), spaceAfter=4
    )
    section = ParagraphStyle(
        "Sec",
        parent=styles["Heading2"],
        fontSize=9,
        textColor=colors.HexColor("#0096c7"),
        spaceBefore=12,
        spaceAfter=5,
        fontName="Helvetica-Bold",
    )
    body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=9.5, leading=13, textColor=colors.HexColor("#333333"))
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=12, spaceAfter=2)

    story = []

    if IMG.exists():
        photo = Image(str(IMG), width=0.8 * inch, height=0.8 * inch)
        header = Table(
            [[photo, [
                Paragraph("<b>Sadhbuddhi Nuthan</b>", title),
                Paragraph("AI Engineer | Machine Learning Engineer | Agentic AI Developer", subtitle),
                Paragraph(
                    "sadhbuddhinuthan.29@email.com &nbsp;|&nbsp; linkedin.com/in/nuthan-s29 &nbsp;|&nbsp; github.com/Snuthan",
                    subtitle,
                ),
            ]]],
            colWidths=[0.95 * inch, 5.25 * inch],
        )
        header.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (1, 0), (1, 0), 10)]))
        story.append(header)
    else:
        story.append(Paragraph("<b>Sadhbuddhi Nuthan</b>", title))

    story.append(Spacer(1, 0.12 * inch))
    story.append(Paragraph("PROFESSIONAL SUMMARY", section))
    story.append(
        Paragraph(
            "B.Tech graduate in Artificial Intelligence &amp; Machine Learning with internship experience at "
            "<b>Regality AI</b>. Specialized in building production-ready RAG systems, agentic AI workflows, and "
            "LLM-powered applications using Python, LangChain, and FastAPI.",
            body,
        )
    )

    story.append(Paragraph("EXPERIENCE", section))
    story.append(Paragraph("<b>AI Development Intern</b> — Regality AI", body))
    for item in [
        "Developed RAG-based applications for document intelligence and retrieval",
        "Built automation workflows using LLMs and agentic AI frameworks",
        "Implemented intelligent document processing pipelines",
        "Contributed to Regal Forms Assistant — RBI compliance AI with PDF generation",
    ]:
        story.append(Paragraph("• " + item, bullet))

    story.append(Paragraph("FEATURED PROJECTS", section))
    projects = [
        ("Regal Forms Assistant", "RBI compliance AI — LangChain, RAG, FastAPI, LLMs (github.com/Snuthan/regal-forms)"),
        ("Context-Aware RAG System", "Hybrid search &amp; semantic retrieval — LangChain, Vector DB (github.com/Snuthan/pdf-chat-ai)"),
        ("AI Code Reviewer", "LLM-powered code analysis, issue detection, and optimization"),
    ]
    for name, desc in projects:
        story.append(Paragraph(f"<b>{name}</b> — {desc}", body))
        story.append(Spacer(1, 3))

    story.append(Paragraph("EDUCATION", section))
    story.append(Paragraph("<b>B.Tech — Artificial Intelligence &amp; Machine Learning</b>", body))
    story.append(Paragraph("Deep Learning, NLP, Computer Vision, Generative AI", subtitle))

    story.append(Paragraph("TECHNICAL SKILLS", section))
    story.append(
        Paragraph(
            "Python, Machine Learning, Deep Learning, CNN, LSTM, NLP, TensorFlow, PyTorch, Generative AI, "
            "LangChain, RAG, Agentic AI, Prompt Engineering, Vector Databases, OpenAI APIs, LLM Evaluation, "
            "FastAPI, REST APIs, SQL, Git, GitHub",
            body,
        )
    )

    story.append(Paragraph("CERTIFICATIONS", section))
    story.append(Paragraph("<b>NCC A Certificate</b> — National Cadet Corps (Leadership &amp; Discipline)", body))

    doc.build(story)
    print(f"Created {OUT}")


if __name__ == "__main__":
    build()
