# Day 16: Basic Email Automation in Python ✉️🚀

> **Motto**: *"Not here to be known, here to build."*

Welcome to **Day 16 of Python**! Today we explore **Email Automation** using Python's built-in standard libraries (`smtplib` and `email.mime`). Learn how to automate sending transactional emails, alerts, rich HTML newsletters, and file attachments without third-party dependencies.

---

## 📌 Table of Contents
1. [What is Email Automation & SMTP?](#1-what-is-email-automation--smtp)
2. [Architecture & Email Flow](#2-architecture--email-flow)
3. [Setting Up Secure Credentials (App Passwords)](#3-setting-up-secure-credentials-app-passwords)
4. [Key Python Modules](#4-key-python-modules)
5. [Code Examples & Walkthrough](#5-code-examples--walkthrough)
   - [Example 1: Sending Plain Text Email](#example-1-sending-plain-text-email)
   - [Example 2: Sending Rich HTML Formatted Email](#example-2-sending-rich-html-formatted-email)
   - [Example 3: Email with File Attachments](#example-3-email-with-file-attachments)
   - [Example 4: Sending Bulk Personalized Emails](#example-4-sending-bulk-personalized-emails)
   - [Example 5: Error Handling & Secure Transmission](#example-5-error-handling--secure-transmission)
6. [Best Practices & Security Rules](#6-best-practices--security-rules)
7. [How to Run](#7-how-to-run)
8. [Summary & Key Takeaways](#8-summary--key-takeaways)

---

## 1. What is Email Automation & SMTP?

**Email Automation** is the programmatic creation, configuration, and dispatch of email messages from an application.

### Understanding SMTP
- **SMTP** stands for **Simple Mail Transfer Protocol**. It is the industry standard protocol for transmitting email messages over IP networks.
- Python communicates with an SMTP server (such as Gmail, Outlook, or Yahoo) which acts as the mail transfer agent delivering messages to the recipient's mail server.

### Standard Ports & Encryption:
| Protocol / Method | Standard Port | Description |
| :--- | :--- | :--- |
| **SSL (`SMTP_SSL`)** | **465** | Connection is encrypted immediately upon establishing the socket. |
| **STARTTLS (`starttls()`)** | **587** | Starts as plain text connection, then upgrades securely to TLS. |

---

## 2. Architecture & Email Flow

```
+-------------------------------------------------------+
|                    Python Script                      |
|  - MIMEText / MIMEMultipart (Compose subject, body)   |
|  - MIMEBase & encoders (Attach files)                 |
+-------------------------------------------------------+
                           |
               (SMTP_SSL or STARTTLS)
                           v
+-------------------------------------------------------+
|                     SMTP Server                       |
|   (e.g., smtp.gmail.com / smtp.office365.com)         |
+-------------------------------------------------------+
                           |
                           v
+-------------------------------------------------------+
|                  Recipient Mailbox                    |
|             (Inbox / Spam Filter / Delivery)          |
+-------------------------------------------------------+
```

---

## 3. Setting Up Secure Credentials (App Passwords)

> ⚠️ **IMPORTANT**: Modern email providers (like Google Gmail) do not permit using your standard account password with basic authentication. You must generate an **App Password**.

### Steps for Gmail:
1. Go to your **Google Account** settings: [https://myaccount.google.com/](https://myaccount.google.com/)
2. Navigate to **Security** and enable **2-Step Verification**.
3. Search for **App passwords** in the search bar.
4. Name the app (e.g., `Python Email Automation`) and click **Create**.
5. Copy the 16-character generated password.
6. Store it securely in your environment variables:
   ```bash
   export SENDER_EMAIL="your_email@gmail.com"
   export SENDER_PASSWORD="your_16_char_app_password"
   export RECEIVER_EMAIL="target_recipient@example.com"
   ```

---

## 4. Key Python Modules

Python includes everything you need in its **standard library** — no `pip install` required!

- `smtplib`: Defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP listener daemon.
- `ssl`: Creates secure default SSL contexts (`ssl.create_default_context()`).
- `email.mime.text.MIMEText`: Formats plain text and HTML message bodies.
- `email.mime.multipart.MIMEMultipart`: Container for complex messages (alternative plain/HTML formats, attachments).
- `email.mime.base.MIMEBase`: Handles file streams for attachments.
- `email.encoders`: Encodes binary attachment payloads into Base64 format.

---

## 5. Code Examples & Walkthrough

### Example 1: Sending Plain Text Email
```python
from email.mime.text import MIMEText

msg = MIMEText("Hello Harish! Welcome to Day 16 of Python.", "plain")
msg["Subject"] = "Day 16: Python Email Automation"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"
```

### Example 2: Sending Rich HTML Formatted Email
Use `MIMEMultipart("alternative")` to provide both an HTML view and a plain-text fallback:
```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart("alternative")
msg["Subject"] = "Rich HTML Email"
msg["From"] = sender
msg["To"] = receiver

html_content = "<h2>Day 16 of Python</h2><p>Styled with <b>HTML</b>!</p>"
msg.attach(MIMEText(html_content, "html", "utf-8"))
```

### Example 3: Email with File Attachments
```python
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
with open("report.pdf", "rb") as file_handle:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(file_handle.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition", 'attachment; filename="report.pdf"')
msg.attach(part)
```

### Example 4: Sending Bulk Personalized Emails
```python
recipients = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]

for person in recipients:
    custom_body = f"Hello {person['name']},\nWelcome to Day 16!"
    # Send individually to avoid exposing all recipient addresses
```

### Example 5: Error Handling & Secure Transmission
```python
import smtplib
import ssl

context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Check your App Password.")
except smtplib.SMTPException as e:
    print(f"SMTP error occurred: {e}")
```

---

## 6. Best Practices & Security Rules

1. 🔒 **Never Commit Credentials**: Never hardcode email passwords or sensitive API keys in your repository.
2. 🔑 **Use App-Specific Passwords**: Always generate and use app passwords with 2FA enabled.
3. 🛡️ **Always Use TLS/SSL**: Always encrypt your transmission using `ssl.create_default_context()`.
4. ⏱️ **Rate Limiting**: When sending bulk emails, add delays (`time.sleep`) to prevent being throttled or flagged as spam.
5. ⚠️ **Validate Email Addresses**: Sanitize recipient inputs before sending.
6. 🧩 **Exception Handling**: Catch `smtplib.SMTPException`, `socket.error`, and authentication errors gracefully.

---

## 7. How to Run

### 1. Run in Safe Simulation Mode (Default)
Run without setting environment variables to inspect the message building and mock transmission:
```bash
python day16.py
```

### 2. Run with Live Credentials (Optional)
To send a real email, supply your credentials via environment variables:
```bash
# On Windows (PowerShell):
$env:SENDER_EMAIL="your_email@gmail.com"
$env:SENDER_PASSWORD="your-app-password"
$env:RECEIVER_EMAIL="target_recipient@example.com"
python day16.py

# On Linux / macOS:
export SENDER_EMAIL="your_email@gmail.com"
export SENDER_PASSWORD="your-app-password"
export RECEIVER_EMAIL="target_recipient@example.com"
python day16.py
```

---

## 8. Summary & Key Takeaways

- Python's standard library provides full email creation and transmission capabilities via `smtplib` and `email.mime`.
- Port **465** is standard for `SMTP_SSL` and Port **587** is standard for `STARTTLS`.
- `MIMEMultipart` enables combining plain text, HTML, and file attachments in a single message.
- Always follow email security protocols: environment variables, TLS encryption, and provider App Passwords.

---
⭐ *Day 16 of the Python series completed!*
