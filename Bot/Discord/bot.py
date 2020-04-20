import discord
from discord.ext import commands
from discord.utils import get
import asyncio
import logging
import logging.handlers
import random
import sys

my_logger = logging.getLogger('Discordbot launcher')
my_logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
my_logger.addHandler(handler)
my_logger.debug('Discordbot : Start of script')


bot = commands.Bot(command_prefix='!')




@bot.event
async def on_ready():
    print("Connecté en tant que : ")
    print(bot.user.name)
    print("avec l""'""ID :")
    print(bot.user.id)
    print('------------------')






# commande d'aide
bot.remove_command('help')
@bot.command()
async def help(ctx):
    try:
        await ctx.send("Coucou\nJe suis MemeAlpha\nun gentil lapin farceur !\nVoici l'aide :\n")
        embed=discord.Embed(title="Aide", color=0xff0080)
        embed.add_field(name="!help", value="Affiche cette aide", inline=False)
        embed.add_field(name="!nuke", value="Affiche un GIF de nuke", inline=False)
        embed.add_field(name="!dog", value="Je n'aime pas les chiens. Fonction qui vous kick.", inline=False)
        embed.add_field(name="!what", value="Affiche un GIF 'WHAT' aléatoire", inline=False)
        embed.add_field(name="!think", value="Affiche un GIF de réflexion aléatoire", inline=False)
        embed.add_field(name="!yes", value="Affiche un GIF d'acquiessement aléatoire", inline=False)
        embed.add_field(name="!no", value="Affiche un GIF de négation aléatoire", inline=False)
        embed.add_field(name="!hacker", value="Affiche un GIF de h@ck3r aléatoire", inline=False)
        embed.add_field(name="!miaou -- VOCAL", value="Miaule dans le channel vocal", inline=False)
        embed.add_field(name="!miaou_angry -- VOCAL", value="OCTOGONE DE CHATS", inline=False)
        embed.add_field(name="!maisoui -- VOCAL", value="Réflexion nucléaire des rollers.", inline=False)
        embed.add_field(name="!nani -- VOCAL", value="You are already dead.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# commande d'aide vocale
bot.remove_command('helpvoc')
@bot.command()
async def helpvoc(ctx):
    try:
        await ctx.send("Coucou\nJe suis MemeAlpha\nun gentil lapin farceur !\nVoici l'aide :\n")
        embed=discord.Embed(title="Aide", color=0xff0080)
        embed.add_field(name="!miaou -- VOCAL", value="Miaule dans le channel vocal", inline=False)
        embed.add_field(name="!miaou_angry -- VOCAL", value="OCTOGONE DE CHATS", inline=False)
        embed.add_field(name="!maisoui -- VOCAL", value="Réflexion nucléaire des rollers.", inline=False)
        embed.add_field(name="!nani -- VOCAL", value="You are already dead.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# commande d'aide admin
bot.remove_command('helpadmin')
@bot.command()
async def helpadmin(ctx):
    try:
        await ctx.send("Coucou\nJe suis MemeAlpha\nun gentil lapin farceur !\nVoici l'aide :\n")
        embed=discord.Embed(title="Aide", color=0xff0080)
        embed.add_field(name="!accept @user  -- ADMINS", value="Permet d'attribuer le rÃle chaton", inline=False)
        embed.add_field(name="!ban @user  -- ADMINS", value="Permet de bannir un utilisateur", inline=False)
        embed.add_field(name="!clear <int>  -- ADMINS", value="Permet de nettoyer les messages d'un channel", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# channel vocal miaou
@bot.command()
async def honteux(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/home/pi/bot/sound/honteux.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(3)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


@bot.command()
async def maisoui(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("home/pi/bot/sound/clair.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(3)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



@bot.command()
async def nani(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/nani.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(3)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


@bot.command()
async def miaou_angry(ctx):
    try:
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("/root/angry.mp3"), after=lambda e: print('done', e))
        await asyncio.sleep(4)
        await vc.disconnect()
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# simple commande ping
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping =  round(ping_ * 1000)
    await ctx.send("my ping is "+str(ping)+"ms")





# commandes giphy - on creer un tableau de liens giphy et on pioche un random
@bot.command()
async def cat(ctx):
    chats=["https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif","http://giphygifs.s3.amazonaws.com/media/13CoXDiaCcCoyk/giphy.gif","https://media.giphy.com/media/Q94xQWspTUkShljj8P/giphy.gif","https://media.giphy.com/media/WXB88TeARFVvi/giphy.gif","https://media.giphy.com/media/5i7umUqAOYYEw/giphy.gif","https://media.giphy.com/media/GFHJXPCoVQEec/giphy.gif","https://media.giphy.com/media/3oEdvbAVPeVsPDQL5u/giphy.gif","https://media.giphy.com/media/Nm8ZPAGOwZUQM/giphy.gif","https://media.giphy.com/media/QyJ0We4GHpjBa7PvKL/giphy.gif","https://media.giphy.com/media/mlvseq9yvZhba/giphy.gif","https://media.giphy.com/media/NjevnbNiUmeLm/giphy.gif","https://media.giphy.com/media/cuPm4p4pClZVC/giphy.gif","http://giphygifs.s3.amazonaws.com/media/nR4L10XlJcSeQ/giphy.gif","https://media.giphy.com/media/jRlP4zbERYW5HoCLvX/giphy.gif"]
    thisone = random.choice(chats)
    await ctx.send(str(thisone))

@bot.command()
async def dog(ctx):
    await ctx.author.kick(reason="Miaou")
    await ctx.send("NON.")

@bot.command()
async def what(ctx):
    whats =["https://media.giphy.com/media/puOukoEvH4uAw/giphy.gif", "https://media.giphy.com/media/oOTTyHRHj0HYY/giphy.gif", "https://media.giphy.com/media/CiYImHHBivpAs/giphy.gif", "https://media.giphy.com/media/g9SURfIJouBck/giphy.gif", "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", "https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif"]
    thisone = random.choice(whats)
    await ctx.send(str(thisone))

@bot.command()
async def think(ctx):
    thinks =["https://media.giphy.com/media/BmmfETghGOPrW/giphy.gif", "https://media.giphy.com/media/26xBI73gWquCBBCDe/giphy.gif", "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", "https://media.giphy.com/media/21I1WOUDnct4EmSNa6/giphy.gif", "https://media.giphy.com/media/Caey86HvbOPuPwHrsx/giphy.gif", "https://media.giphy.com/media/dJ4vNQ7r72pb4nDhN5/giphy.gif"]
    thisone = random.choice(thinks)
    await ctx.send(str(thisone))

@bot.command()
async def yes(ctx):
    yess = ["https://media.giphy.com/media/yFs12GkGa4Cpq/giphy.gif","http://giphygifs.s3.amazonaws.com/media/nFjDu1LjEADh6/giphy.gif","https://media.giphy.com/media/WQr2txk5iEYUS6Kv3d/giphy.gif","http://giphygifs.s3.amazonaws.com/media/NEvPzZ8bd1V4Y/giphy.gif","https://media.giphy.com/media/10Jpr9KSaXLchW/giphy.gif","https://media.giphy.com/media/oGO1MPNUVbbk4/giphy.gif"]
    thisone = random.choice(yess)
    await ctx.send(str(thisone))

@bot.command()
async def no(ctx):
    nos = ["http://giphygifs.s3.amazonaws.com/media/12XMGIWtrHBl5e/giphy.gif","https://media.giphy.com/media/eKrgVyZ7zLvJrgZNZn/giphy.gif","https://media.giphy.com/media/wYyTHMm50f4Dm/giphy.gif","https://media.giphy.com/media/pLcgO003rbeo0/giphy.gif","http://giphygifs.s3.amazonaws.com/media/g69ZPJfLy7hD2/giphy.gif","https://media.giphy.com/media/26tPlltsuA89RwYww/giphy.gif","https://media.giphy.com/media/kE8bAdv1AKdSqJf2Rw/giphy.gif","http://giphygifs.s3.amazonaws.com/media/8NQ7T1ExRuMz6/giphy.gif","https://media.giphy.com/media/23BST5FQOc8k8/giphy.gif"]
    thisone = random.choice(nos)
    await ctx.send(str(thisone))

@bot.command()
async def hacker(ctx):
    hackers = ["https://media.giphy.com/media/YQitE4YNQNahy/giphy.gif","https://media.giphy.com/media/UqxVRm1IaaIGk/giphy.gif","https://media.giphy.com/media/TOWeGr70V2R1K/giphy.gif","https://media.giphy.com/media/ZvLUtG6BZkBi0/giphy.gif","https://media.giphy.com/media/QNFhOolVeCzPQ2Mx85/giphy.gif","https://media.giphy.com/media/VbAFrrDVGAvZu/giphy.gif","https://media.giphy.com/media/Wsju5zAb5kcOfxJV9i/giphy.gif","http://giphygifs.s3.amazonaws.com/media/rMS1sUPhv95f2/giphy.gif","https://media.giphy.com/media/3oriNLx3dUqFgVi86I/giphy.gif","https://media.giphy.com/media/9kSM4y028LvvW/giphy.gif","http://giphygifs.s3.amazonaws.com/media/eCqFYAVjjDksg/giphy.gif","https://media.giphy.com/media/eDmCKa8Wd3MUU/giphy.gif","https://media.giphy.com/media/13UZisxBxkjPwI/giphy.gif","https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif"]
    thisone = random.choice(hackers)
    await ctx.send(str(thisone))



@bot.command()
async def excusetoi(ctx):
    await ctx.send("Pardon :(")


# commande pour passer un utilisateur en chaton
# uniquement pour veto et secretaire
@bot.command(pass_context=True)
async def accept(ctx, member: discord.Member):
    try:
        # role veto ou secretaire uniquement
        for role in ctx.author.roles:
            if str(role.id) == str(Humains) or str(role.id) == str(Humains):
                print(member)
                role = discord.utils.get(member.guild.roles, id=ALL)
                print(role)
                await member.add_roles(role)
                await ctx.send(str(member)+" est devenu un petit chaton !")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


# commande pour ban un utilisateur
@bot.command()
async def ban(ctx, member: discord.Member):
    try:
        await ctx.send("Miaou !")
        my_logger.debug('Discordbot : Ban demandé pour '+str(member))
        if str(member) == "Ethandudu#4268":
            await ctx.send("Le maitre des croquettes ne peut pas être banni !")
        # role veto ou secretaire uniquement
        for role in ctx.author.roles:
            if str(role.id) == str(Humains) or str(role.id) == str(Humains):
    	        my_logger.debug('Discorbot : '+str(member)+" a été banni !")
    	        await member.ban(reason="Miaou")
    	        await ctx.send(str(member)+" a été banni !")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


# commande de bienvenue - envoie un message a l'utilisateur dans le chan d'arrivee
@bot.event
async def on_member_join(member):
    try:
        print(str(member)+"has joined")
        my_logger.debug('Discorbot : '+str(member)+"has joined")
        channel = member.guild.text_channels[0]
        await asyncio.sleep(2)
        await member.send("Coucou !\n\nJe suis Minou le gentil chaton\nPour le moment seul le channel \#la-chatiere t'est accessible\nMerci de bien vouloir compléter cette présentation \n(directement dans le channel \#la-chatiere, pas ici !)\nafin qu'un modérateur valide ta candidature : \n\nTon âge : \nTes domaines de compétences (réseau, systèmes, web, dev) : \nDonne un compliment sur les chats : ")
        await channel.send( member.mention + " has joined !")
        await channel.send("Bienvenue !\n\nJe suis Minou le gentil chaton\nPour le moment seul ce channel t'est accessible\nMerci de bien vouloir compléter cette présentation\nafin qu'un modérateur valide ta candidature : \n\nTon âge : \nTes domaines de compétences (réseau, systèmes, web, dev) : \nDonne un compliment sur les chats : ")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


# commande de sortie - previent du depart d'un utilisateur
@bot.event
async def on_member_remove(member):
    try:
        print(str(member)+"has quit")
        my_logger.debug('Discorbot : '+str(member)+"has quit")
        channel = member.guild.text_channels[1]
        await channel.send(str(member)+" a quitté le serveur.\nY-a-t'il un soucis avec les croquettes ?")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


# commande de nettoyage d'un channel - specifier le nb de lignes
@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    try:
        for role in ctx.author.roles:
            if str(role.id) == str(Humains) or str(role.id) == str(Humains):
                channel=ctx.message.channel
                messages=[]
                async for message in channel.history(limit=int(amount)):
                    messages.append(message)
                await channel.delete_messages(messages)
                await ctx.send("La litière a été vidée.")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))




try:
    bot.run("token")
except KeyboardInterrupt:
        print("\n\n************************************\n\n")
