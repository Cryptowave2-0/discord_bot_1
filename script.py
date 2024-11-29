# bot.py
import discord, os, time, logs, json
from discord.ext import commands, tasks
from itertools import cycle
from datetime import datetime
from colorama import Fore, Back, Style


dir_path = os.path.dirname(os.path.realpath(__file__))
settingdict = json.load(open(dir_path + "/settings.json", "r"))

bot = commands.Bot(command_prefix="!", help_command=None, intents=discord.Intents.all())


async def server_in():
    for i in bot.guilds:
        if str(i.id) in settingdict["servers"]:
            pass
        else:
            settingdict
            settingdict["servers"][str(i.id)] = settingdict["server_patern"]
            json.dump(settingdict, open(dir_path + "/settings.json", "w"), indent=4)


@bot.event
async def on_ready():
    await logs.log(f"Logged in as {bot.user.name}", "EVENT")
    await server_in()

@bot.event
async def on_member_join(member):
        await logs.log(member.guild.id, "DEBUG")
        try:
            for i in settingdict['servers'][f'{member.guild.id}']["welcome_roles"]:
                await member.add_roles(member.guild.get_role(i), reason="he's new member")
        except Exception as e:
            await logs.log(e, "ERROR", bot, member.guild.id)
        try:
            channel = discord.utils.get(member.guild.channels, id=settingdict['servers'][f'{member.guild.id}']["welcome_channel"]) # Remplacez 'bienvenue' par le nom du salon où vous souhaitez envoyer l'embed
        except KeyError:
            await logs.log(KeyError, "ERROR", bot, member.guild.id)
        except AttributeError:
            await logs.log(KeyError, "ERROR", bot, member.guild.id)
        embed = discord.Embed(title='Nouveau joueur !', description=f'Bienvenue {member.mention} sur le serveur !', color=discord.Color.green())
        embed.set_thumbnail(url=member.avatar)
        await channel.send(embed=embed)
        await logs.log(f"Welcome to {member.name} ({member.id}) in {member.guild.name} ({member.guild.id})", "EVENT")

@bot.event
async def on_member_remove(member):
        discord.member.Member.guild.channels
        try:
            channel = discord.utils.get(member.guild.channels, id=settingdict['servers'][f'{member.guild.id}']["bye_channel"]) # Remplacez 'bienvenue' par le nom du salon où vous souhaitez envoyer l'embed
        except KeyError:
            await logs.log(KeyError, "ERROR", bot, member.guild.id)
        except AttributeError:
            await logs.log(KeyError, "ERROR", bot, member.guild.id)
        embed = discord.Embed(title='Départ d\'un joueur', description=f'Au revoir {member.mention} !', color=discord.Color.red())
        embed.set_thumbnail(url=member.avatar)
        await channel.send(embed=embed)
        await logs.log(f"Bye to {member.name} ({member.id}) in {member.guild.name} ({member.guild.id})", "EVENT")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('hi'):
        return await message.channel.send('Hi there!')
    elif 'test_log' in message.content.lower():
        guild_id = message.guild.id
        return await logs.log('Hi there!', "DEBUG", bot, message.guild.id)

# Lancez la boucle d'événements du bot
bot.run(settingdict['bot']['TOKEN'])