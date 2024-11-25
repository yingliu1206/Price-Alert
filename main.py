import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import dotenv_values

TARGET = 100
config = dotenv_values(".env")
smtp_address = config['SMTP_ADDRESS']
my_email = config['EMAIL_ADDRESS']
address = config['EMAIL_ADDRESS']
password = config['EMAIL_PASSWORD']
url = 'https://www.amazon.com/Hourglass-Ambient-Soft-Foundation-Shade/dp/B0BM56X779/ref=sr_1_5?dib=eyJ2IjoiMSJ9.6DkOjJLSEbxFUqiRhIjRTugG8vCsyGUNQvSeVrxtgjLKlzlRwE7Ihtgthw7-iqc4i9vrRjgtr8iRn_iqKngym9J01C4ttMnMrzJNB0Pw0c5ZsL2a3NSaySHmVejuJ6uGT5M9hI00meVCjQcgkHVH5AEiTL2898pqIDVGXpSYYqx_XCkKuHUrf5B5p-d7VpEEsL89pxdhck4kOS2SxvljOC5wxdurkLTbJA_RrIiXDVRq8uqfLkX3rt1ntrLpOCR0Q59MZi9qqIoyThcN2CDquEfDpeuQQXW3ExSdOWTVhqM.3veltpd5UAVChYhj-ZHi3BW8UqMPVauuCyVP5Kj7f0U&dib_tag=se&keywords=hourglass+foundation&qid=1732569744&sr=8-5'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

#scrape the website
response = requests.get(url, headers=headers)
website_html = response.text


soup = BeautifulSoup(website_html, 'html.parser')
# print(soup.prettify())

price = float(soup.find(class_ = "a-offscreen").text.replace('$', ''))

if price < TARGET:
    # Create a multipart message to include both text and image
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = address
    msg['Subject'] = 'Amazon Price Alert!'

    # Attach the image (Ensure you have a valid path to the image)
    with open('foundation.jpg', 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', '<image1>')  # Assign an ID to the image for inline display
        msg.attach(img)

    # Add the body text to the email with utf-8 encoding
    body = f'''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f0f8ff; /* Light blue background */
                        color: #333; /* Dark text color */
                        text-align: center; /* Center-align text */
                        padding: 20px;
                    }}
                    .template {{
                        font-size: 1em; /* Slightly larger font for the template */
                        margin: 20px 0; /* Margin for spacing */
                    }}
                    .footer {{
                        margin-top: 40px;
                        font-size: 1em; /* Smaller font for the footer */
                        color: #555; /* Gray color for the footer */
                    }}
                    img {{
                        max-width: 60%; /* Flexible width */
                        height: auto; /* Maintain aspect ratio */
                        border-radius: 10px; /* Rounded corners for the image */
                    }}
                </style>
            </head>
            <body>
                <div class="template">The price dropped to ${price}!</div>
                <img src="cid:image1" alt="Product Image">
                <p class="footer">Let's do shopping!</p>
            </body>
            </html>
            '''
    msg.attach(MIMEText(body, 'html', 'utf-8'))  # Change to 'html' to include the image

    # Create a connection and send the email
    with smtplib.SMTP(smtp_address, 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=address, msg=msg.as_string())
        connection.close()
