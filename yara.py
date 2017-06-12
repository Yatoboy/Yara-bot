import discord
from discord.ext import commands
from os import listdir, remove

client = discord.Client()
bot = commands.Bot(command_prefix='=')
tagtext = []


def ReadExistingTags():
    tags = listdir('tags/')
    return tags


def ReadExistingTagText(TagName):
    with open('tags/'+TagName, 'r') as f:
        tagtext = ''
        for line in f:
            tagtext = str(tagtext + line + ' \n')
    return tagtext


def WriteNewTag(linestowrite, TagName):
    WritingTag = open('tags/'+TagName, 'w')
    WritingTag.write(linestowrite)
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
        tags = ReadExistingTags()
        messagestring = ' '
        for i in tags:
            messagestring = messagestring + ' -' + i + ' '
        await client.send_message(message.channel, 'available tags are `{0}`'.format(messagestring))
        print(message.content, message.author.name, message.channel)
    elif message.content.startswith('-createtag '):
        if '\n' in message.content:
            await client.send_message(message.channel, 'Sorry we do not support multiline commands currently')
        else:
            linetowrite = message.content[len('-createtag '):] + '\n'
            tags = ReadExistingTags()
            tagname = linetowrite.split('|')
            if tagname[0] in tags:
                await client.send_message(message.channel, 'tag already exists')
            else:
                stringtowrite = ''
                for i in tagname[1:]:
                    stringtowrite += i
                WriteNewTag(stringtowrite, tagname[0])
                await client.send_message(message.channel, 'tag `{0}` created :+1:'.format(tagname[0]))
            print(message.content)
    elif message.content.startswith('-tag'):
        tagname = message.content[len('-tag '):]
        tags = ReadExistingTags()
        if tagname in tags:
            messagestring = ReadExistingTagText(tagname)
            await client.send_message(message.channel, messagestring)
        else:
            await client.send_message(message.channel, 'tag does not exist')
    elif message.content.startswith('-deltag'):
        tags = ReadExistingTags()
        tagname = message.content[len('-deltag '):]
        if tagname in tags:
            remove('tags/{0}'.format(tagname))
            await client.send_message(message.channel, 'The tag `{0}` has been successfully removed :+1::skin-tone-2:'.format(tagname))
        else: await client.send_message(message.channel, 'Tag does not exist, please check your spelling or use the `-tags` command to check what tags are available')

#token = token
#client.run(token)
