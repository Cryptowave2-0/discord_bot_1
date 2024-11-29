import discord

EmbedError = discord.Embed(title="Vous n'avez pas la permission requise", colour=discord.Colour.red())
EmbedErrorGuild = discord.Embed(title="Vous ne povez pas exécuter la commande sur ce serveur", colour=discord.Colour.red())
EmbedUserErrorNotFound = discord.Embed(title="Utilisateur non trouvé", colour=discord.Colour.red())
EmbedMissingPermissions = discord.Embed(title="Je manque de permissions", colour=discord.Colour.red())