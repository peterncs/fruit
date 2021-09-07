#!/usr/bin/env python3

import emails

if __name__ == "__main__":
    """Send the PDF report as an email attachment"""
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send(message)
