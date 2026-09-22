# =============================================================================
# DAY 16: BASIC EMAIL AUTOMATION IN PYTHON
# Author: Harish
# Repository: DAY-16-OF-PYTHON
# Motto: "Not here to be known, here to build."
# =============================================================================

import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# =============================================================================
# 1. WHAT IS EMAIL AUTOMATION? (OVERVIEW & SMTP)
# =============================================================================
# Email automation allows Python scripts to send transactional messages,
# notifications, alerts, newsletters, or reports without manual intervention.
#
# Python provides built-in libraries for this:
# - smtplib: Handles communication with mail servers via SMTP (Simple Mail Transfer Protocol).
# - email.mime: Formats and structures email messages (headers, plain text, HTML, attachments).
#
# Common SMTP Ports & Protocols:
# - Port 465 : SSL (Secure Sockets Layer) - Encrypted from connection start.
# - Port 587 : STARTTLS (Transport Layer Security) - Starts unencrypted, upgrades to TLS.
#
# Common SMTP Server Hosts:
# - Gmail       : smtp.gmail.com
# - Outlook/MS  : smtp.office365.com
# - Yahoo       : smtp.mail.yahoo.com

print("=" * 60)
print("DAY 16: BASIC EMAIL AUTOMATION IN PYTHON")
print("=" * 60)


# =============================================================================
# 2. CONFIGURATION & CREDENTIAL MANAGEMENT
# =============================================================================
# SECURITY BEST PRACTICE:
# Never hardcode email addresses or passwords directly into public code!
# For Gmail, you must use an "App Password" (requires 2-Step Verification enabled).
# Use environment variables or interactive prompts.

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT_SSL = 465
SMTP_PORT_TLS = 587

# Reading credentials from environment variables (safe fallback to demo placeholders)
SENDER_EMAIL = os.environ.get("SENDER_EMAIL", "sender.developer@example.com")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD", "your-app-password-here")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL", "receiver.developer@example.com")


# =============================================================================
# 3. EXAMPLE 1: SENDING A SIMPLE PLAIN-TEXT EMAIL (MIMEText)
# =============================================================================
print("\n--- 1. BUILDING A PLAIN TEXT EMAIL ---")

def create_plain_text_email(sender, receiver, subject, message_body):
    """
    Creates a standard plain text email message using MIMEText.
    """
    msg = MIMEText(message_body, "plain")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    return msg

# Create sample plain text email
sample_text_body = """Hello Harish,

Welcome to Day 16 of Python!
This is an automated plain text email sent using Python's smtplib and MIMEText.

Motto: Not here to be known, here to build.
Happy coding!"""

text_email = create_plain_text_email(
    sender=SENDER_EMAIL,
    receiver=RECEIVER_EMAIL,
    subject="Python Day 16: Plain Text Email Test",
    message_body=sample_text_body
)

print("Created MIME Message:")
print("Subject:", text_email["Subject"])
print("From   :", text_email["From"])
print("To     :", text_email["To"])
print("Content:\n", text_email.get_payload())


# =============================================================================
# 4. EXAMPLE 2: SENDING RICH HTML FORMATTED EMAIL
# =============================================================================
print("\n--- 2. BUILDING AN HTML FORMATTED EMAIL ---")

def create_html_email(sender, receiver, subject):
    """
    Creates an HTML formatted email with styling and links.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                color: #333333;
                margin: 0;
                padding: 20px;
            }}
            .card {{
                max-width: 600px;
                margin: auto;
                background: #ffffff;
                border-radius: 8px;
                padding: 30px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .badge {{
                display: inline-block;
                padding: 4px 10px;
                background: #007bff;
                color: #ffffff;
                border-radius: 12px;
                font-size: 12px;
                font-weight: bold;
            }}
            h2 {{ color: #2c3e50; }}
            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #777777;
                border-top: 1px solid #eeeeee;
                padding-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <span class="badge">DAY 16 OF PYTHON</span>
            <h2>🚀 Basic Email Automation in Python</h2>
            <p>Hello <b>{receiver}</b>,</p>
            <p>This is a rich HTML automated email sent using Python standard library.</p>
            <ul>
                <li>✅ Secure SSL/TLS encryption</li>
                <li>✅ MIME Multipart formatting</li>
                <li>✅ Custom HTML & CSS styling</li>
            </ul>
            <div class="footer">
                <p><i>"Not here to be known, here to build."</i> — Harish</p>
            </div>
        </div>
    </body>
    </html>
    """

    # Multi-part container with alternative subtypes
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    # Plain-text fallback for email clients that do not support HTML
    plain_fallback = MIMEText("This email requires an HTML compatible viewer.", "plain", "utf-8")
    html_part = MIMEText(html_content, "html", "utf-8")

    msg.attach(plain_fallback)
    msg.attach(html_part)
    return msg

html_email = create_html_email(
    sender=SENDER_EMAIL,
    receiver=RECEIVER_EMAIL,
    subject="Python Day 16: Rich HTML Email"
)
print("Created HTML Email with Subject:", html_email["Subject"])
print("Payload parts attached:", len(html_email.get_payload()))


