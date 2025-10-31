# Fast-Homework

Got bored of doing homework that doesn't has a purpose other than being reviewed without any interest + not being relevant, I did automatized this task by using a **Telegram bot** that use **Google Gemini AI** and a **docx Template**. 

---

## Tech Stack
- **Python 3.x**
- **python-telegram-bot** - Telegram bot framework
- **Google Genai** - Google Gemini AI API

---

## Project Structure

```
FastHomework/
├── bot/                    # Telegram bot logic
│   ├── core.py            # Bot initialization
│   ├── handlers.py        # Message and command handlers
│   └── __init__.py
├── services/              # Business logic
│   ├── llm_client.py      # Google Gemini integration
│   ├── report_generator.py # Report generation
│   └── __init__.py
├── templates/             # Response templates
├── output/                # Generated outputs
├── config.py              # Configuration & environment variables
├── main.py                # Entry point
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.8+
- Telegram account
- Google API key (for Gemini)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AlanValerdi/Fast-Homework.git
   cd Fast-Homework
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   TELEGRAM_TOKEN=your_telegram_bot_token
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Run the bot**
   ```bash
   python main.py // python3 -m main
   ```

---

**Alan Valerdi** - [GitHub](https://github.com/AlanValerdi)

---
