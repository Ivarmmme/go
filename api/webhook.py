import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text("Hello! This is your Telegram bot.")

async def hello(update: Update, context):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def handler(request):
    token = os.getenv('TELEGRAM_TOKEN')
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))

    if request.method == 'POST':
        update_data = await request.json()
        update = Update.de_json(update_data, app.bot)
        await app.process_update(update)

    return {
        "statusCode": 200,
        "body": "Webhook received"
    }
