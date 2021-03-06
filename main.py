import math
import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "dpy!")

def round_to_place(number, decimal = 1):
    factor = 10.0**decimal
    return math.trunc(number*factor)/factor

@client.event
async def on_ready():
    await client.change_presence(
        activity = discord.Activity(
            type = discord.ActivityType.listening,
            name = "corridones"
        )
    )

@client.command()
async def pato(ctx):
	new_embed = discord.Embed(
		title = "Un pato",
		description = f"Cuá cuá, {ctx.message.author.mention}, ¡aquí está tu pato!",
		colour = discord.Colour.blue()
	)

	new_embed.set_author(name = "DesarrollaBot.py")
	new_embed.set_image(url = "https://www.random-d.uk/api/randomimg")
	await ctx.send(embed = new_embed)

@client.command()
@commands.has_permissions(administrator = True)
async def repetir(ctx, message):
	await ctx.message.delete()
	await ctx.send(message)

@client.command()
async def redes(ctx):
    await ctx.send(
        """
Twitter: <https://twitter.com/dh_rblx>
Sitio web: <https://desarrolladoreshispanos.com>
GitHub: <https://github.com/Desarrolladores-Hispanos>
Grupo de Roblox: <https://www.roblox.com/groups/9369198/Desarrolladores-Hispanos>
Discord: pues ya estás en el servidor xd
        """
    )

@client.command()
@commands.has_permissions(manage_messages = True)
async def eliminar(ctx, cantidad):
    await ctx.channel.purge(limit = int(cantidad) + 1)

@client.command()
async def convertir_a_robux(ctx, usd):
    usd = float("%.2f" % float(usd)) # definitivamente hay una mejor manera de hacer esto xd
    await ctx.send("USD %s son <:robux:806422545359306752> %s" % (f"{usd:,}", f"{round_to_place(usd/0.0035, 2):,}"))

@client.command()
async def convertir_a_usd(ctx, robux):
    robux = int("%.2f" % int(robux)) # definitivamente hay una mejor manera de hacer esto xd
    await ctx.send("<:robux:806422545359306752> %s son USD $%s" % (f"{robux:,}", f"{round_to_place(robux*0.0035, 2):,}"))

client.run(os.getenv("BOT_TOKEN"))