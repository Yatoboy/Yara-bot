import discord
from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix='=')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('yara.tags'):
        MessageString = ''
        TagsList = open("tags list.txt", 'r')
        StringMaker= TagsList.readline()
        MessageString += StringMaker
        await client.send_message(message.channel, str(MessageString))
    if message.content.startswith('yara.tag'):
        if message.content.startswith('yara.tag.new'):  # Creating a new tag
            CommandName,CommandContent = message.content[len('yara.tag.new')+1:].split(" | ")
            TagsList = open("tags list.txt", 'r')
            ReadTagsList = TagsList.readline()
            while len(ReadTagsList) > 0:
                if CommandName in TagsList == True:
                    TagFound = True
                else: TagFound = False
            if TagFound == False:
                filehandle = open('tags.txt', 'a')
                CommandString = '\n {0} {1}'.format(CommandName, CommandContent)
                filehandle.write(CommandString)
                messagesend = 'The tag `{0}` has been added'.format(CommandName)
                TagsList = open("tags list.txt", 'a').write
                TagsList('{0} \n'.format(CommandName))
                await client.send_message(message.channel, messagesend)
            else:
                await client.send_message(message.channel, 'This tag already exists')
        else:  # getting the tag
            filehandle = open('tags.txt', 'r')
            textline = filehandle.readline()
            CommandFound = False
            Command, CommandName = message.content.split(' ')
            while textline.startswith(CommandName) == False and len(textline) > 0:
                print(textline)
                textline = filehandle.readline()
                CommandFound = True
            if CommandFound == True:
                CommandMessage = textline[len(CommandName):]
            else: CommandMessage = 'tag not found'
            await client.send_message(message.channel, CommandMessage)

client.run(token)
