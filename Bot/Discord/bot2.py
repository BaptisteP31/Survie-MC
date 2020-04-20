import json

# on importe le module discord.py
import discord

from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands

# une commmande
# !regles =regles #regles

# créer le bot
bot = commands.Bot(command_prefix='!')
warnings = {}

with open('warnings.json', 'r') as infile:
    warnings = json.load(infile)

# détecter quand le bot est pret ("allumé")
@bot.event
async def on_ready():
    print("Bot pret")
    await bot.change_presence(status=discord.Status.idle,
            activity=discord.Game("Graven est en live"))


# détecter quand quelqu'un ajoute un emoji sur un message
@bot.event
async def on_raw_reaction_add(payload):

    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message

    python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    # verifier si l'emoji qu'on a ajoutée est "python"
    if canal == 700350381250838560 and message == 700350680677744761 and emoji == "python":
        print("Grade ajouté !")
        await membre.add_roles(python_role)
        await membre.send("Tu obtiens le grade python !")


# détecter quand quelqu'un ajoute un emoji sur un message
@bot.event
async def on_raw_reaction_remove(payload):

    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id # recupere le numero du messae

    python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)

    # verifier si l'emoji qu'on a ajoutée est "python"
    if canal == 700350381250838560 and message == 700350680677744761 and emoji == "python":
        print("Grade supprimé !")
        await membre.remove_roles(python_role)
        await membre.send("Tu perds le grade python !")


# créer la commande !regles
@bot.command()
async def regles(ctx):
    await ctx.send("Les règles:\n1. Pas d'insultes\n2. Pas de double compte\n3. Pas de spam")

# créer la commande !warning
@bot.command()
@commands.has_role("Admin")
async def warning(ctx, membre: discord.Member):
    pseudo = membre.mention
    id = membre.id

    # si la personne n'a pas de warning
    if id not in warnings:
        warnings[id] = 0
        print("Le membre n'a aucun avertissement")

    warnings[id] += 1

    print("ajoute l'avertissement", warnings[id], "/3")

    # verifier le nombre d'avertissements
    if warnings[id] == 3:
        # remet à les warnings
        warnings[id] = 0
        # message
        await membre.send("Vous avez été éjécté du serveur ! trop d'avertissements !")
        # ejecter la personne
        await membre.kick()

    # mettre à jour le fichier json
    with open('warnings.json', 'w') as outfile:
        json.dump(warnings, outfile)

    await ctx.send(f"Le membre {pseudo} a reçu une alerte ! Attention à bien respecter les regles")

# verifier l'erreur si la commande !warning
@warning.error
async def on_command_error(ctx, error):
    # detecter cette erreur
    if isinstance(error, commands.MissingRequiredArgument):
        # envoyer un message
        await ctx.send("Tu dois faire !warning @pseudo")


# créer la commande !bienvenue @pseudo
@bot.command()
async def bienvenue(ctx, nouveau_membre: discord.Member):
    # recupere le nom
    pseudo = nouveau_membre.mention

    # executer le message de bienvenue
    await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord ! N'oublie pas de faire !regles")

# verifier l'erreur
@bienvenue.error
async def on_command_error(ctx, error):
    # detecter cette erreur
    if isinstance(error, commands.MissingRequiredArgument):
        # envoyer un message
        await ctx.send("Tu dois faire !bienvenue @pseudo")



# phrase
print("Lancement du bot...")

# connecter au serveur
bot.run("VOTRE-JETON")
