import random
import time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot Telegram
updater = Updater(token='6351605119:AAF8qYVXGiETnetsLwJjqGKTm7qm56EauSo', use_context=True)
dispatcher = updater.dispatcher

def generate_sequence():
    sequence = ["🟩", "🟩", "🟩", "🟩", "🍎"]
    random.shuffle(sequence)
    return ' '.join(sequence)

def send_sequence_to_channel(update, context):
    sequence_template = """
🔔 CONFIRMED ENTRY!
🍎 Apple : 3
🔐 Attempts: 3
⏰ Validity: 5 minutes
"""

    sequence_message = f"""
{sequence_template}
2.41: {generate_sequence()}
1.93: {generate_sequence()}
1.54: {generate_sequence()}
1.23: {generate_sequence()}

🚨 FONCTIONNE UNIQUEMENT SUR 1XBET ET LINEBET AVEC LE CODE PROMO Free221 ✅️ !

[S'inscrire](https://bit.ly/3NJ4vy0)
[Comment jouer](https://t.me/SOLKAH00/1102)
"""

    inline_keyboard = [
        [
            InlineKeyboardButton("S'inscrire", url='https://bit.ly/3NJ4vy0'),
            InlineKeyboardButton("Comment jouer", url='https://t.me/SOLKAH00/1102')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    update.message.reply_text(text=sequence_message, parse_mode='Markdown', disable_web_page_preview=True, reply_markup=reply_markup)

def start(update, context):
    inline_keyboard = [
        [
            InlineKeyboardButton("Voir la pomme", callback_data='voir_la_pomme'),
            InlineKeyboardButton("Test", callback_data='test_message')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    update.message.reply_text("Cliquez sur 'Voir la pomme' pour générer les séquences :", reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    chat_id = query.message.chat_id

    if query.data == 'voir_la_pomme':
        send_sequence_to_channel(update, context)
    elif query.data == 'test_message':
        send_sequence_to_channel(update, context)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)

updater.start_polling()
updater.idle()
