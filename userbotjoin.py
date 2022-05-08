import asyncio
from config import BOT_USERNAME, SUDO_USERS
from driver.decorators import authorized_users_only, sudo_users_only, errors
from driver.filters import command, other_filters
from driver.veez import user as USER
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant


@Client.on_message(
    command(["join", f"join@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def join_group(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except BaseException:
        await message.reply_text(
            "• **Bu yetkiyə sahib deyiləm :**\n\n» ❌ __İstifadəçi əlavə etmək__",
        )
        return

    try:
        user = await USER.get_me()
    except BaseException:
        user.first_name = "music assistant"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 Flood Wait xətası 🛑 \n\n**asistan qrupa qatıla bilmədi ya qrupdan ban alıb yaxud mənim yetkim yoxdur**"
            "\n\n**Manual olaraq əlinizlə asistanı qrupa əlavə edin**",
        )
        return
    await message.reply_text(
        f"✅ **Uğurla Söhbətə qatıldım!**",
    )


@Client.on_message(command(["leave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leave_one(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ Eh sizdən küsdüm qrupdan çıxıram :/ !")
        await USER.leave_chat(message.chat.id)
    except BaseException:
        await message.reply_text(
            "❌ **FloodWait xətası asistan qrupdan çıxa bilmədi onu /kick edərək başqa botla çıxarın**\n\n**» yaxud əlinizlə çıxarın**"
        )

        return


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **userbot** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats."
    )
