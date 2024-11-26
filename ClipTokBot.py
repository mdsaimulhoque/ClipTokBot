# import os
# import yt_dlp
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


# # Function to download TikTok video using yt_dlp
# def download_tiktok_video_with_ytdlp(video_url, save_path='tiktok_videos'):
#     # Ensure the save directory exists
#     if not os.path.exists(save_path):
#         os.makedirs(save_path)

#     # Configure yt-dlp options
#     ydl_opts = {
#         'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
#         'format': 'best',
#     }

#     try:
#         # Create a yt-dlp object and download the video
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(video_url, download=True)
#             filename = ydl.prepare_filename(info)
#             return filename
#     except Exception as e:
#         print(f"Error downloading video: {str(e)}")
#         return None


# # /start command handler
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(
#         "Welcome! Send me a TikTok video URL, and I'll download the video for you."
#     )


# # Message handler to process video URLs
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     message = update.message.text

#     # Check if the message contains a TikTok URL
#     if "tiktok.com" in message:
#         await update.message.reply_text("Downloading the video. Please wait...")

#         # Download the video
#         video_file = download_tiktok_video_with_ytdlp(message)

#         if video_file:
#             # Send the video file back to the user
#             with open(video_file, 'rb') as video:
#                 await update.message.reply_video(video=video, caption="Here's your TikTok video!")
#             os.remove(video_file)  # Clean up after sending the file
#         else:
#             await update.message.reply_text(
#                 "Sorry, I couldn't download the video. Please check the URL and try again."
#             )
#     else:
#         await update.message.reply_text("Please send a valid TikTok video URL.")


# # Main function to set up the bot
# def main():
#     # Replace 'YOUR_BOT_TOKEN' with your BotFather token
#     bot_token = "7602614696:AAFo7Cai_tnpn1F1ZVvSiqOVpmJfnj6hufY"

#     # Initialize the bot
#     app = ApplicationBuilder().token(bot_token).build()

#     # Add command and message handlers
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

#     # Run the bot
#     print("Bot is running. Press Ctrl+C to stop.")
#     app.run_polling()


# if __name__ == "__main__":
#     main()




import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Function to download TikTok video using yt_dlp
def download_tiktok_video(video_url, save_path='tiktok_videos'):
    # Ensure the save directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
        'format': 'best',
    }

    try:
        # Create a yt-dlp object and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        print(f"Error downloading video: {e}")
        return None


# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "👋 Welcome to the TikTok Downloader Bot!\n\n"
        "📌 Send me a TikTok video URL, and I'll download the video for you!"
    )


# Message handler to process video URLs
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    # Check if the message contains a TikTok URL
    if "tiktok.com" in message:
        await update.message.reply_text("⏳ Downloading the video. Please wait...")

        # Download the video
        video_file = download_tiktok_video(message)

        if video_file:
            # Check if the file size is within Telegram's limit
            if os.path.getsize(video_file) > 50 * 1024 * 1024:  # 50 MB
                await update.message.reply_text("❗ The video is too large to send via Telegram.")
                os.remove(video_file)
                return

            # Send the video file back to the user
            with open(video_file, 'rb') as video:
                await update.message.reply_video(video=video, caption="🎥 Here's your TikTok video!")
            os.remove(video_file)  # Clean up after sending the file
        else:
            await update.message.reply_text(
                "⚠️ Sorry, I couldn't download the video. Please check the URL and try again."
            )
    else:
        await update.message.reply_text("❗ Please send a valid TikTok video URL.")


# Main function to set up the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your BotFather token
    bot_token = "7602614696:AAFo7Cai_tnpn1F1ZVvSiqOVpmJfnj6hufY"

    # Initialize the bot
    app = ApplicationBuilder().token(bot_token).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    print("🤖 Bot is running. Press Ctrl+C to stop.")
    app.run_polling()


if __name__ == "__main__":
    main()
