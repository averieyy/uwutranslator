import discord
import uwu
import secret

token = ""

with open("token.txt", "r") as f:
    token = f.readline()

bot = discord.Client()

@bot.event
async def on_ready():
    print(uwu.translate('tanslator set up and ready to go'))

ROLEGETMSG = 939701249920626728

@bot.event
async def on_message(msg:discord.Message):
    print(msg.content)
    if msg.author != bot.user:
        uwurole = msg.author.guild.get_role(secret.UWUROLEID)
        if uwurole in msg.author.roles and '<@!939666764969701406>' not in msg.content:
            translatedmsg = uwu.translate(msg.content)
            try:
                await msg.edit(content=translatedmsg)
            except:
                await msg.channel.send(translatedmsg)

        if '<@!939666764969701406>' in msg.content and msg.reference != None:
            message:discord.Message = await msg.channel.fetch_message(int(msg.reference.message_id))
            translatedmsg = uwu.translate(message.content)
            try:
                await msg.edit(content=translatedmsg)
            except:
                await msg.channel.send(translatedmsg)
    if msg.content == '!roleprint':
        embeds = ['😳', '🐍', '🎲', '🕹']
        roleembed = discord.Embed()
        roleembed.title = 'React to the different emojis to get different roles'
        roleembed.add_field(name='Emojis', value='<@&939669513992036383>: :flushed:\n<@&939689679203209216>: :snake:\n<@&939689521941987358>: :game_die:\n<@&939690137527406694>: :joystick:')
        messageresponse = await msg.channel.send(embed=roleembed)
        for i in embeds:
            await messageresponse.add_reaction(emoji=i)
        print(messageresponse.id)

@bot.event
async def on_raw_reaction_add(payload:discord.RawReactionActionEvent):
    member:discord.Member = get_member(payload.guild_id, payload.user_id)

    if member == bot.user: return
    
    if payload.message_id == ROLEGETMSG:
        print('roleget')
        if payload.emoji.name == '😳': await member.add_roles(discord.utils.get(member.guild.roles, name='uwu')) # @uwu role
        if payload.emoji.name == '🐍': await member.add_roles(discord.utils.get(member.guild.roles, name='snake')) # @snake role
        if payload.emoji.name == '🎲': await member.add_roles(discord.utils.get(member.guild.roles, name='connect 4')) # @connect 4 role
        if payload.emoji.name == '🕹': await member.add_roles(discord.utils.get(member.guild.roles, name='text based adventure')) # @text based adventure role

@bot.event
async def on_raw_reaction_remove(payload:discord.RawReactionActionEvent):
    member:discord.Member = get_member(payload.guild_id, payload.user_id)

    if member == bot.user: return
    
    if payload.message_id == ROLEGETMSG:
        print('roleget')
        if payload.emoji.name == '😳': await member.remove_roles(discord.utils.get(member.guild.roles, name='uwu')) # @uwu role
        if payload.emoji.name == '🐍': await member.remove_roles(discord.utils.get(member.guild.roles, name='snake')) # @snake role
        if payload.emoji.name == '🎲': await member.remove_roles(discord.utils.get(member.guild.roles, name='connect 4')) # @connect 4 role
        if payload.emoji.name == '🕹': await member.remove_roles(discord.utils.get(member.guild.roles, name='text based adventure')) # @text based adventure role

def get_member(guild_id, user_id):
    members:list[discord.Member] = bot.get_all_members()
    for i in members:
        if i.id == user_id and i.guild.id == guild_id:
            return i

bot.run(token)