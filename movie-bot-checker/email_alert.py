import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "ravi.praj55@gmail.com"
# receiver_email = "dominator2rule@gmail.com"
# password = input("Type your password and press enter:")
password = 'techprixa1234'

message = MIMEMultipart("alternative")
message["Subject"] = "Movie is now showing"
message["From"] = sender_email


# Create the plain-text and HTML version of your message
text = """\
Quick, Doctor Strange in the Multiverse of Madness is now showing.
Book it fast when you can
Find more about it at:
https://www.qfxcinemas.com/home"""
html = """\
<html>
  <body>
    <h1>Movie AYO!!!!..., Doctor Strange in the Multiverse of Madness is now showing.</h1><br>
    <p>
       Book it fast when you can<br>
        Find more about it at:<br>
       <a href="https://www.qfxcinemas.com/home">QFX Cenema</a> 
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

def send_email(receiver_email):
    # Create secure connection with server and send email
    message["To"] = receiver_email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
