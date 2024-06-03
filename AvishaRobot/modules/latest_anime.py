from pyrogram import filters
import requests
from AvishaRobot import pbot

@pbot.on_message(filters.command('latest'))
def schedule(_, message):
    results = requests.get('https://subsplease.org/api/?f=schedule&h=true&tz=Japan').json()
    text = None
    for result in results['schedule']:
        title = result['title']
        time = result['time']
        aired = bool(result['aired'])
        title = f"**[{title}](https://subsplease.org/shows/{result['page']})**" if not aired else f"**~~[{title}](https://subsplease.org/shows/{result['page']})~~**"
        data = f" {title} ➥ **{time}**"
        
        if text:
            text = f"{text}\n{data}"
        else:
            text = data

    message.reply_text(f"❖ ᴛᴏᴅᴀʏ's ʟᴇᴛᴀsᴛ ᴀɴɪᴍᴇ sᴄʜᴇᴅᴜʟᴇ\n\n● ᴛɪᴍᴇ-ᴢᴏɴᴇ ➥ ᴛᴏᴋʏᴏ (ɢᴍᴛ +9)\n\n{text}")



