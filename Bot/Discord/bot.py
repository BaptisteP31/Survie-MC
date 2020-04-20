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


bot = commands.Bot(command_prefix='$')



@bot.event
async def on_ready():
    print("Connecté en tant que : ")
    print(bot.user.name)
    print("avec l""'""ID :")
    print(bot.user.id)
    print('------------------')
    game = discord.Game("préfixe ""'$'""")
    await bot.change_presence(status=discord.Status.online, activity=game)



# commande d'aide
bot.remove_command('help')
@bot.command()
async def help(ctx):
    try:
        await ctx.send("Voici l'aide :")
        embed=discord.Embed(title="Aide", color=808080)
        embed.add_field(name="?help", value="Affiche cette aide", inline=False)
        embed.add_field(name="?assassin", value="Affiche la description du rôle **Assassin**", inline=False)
        embed.add_field(name="?detective", value="Affiche la description du rôle **Détective**", inline=False)
        embed.add_field(name="?traitre", value="Affiche la description du rôle **Traître**", inline=False)
        embed.add_field(name="?parrain", value="Affiche la description du rôle **Parrain**", inline=False)
        embed.add_field(name="?sousfifre", value="Affiche la description du rôle **Sous Fifre**", inline=False)
        embed.add_field(name="?infirmier", value="Affiche la description du rôle **Infirmier**", inline=False)
        embed.add_field(name="?vengeur", value="Affiche la description du rôle **Vengeur**", inline=False)
        embed.add_field(name="?tueur", value="Affiche la description du rôle **Tueur**", inline=False)
        embed.add_field(name="?bruh + valeur -- STAFF ONLY", value="Nettoie tout le tchat si aucun nombre n'est spécifié. Pour définir un nombre de messages à supprimer il faut mettre une valeur", inline=False)
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



