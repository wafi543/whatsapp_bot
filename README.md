# WhatsApp Bot

A Django-based WhatsApp bot that interacts with users via the WhatsApp Cloud API. It provides interactive menus for various engineering and consultancy services.

## Features

- **Webhook Integration**: Handles incoming messages from the WhatsApp Cloud API.
- **Interactive Menus**: Sends interactive list messages (main menu, other services) loaded dynamically from JSON files.
- **Service Categories**: Includes options for free engineering consultations, design, supervision, and other services.

## Project Structure

- `bot/` - Main Django app for bot logic.
  - `views.py` - Webhook endpoints for receiving messages and verifying the webhook.
  - `services.py` - Helper functions to send messages to users (e.g., `send_menu`).
  - `menus/` - Contains JSON templates for interactive menus (`menu.json`, `other_services.json`).
- `whatsapp_bot/` - Django project settings.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:
   - `PHONE_NUMBER_ID`: Your WhatsApp Phone Number ID.
   - `WHATSAPP_TOKEN`: Your WhatsApp Cloud API access token.
   - `WEBHOOK_VERIFY_TOKEN`: Your custom verify token for webhook setup.

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Expose your local server to the internet (e.g., using ngrok) and configure the webhook URL in your Meta app dashboard.
