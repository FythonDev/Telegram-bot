# force-join-bot

A Telegram bot that checks if a user is a member of a specific channel before allowing access.  
Smart gatekeeping with inline buttons and custom messages.

## 🚀 Setup
1. Fill `config.json` with your API credentials and bot token.
2. Install dependencies: `pip install pyrogram tgcrypto`
3. Run `main.py` with Python 3.8+

## ⚙️ Features
- Membership check via `get_chat_member`
- Custom welcome message for verified users
- Inline button for quick channel join
- Lightweight and easy to deploy
