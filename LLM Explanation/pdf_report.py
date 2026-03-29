from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import matplotlib.pyplot as plt
import re

def format_llm_text(text):
    if not text:
        return ""

    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"## (.*?)\n", r"<b>\1</b><br/><br/>", text)
    text = text.replace("* ", "• ")
    text = text.replace("\n", "<br/>")
    return text


def generate_pdf(metrics_df, llm_main, llm_decision, llm_run):

    plt.figure()
    metrics_df.plot(x="Algorithm", y="Success Rate", kind="bar", legend=False)
    plt.title("Success Rate Comparison")
    plt.savefig("success_rate.png")
    plt.close()

    plt.figure()
    metrics_df.plot(x="Algorithm", y="Avg Path Length", kind="bar", legend=False)
    plt.title("Average Path Length")
    plt.savefig("path_length.png")
    plt.close()

    plt.figure()
    metrics_df.plot(x="Algorithm", y="Avg Explored Nodes", kind="bar", legend=False)
    plt.title("Explored Nodes")
    plt.savefig("explored_nodes.png")
    plt.close()

    doc = SimpleDocTemplate("Hybrid_AI_Report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("<b>Hybrid Classical–Quantum Path Planning Report</b>", styles["Title"]))
    content.append(Spacer(1, 20))

    content.append(Paragraph(metrics_df.to_string().replace("\n", "<br/>"), styles["Normal"]))

    content.append(Image("success_rate.png", width=400, height=250))
    content.append(Image("path_length.png", width=400, height=250))
    content.append(Image("explored_nodes.png", width=400, height=250))

    content.append(Paragraph(format_llm_text(llm_main), styles["Normal"]))
    content.append(Paragraph(format_llm_text(llm_decision), styles["Normal"]))
    content.append(Paragraph(format_llm_text(llm_run), styles["Normal"]))

    doc.build(content)