from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from database import get_history


def export_history_pdf(username):

    filename = f"{username}_history.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            f"Security Report - {username}",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    history = get_history(username)

    for record in history:

        line = (
            f"{record[0]} | "
            f"{record[1]} | "
            f"{record[2]} | "
            f"{record[3]}"
        )

        content.append(
            Paragraph(line, styles["Normal"])
        )

    doc.build(content)

    return filename