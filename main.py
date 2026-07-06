
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"👋 স্বাগতম, {user.first_name}! BD Free Income Hub-এ আপনার স্বাগত।\n\n"
        "⭐ টেলিগ্রাম স্টারস প্রাইস\n"
        "👤 অ্যাডমিন: @RISHAD_Vai12"
    )

async def stars(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⭐ টেলিগ্রাম স্টারস প্রাইস:\n"
        "1 স্টার = ১ টাকা ২০ পয়সা\n"
        "50 স্টার = 60 টাকা\n"
        "100 স্টার = 120 টাকা\n"
        "500 স্টার = 600 টাকা\n"
        "1000 স্টার = ১,২০০ টাকা"
    )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👤 যোগাযোগ করুন: @RISHAD_Vai12"
    )

app = Application.builder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stars", stars))
app.add_handler(CommandHandler("admin", admin))

app.run_polling()
