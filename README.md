# Price-Alert

A simple and efficient program to track price changes for your desired products. When the price of a product drops to or below your target, you'll receive an instant email alert.

## Features

- **Real-Time Price Tracking**: Monitor product prices from supported platforms dynamically.
- **Email Alerts**: Get notified via email as soon as the price reaches your set target.
- **Customizable Targets:**: Easily set your desired price for each product.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries
    * requests
    * beautifulsoup4
    * smtplib (built-in)

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yingliu1206/Price-Alert.git
   cd Price-Alert
   ```
   
2. **Add the URLs of the products you want to track and set your target prices in the script**:

3. **Configure the email alert system**:
   - Edit the email settings in the script to add your email credentials and the recipient's email address.
     
4. **Run the program**:
   ```bash
   python price_alert.py
   ```
   
## Acknowledgments
- [100 Days of Code: The Complete Python Pro Bootcamp - Udemy](https://www.udemy.com/course/100-days-of-code) for the inspiration and guidance.