# =============================================================================
# 5. EXAMPLE 3: EMAIL WITH FILE ATTACHMENTS (MIMEBase)
# =============================================================================
print("\n--- 3. BUILDING AN EMAIL WITH ATTACHMENT ---")

def create_email_with_attachment(sender, receiver, subject, body_text, attachment_path):
    """
    Creates an email with an attached file (e.g. .txt, .pdf, .csv, .png).
    """
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    # Attach message body
    msg.attach(MIMEText(body_text, "plain", "utf-8"))

    # If the file exists, read and attach it
    if os.path.exists(attachment_path):
        with open(attachment_path, "rb") as file_handle:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(file_handle.read())

        # Encode the payload in Base64
        encoders.encode_base64(part)

        filename = os.path.basename(attachment_path)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}"
        )
        msg.attach(part)
        print(f"-> Attached file '{filename}' successfully.")
    else:
        print(f"-> Attachment '{attachment_path}' not found on disk (skipping file attach).")

    return msg

# Create a sample temporary report file to demonstrate attachment
demo_report_file = "day16_sample_report.txt"
with open(demo_report_file, "w", encoding="utf-8") as f:
    f.write("Day 16: Email Automation Status Report\nStatus: Active\nCompleted: True\n")

email_with_file = create_email_with_attachment(
    sender=SENDER_EMAIL,
    receiver=RECEIVER_EMAIL,
    subject="Python Day 16: Email with Attachment",
    body_text="Please find the attached status report.",
    attachment_path=demo_report_file
)

# Clean up sample temporary file
if os.path.exists(demo_report_file):
    os.remove(demo_report_file)


# =============================================================================
# 6. EXAMPLE 4: SENDING BULK / MULTIPLE EMAILS
# =============================================================================
print("\n--- 4. BULK EMAIL AUTOMATION TEMPLATE ---")

recipients_list = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"}
]

def generate_personalized_emails(sender, recipients):
    """
    Iterates through a list of recipients to generate personalized messages.
    """
    prepared_emails = []
    for recipient in recipients:
        name = recipient["name"]
        to_email = recipient["email"]
        custom_message = f"Hello {name},\n\nHere is your daily update for Day 16 of Python.\nKeep building!"
        
        email_msg = MIMEText(custom_message, "plain", "utf-8")
        email_msg["Subject"] = f"Daily Python Update for {name}"
        email_msg["From"] = sender
        email_msg["To"] = to_email
        prepared_emails.append(email_msg)
        print(f"-> Prepared message for: {name} <{to_email}>")
    
    return prepared_emails

bulk_messages = generate_personalized_emails(SENDER_EMAIL, recipients_list)


# =============================================================================
# 7. EXAMPLE 5: TRANSMISSION WITH ERROR HANDLING (SSL & STARTTLS)
# =============================================================================
print("\n--- 5. TRANSMISSION FUNCTION & EXCEPTION HANDLING ---")

def send_email_ssl(server_host, server_port, sender, password, receiver, message):
    """
    Demonstrates sending an email securely over SSL (Port 465).
    Includes comprehensive exception handling for network, authentication, and SMTP errors.
    """
    context = ssl.create_default_context()
    
    # Check if credentials are placeholder or demo
    if password == "your-app-password-here" or "example.com" in sender:
        print("[DRY RUN / SIMULATION MODE]")
        print("Real credentials not supplied. Skipping live socket connection.")
        print(f"Simulated sending message from '{sender}' to '{receiver}' via {server_host}:{server_port}.")
        print("Status: SUCCESS (Mock transmission verified!)")
        return True

    try:
        print(f"Connecting to SMTP Server: {server_host}:{server_port} via SSL...")
        with smtplib.SMTP_SSL(server_host, server_port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
        print("Email sent successfully!")
        return True
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Authentication failed! Check your email and App Password.")
    except smtplib.SMTPRecipientsRefused:
        print("ERROR: All recipient addresses were refused.")
    except smtplib.SMTPServerDisconnected:
        print("ERROR: Server unexpectedly disconnected.")
    except smtplib.SMTPException as e:
        print(f"SMTP Error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return False

# Execute demonstration send using dry-run simulation
send_email_ssl(
    server_host=SMTP_SERVER,
    server_port=SMTP_PORT_SSL,
    sender=SENDER_EMAIL,
    password=SENDER_PASSWORD,
    receiver=RECEIVER_EMAIL,
    message=text_email
)


# =============================================================================
# 8. SUMMARY & BEST PRACTICES
# =============================================================================
print("\n" + "=" * 60)
print("SUMMARY & BEST PRACTICES FOR EMAIL AUTOMATION")
print("=" * 60)
# 1. Use smtplib for SMTP transport and email.mime for message structuring.
# 2. Prefer SSL (port 465) or STARTTLS (port 587) with ssl.create_default_context().
# 3. Always use App Passwords instead of actual account passwords (e.g. Gmail App Password).
# 4. Store sensitive secrets in Environment Variables or .env files, never in version control.
# 5. Handle smtplib.SMTPException to ensure graceful failure.
# 6. Apply rate limiting and pacing when sending bulk emails to avoid spam blacklisting.
