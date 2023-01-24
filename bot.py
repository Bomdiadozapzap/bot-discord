import discord, datetime, asyncio
from datetime import datetime
from discord import guild
from discord import channel
from discord import permissions
from discord import activity
from discord.colour import Color
from discord.utils import get
from discord.ext import commands
import os


intents = discord.Intents.default()
intents.members = True


client = commands.Bot(command_prefix="!" , case_insentitive=True, intents=intents)
ROLE = '👨SEM WHITELIST'






@client.event
async def on_ready():
   print("estou pronto!")



@client.command()
async def say(ctx, *, mensagem):
    embed = discord.Embed(title=f"{mensagem}", description=f"Mensagem enviada por {ctx.author.name}", color=0xff0000)
    await ctx.send(embed=embed)



@client.event #entrada
async def on_member_join(member):
    server_name = "nome do server"
    guild = member.guild
    role = get(member.guild.roles, name=ROLE) #cargos
    await member.add_roles(role)


    canalboasvindas = client.get_channel(916518428288892968)
    regras = client.get_channel(916781999950291024)
    embed = discord.Embed(title=f'Bem-Vindo(a)!', description=f'bem vindo a {server_name} {member.mention}! divirta-se, Leia as regras em {regras.mention}', color=0xff0000)
    embed.add_field(name="ID" , value=member.id)
    embed.add_field(name="Quantidade de membros:", value=len(guild.members))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/928239010483175457/936376944998645791/xpika.gif')
    embed
    mensagem = await canalboasvindas.send(embed=embed)


@client.event #saida
async def on_member_remove(member):
    guild = member.guild
    canalvaicomdeus = client.get_channel(916793079640502292)
    embed = discord.Embed(title=f"O user {member.mention} saiu!", description=f"{member.mention} saiu do server, é uma pena! espero que volte!", color=0xff0000)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/928239010483175457/936376944998645791/xpika.gif')
    mensagem = await canalvaicomdeus.send(embed=embed)




    

client.run('')