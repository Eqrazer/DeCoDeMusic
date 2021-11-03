from plugins import check_heroku
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram import Client, filters
from helpers.decorators import sudo_users_only
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery


@Client.on_message(command(["shadow_summmon", "arise"]) & ~filters.edited)
@sudo_users_only
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_photo(
                                     photo="https://telegra.ph/file/d1fda03ea9d798f46888a.jpg", 
                                     caption="**Restaring**\n**Please Wait...**"
   )
    hap.restart()
