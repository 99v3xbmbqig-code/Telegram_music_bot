import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from urllib.parse import quote

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 هلا بيك!\n\n"
        "اكتب اسم الأغنية أو الفنان، وأنا أبحثلك عنها 🔎🎶"
    )


async def search_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    song = update.message.text.strip()

    if not song:
        return

    query = quote(song)

    youtube = f"https://www.youtube.com/results?search_query={query}"
    spotify = f"https://open.spotify.com/search/{query}"

    await update.message.reply_text(
        f"🎵 البحث عن: {song}\n\n"
        f"▶️ YouTube:\n{youtube}\n\n"
        f"🎧 Spotify:\n{spotify}"
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not configured")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_song))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
