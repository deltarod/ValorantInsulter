import discord
import requests
import configparser

configFile = 'config.cfg'
config = configparser.ConfigParser()
config.read(configFile)

configSections = config.sections()

save = False

if 'general' not in configSections:
    config.add_section('general')
    config['general']['token'] = 'token_goes_here'
    save = True

if save:
    with open(configFile, 'w') as cfg:
        config.write(cfg)


magicWords = ['val', 'valorant']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        messageWords = message.content.split()

        for word in messageWords:
            if word.lower() in magicWords:
                request = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')

                test = request.json()

                await message.reply(test['insult'])


token = config['general']['token']
if token == 'token_goes_here':
    print('Set token in cfg file')
else:
    client = MyClient()
    client.run(token)