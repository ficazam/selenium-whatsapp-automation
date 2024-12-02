# WhatsApp Web Automation (Selenium)

## Overview
This project is an attempt to automate sending messages via WhatsApp Web using **Selenium**. While functional, it faced limitations due to WhatsApp Web's anti-automation protections, making it impractical for long-term or reliable use.

## Features
- Automates sending messages through WhatsApp Web.
- Uses Selenium to interact with the browser programmatically.
- Demonstrates handling browser elements such as search boxes and message inputs.

## Limitations
- Requires manual login each time (QR code scan).
- Cannot persist sessions effectively due to WhatsApp Web protections against automated cookies and localStorage manipulation.
- May log out or fail due to anti-bot measures.

## Requirements
- Python 3.7 or higher
- **Selenium**: For browser automation
- Google Chrome and ChromeDriver (matching versions)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ficazam/selenium-whatsapp-automation.git
   cd selenium-whatsapp-automation
