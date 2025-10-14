#!/usr/bin/env python3
import os
import argparse
import smtplib
import logging
from email.message import EmailMessage

# Configure logging
logging.basicConfig(filename='handler.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

def parse_args():
    parser = argparse.ArgumentParser(
        description='Send form data via SMTP.'
    )
    parser.add_argument('--to', required=True, help='Recipient email')
    parser.add_argument('--subject', default='Contact Form Submission', help='Email subject')
    parser.add_argument('--body', required=True, help='Email body text')
    return parser.parse_args()

def send_email(recipient, subject, body):
    smtp_host = os.getenv('SMTP_HOST')
    smtp_port = int(os.getenv('SMTP_PORT', 587))
    smtp_user = os.getenv('SMTP_USER')
    smtp_pass = os.getenv('SMTP_PASS')

    if not all([smtp_host, smtp_user, smtp_pass]):
        logging.error('Missing SMTP configuration in environment variables.')
        raise RuntimeError('SMTP credentials not fully set.')

    msg = EmailMessage()
    msg['From'] = smtp_user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        logging.info(f'Email sent to {recipient}')

if __name__ == '__main__':
    args = parse_args()
    try:
        send_email(args.to, args.subject, args.body)
        print(f'Success: Email sent to {args.to}')
    except Exception as e:
        print(f'Error: {e}')
        logging.exception(e)
        exit(1)