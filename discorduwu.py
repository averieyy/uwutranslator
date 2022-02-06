import discord
import uwu
import secret

bot = discord.Client()

@bot.event
async def on_ready():
    print(uwu.translate('tanslator set up and ready to go'))

@bot.event
async def on_message(msg:discord.Message):
    print(msg.content)
    if msg.author != bot.user:
        if '<@!939666764969701406>' in msg.content and msg.reference != None:
            
            message:discord.Message = await msg.channel.fetch_message(int(msg.reference.message_id))
            translatedmsg = uwu.translate(message.content)
            try:
                await msg.edit(content=translatedmsg)
            except:
                await msg.channel.send(translatedmsg)

bot.run(secret.DISCORDTOKEN)