from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update: Update, context):
    await update.message.reply_text("Hello! I’m a bot deployed on Vercel.")

async def hello(update: Update, context):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def webhook(update: Update, context):
    await context.bot.process_update(update)

if __name__ == '__main__':
    app = ApplicationBuilder().token('YOUR_BOT_TOKEN').build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hello", hello))

    # Set webhook URL as Vercel's endpoint
    app.run_webhook(listen="0.0.0.0",
                    port=8000,
                    webhook_url='https://your-vercel-url/api/webhook')
