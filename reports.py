#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from datetime import date
import glob

def generate_report(filename, title, additional_info):
    """Define a function that generates PDF report"""
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(additional_info, styles["BodyText"])

    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info])

if __name__ == "__main__":
    """Generate a PDF report of the weight of each kind of fruits"""
    today = date.today()
    title = "Processed Update on " + today.strftime("%b %d, %Y")

    #Loop through the list of description files of fruits
    summary = ""
    for file_name in glob.iglob(r"../supplier-data/descriptions/*.txt"):
        with open(file_name) as file:
            #Read through lines of the description file
            reader = file.readlines()
            """Process the text data in the following format,
            Name: Apple
            Weight: 500 lbs
            """
            summary = summary + "name: " + reader[0] + "<br/>" + "weight: " + reader[1] + "<br/>" + "<br/>"

generate_report("/tmp/processed.pdf", title, summary)