# commande d'aide assassin
bot.remove_command('assassin')
@bot.command()
async def assassin(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Assassin**__ :")
        embed=discord.Embed(title="Aide **Assassin**", color=0xFF0000)
        embed.add_field(name="Nombre :", value="3", inline=False)
        embed.add_field(name="Description :", value="Ils peuvent tuer n’importe qui, même l’un d’entre eux.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# commande d'aide détective
bot.remove_command('detective')
@bot.command()
async def detective(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Détective**__ :")
        embed=discord.Embed(title="Aide **Détective**", color=993300)
        embed.add_field(name="Nombre :", value="2", inline=False)
        embed.add_field(name="Description :", value="Les détectives doivent trouver et démasquer les assassins. Ils devront trouver trois objets pour recevoir un indice et un pistolet nerf sera caché quelque part. Leur but sera de le trouver pour tirer les balle qui seront cachées dans la même maison.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# commande d'aide traître
bot.remove_command('traitre')
@bot.command()
async def traitre(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Traître**__ :")
        embed=discord.Embed(title="Aide **Traître**", color=000000)
        embed.add_field(name="Nombre :", value="1", inline=False)
        embed.add_field(name="Description :", value="Peut tuer 1 personne. N'ayant pas d'équipiers, son but est de gagner la partie seul. Ou avec villageois si lui + 2 villageois. Il a la possibilité de tuer deux personnes grâce à des balles qu’il devra trouver dans la maison.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# commande d'aide parrain
bot.remove_command('parrain')
@bot.command()
async def parrain(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Parrain**__ :")
        embed=discord.Embed(title="Aide **Parrain**", color=0x003300)
        embed.add_field(name="Nombre :", value="1", inline=False)
        embed.add_field(name="Description :", value="Peut désigner un sous fifre et tuer s’il tue quelqu’un, il se suicide. Si son sous fifre meurt, il peut le rejoindre sans se faire tuer au bout de deux minutes pour qu’il lui révèle le nom de son assassin. Du coup + 1 kill.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))      



# commande d'aide sous fifre
bot.remove_command('sousfifre')
@bot.command()
async def sousfifre(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Sous Fifre**__ :")
        embed=discord.Embed(title="Aide **Sous Fifre**", color=0x006600)
        embed.add_field(name="Nombre :", value="1", inline=False)
        embed.add_field(name="Description :", value="Remplace l’ancien rôle du joueur s'il tue quelqu'un après être désigné par le parrain. il n’a le droit que de tuer ses cibles. Il peut tuer jusqu’à 3 personnes.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))      



# commande d'aide infirmier
bot.remove_command('infirmier')
@bot.command()
async def infirmier(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Infirmier**__ :")
        embed=discord.Embed(title="Aide **Infirmier**", color=0xFF3366)
        embed.add_field(name="Nombre :", value="1", inline=False)
        embed.add_field(name="Description :", value="A le pouvoir de réanimer une personne grâce à un objet qu’il devra trouver durant la partie.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))      



# commande d'aide protecteur
bot.remove_command('vengeur')
@bot.command()
async def vengeur(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Vengeur**__ :")
        embed=discord.Embed(title="Aide **Vengeur**", color=0x0000FF)
        embed.add_field(name="Nombre :", value="1", inline=False)
        embed.add_field(name="Description :", value="Désigne une personne en qui il a confiance. Si cette personne meurt, il pourra la rejoindre en 5 minute pour récolter le nom de son assassin et la venger.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))   



# commande d'aide tueur
bot.remove_command('tueur')
@bot.command()
async def tueur(ctx):
    try:
        await ctx.send("Voici la description du rôle __**Tueur en série**__ :")
        embed=discord.Embed(title="Aide **Tueur**", color=0xFFCC66)
        embed.add_field(name="Nombre :", value="1", inline=False)
        embed.add_field(name="Description :", value="Peut tuer n’importe qui et doit finir la partie seul il peut s’allier avec la personne de son choix pour gagner la partie a deux.", inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e)) 



# simple commande ping
@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping =  round(ping_ * 1000)
    await ctx.send("my ping is "+str(ping)+"ms")



# commande de bienvenue - envoie un message a l'utilisateur dans le chan d'arrivee
@bot.event
async def on_member_join(member):
    try:
        print(str(member)+"has joined")
        my_logger.debug('Discorbot : '+str(member)+"has joined")
        channel = member.guild.text_channels[0]
        await asyncio.sleep(2)
        await channel.send( member.mention + " est arrivé(e) !")
        await channel.send("Bienvenue sur le serveur du **Murder Mystery** !\n https://media1.tenor.com/images/857a9fed91255db5d4960ebe32501bbc/tenor.gif")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))


# commande de sortie - previent du depart d'un utilisateur
@bot.event
async def on_member_remove(member):
    try:
        print(str(member)+"has quit")
        my_logger.debug('Discorbot : '+str(member)+"a quitté(e)")
        channel = member.guild.text_channels[0]
        await channel.send(str(member)+" a quitté le serveur. Tu veux un octogone ?\n https://media1.tenor.com/images/84ef4bbad192d3f2c76c2e53052f0329/tenor.gif")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



# commande de nettoyage d'un channel - specifier le nb de lignes
@bot.command(pass_context=True)
async def bruh(ctx, amount=100):
    try:
        for role in ctx.author.roles:
            if str(role.id) == str(688430994579128337) or str(role.id) == str(688338602148757537):
                channel=ctx.message.channel
                messages=[]
                async for message in channel.history(limit=int(amount)):
                    messages.append(message)
                await channel.delete_messages(messages)
                await ctx.send("Tchat nettoyé ! \n https://media1.tenor.com/images/92f0e076a76dbfc580b6483fbf692e6b/tenor.gif")
    except Exception as e:
        print(str(e))
        my_logger.debug(str(e))



try:
    bot.run("token")
except KeyboardInterrupt:
        print("\n\n************************************\n\n")
