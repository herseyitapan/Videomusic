# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Xoşgəldin [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Mən səsli söhbətdə video və musiqi oxuda bilərəm!**

💡 **📚 Komandalar buttonu'na klik edib komandalarla tanış ol!**

🔖 **Bu botu necə istifadə edə biləcəyinizi öyrənmək üçün » ❓ Sadə Komandalar!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Məni Qruplarınıza Əlavə Et ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Sadə komandalar", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Komandalar", callback_data="cbcmds"),
                    InlineKeyboardButton("👨🏻‍💻Sahibim", url=f"https://t.me/dakanca_hozu"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Support", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Project", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Bu botu istifadə etmək üçün təməl qaydalar:**
1.) **Əvvəlcə məni qrupa əlavə et.**
2.) **Mənə adminlik yetkiləri ver (Görüntü söhbət yönətmə mütləq açıq olmalıdır).**
3.) **Məni admin etdikdən sonra /reload yazıb admin list yeniləyin.**
3.) **Qrupunuza @{ASSISTANT_NAME} əlavə edin admin hüquqları verin komanda ilədə əlavə edə bilərsiniz /join .**
4.) **Video/musiqi başladmazdan əvvəl səsli söhbət açın.**
5.) **Bəzən /reload komandası botda olan probləmlərə həll yoludur /reload edərək bot adminlərindən öncə sadə təmir edin.**

😍 **Bizi Seçdiyiniz üçün təşəkkürlər **

⚡ __Project Crazy__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**


⚡ __😎 Crazy Project__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin komandaları", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Developer komandaları ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Sadə komandalar", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 geri", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Sadə komandalar:

» /play => istədiyiniz musiqini səslidə açar
» /vplay => istədiyiniz videonu səslidə açar
» /vyukle => video yükləyər
» /song => musiqi yükləyər

⚡️ __Crazy Project__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 admin komandaları:

» /pause - seste botu müvəqqəti dayandırır
» /resume - dayanmış musiqini davam etdirir
» /skip - növbətiyə keç
» /end - hərşeyi bağlayar səsli söhbətidə
» /reload - botu yenidən başladıb Admin list yeniləyər
» /join - asistan qrupa qatılar
» /leave - asistan qrupdan ayrılar

⚡️ __Crazy Project__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮
Ups Sən Bot sahibi deyilsən bu komandalar bot sahibi üçün əlçatandır...

⚡ __Crazy Project__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Geri", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
