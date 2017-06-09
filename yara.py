import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='=')
tags = []
tagtext = []

def ReadExistingTags():
    with open('tags.txt', 'r') as f:
        for line in f:
            TagLine = line.split('|')
            tags.append(TagLine[0])
    return tags

def ReadExistingTagText():
    with open('tags.txt', 'r') as f:
        for line in f:
            TagLine = line.split('|')
            tagtext.append(TagLine[1])
    return tagtext


def WriteNewTag(linetowrite):
    WritingTag = open('tags.txt', 'a')
    WritingTag.write(linetowrite)
    WritingTag.close()
# ------------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content == '-tags':
        ReadExistingTags()
        messagestring = ' '
        for i in tags:
            messagestring = messagestring + i + ', '
        await client.send_message(message.channel, 'available tags are `{0}`'.format(messagestring))
        print(message.content, message.author.name, message.channel)
    elif message.content.startswith('-createtag '):
        linetowrite = message.content[len('-createtag '):] + '\n'
        ReadExistingTags()
        tagname = linetowrite.split('|')
        if tagname[0] in tags:
            await client.send_message(message.channel, 'tag already exists')
        else:
            WriteNewTag(linetowrite)
            await client.send_message(message.channel, 'tag `{0}` created :+1:'.format(tagname[0]))
        print(message.content)
    elif message.content.startswith('-tag'):
        tagname = message.content[len('-tag '):]
        ReadExistingTags()
        if tagname in tags:
            count = 0
            for i in tags:
                count += 1
                if tagname == i:
                    break
            ReadExistingTagText()
            messagestring = tagtext[count-1]
            await client.send_message(message.channel, messagestring)
        else:
            await client.send_message(message.channel, 'tag does not exist')

#token = token
#client.run(token)
