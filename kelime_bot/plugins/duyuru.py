from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from time import sleep
from kelime_bot.plugins.yakalayıcı import data_message
from kelime_bot import OWNER_ID

@Client.on_message(filters.command(["elan"], [".", "/"]) & filters.user(OWNER_ID))
async def elan(c:Client, m:Message):
    chats = await c.get_messages(OWNER_ID, data_message.message.message_id)
    chats_list = chats.text.split()
        
        
    #----> Mesaj içeriği <----
    mesaj = ""
    if m.reply_to_message is not None:
        mesaj = m.reply_to_message.text
    else:
        mesaj = m.text[8:]
    await c.send_message(m.chat.id,f"**Göndəriləcək Qrup Sayı:  {len(chats_list)}\nMesajınız:**\n\n__{mesaj}__")



    #----> Gönderme İşlemi <----
    bas =await c.send_message(m.chat.id, "**Elan Göndərilməyə Başladı.**")
    for chat in chats_list:
        try:
            await c.send_message(chat, mesaj, disable_web_page_preview=True)
            await bas.edit(f"**Elan Göndərilməyə Başladı.**\n\nGöndərildi: {chat}")
        except:
            pass
        sleep(2)
    await c.send_message(m.chat.id, "**Elan Göndərmə Prosesi Bitti Bütün Qruplara Elanınəz Göndərildi.**")
    
    
    
    

@Client.on_message(filters.command(["felan"], [".", "/"]) & filters.user(OWNER_ID))
async def felan(c:Client, m:Message):
    chats = await c.get_messages(OWNER_ID, data_message.message_id)
    chats_list = chats.text.split()
        

    #----> Mesaj içeriği <----
    if m.reply_to_message is not None:
        message_id = m.reply_to_message.message_id
        mesaj = "t.me/" + str(m.chat.username) + "/" + str(message_id)
    else:
        return m.reply("**Mesajı yönləndirmə şəklində Elan etmək üçün  yanıtlayın !!**")
    await c.send_message(m.chat.id,f"**Göndəriləcək Qrup Sayı:  {len(chats_list)}\nMesajınız: [Tıkla]({mesaj})**", disable_web_page_preview=True)


    #----> Gönderme İşlemi <----
    bas = await c.send_message(m.chat.id, "**Elan Göndərilməyə Başlandı.**")
    for chat in chats_list:
        try:
            await c.forward_messages(chat,m.chat.id, message_id)
            await bas.edit(f"**Elan Göndərilməyə Başlandı.**\n\nGöndərildi: {chat}")
        except:
            pass
        sleep(2)
    await c.send_message(m.chat.id, "**Elan Prosesi Bitti Bütün Qruplara Elanınız Göndərildi.**")
