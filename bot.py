#Code By Success
#Discord Success#6656

import discord
import datetime
from discord.ext import commands
from discord.colour import Color
from mcstatus import MinecraftBedrockServer,MinecraftServer



client = commands.Bot(command_prefix="")
client.remove_command("help")

@client.command()
async def help(message):
    embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.green(),timestamp=datetime.datetime.utcnow())
    embed.add_field(name ="Help",value=f"`!help (เครื่่องมือช่วยเหลือ)`\n`!tcp [IP SERVER] [PORT] (เช็ค Status MineCraft ถ้าไม่รู้ Port ไม่ต้องใส่ก็ได้)`\n`!udp [IP SERVER] [PORT] (เช็ค Status MineCraft ถ้าไม่รู้ Port ไม่ต้องใส่ก็ได้)`",inline=False)
    embed.set_footer(text='Made By Success')
    await message.send(embed=embed)


@client.event
async def on_connect():
    print(f"Login as : {client.user.name}#{client.user.discriminator}")


@client.command()
async def tcp(message, ip, port=None):
    if message.guild:
        if port == None:
            try:
                server = MinecraftServer.lookup(f"{ip}")
                status = server.status()
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.green(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🟢`\n`Host : {ip}`\n`Ping : {round(status.latency)} ms`\n`Play : {status.players.online} คน`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed)
            except:
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.red(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🔴`\n`Host : {ip}`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed, delete_after=10)
                await message.message.delete()
        else:
            try:
                server = MinecraftServer.lookup(f"{ip}:{port}")
                status = server.status()
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.green(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🟢`\n`Host : {ip}`\n`Port : {port}`\n`Ping : {round(status.latency)} ms`\n`Play : {status.players.online} คน`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed)
            except:
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.red(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🔴`\n`Host : {ip}`\n`Port : {port}`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed, delete_after=10)
                await message.message.delete()

@client.command()
async def udp(message, ip, port=None):
    if message.guild:
        if port == None:
            try:
                server = MinecraftServer.lookup(f"{ip}")
                status = server.status()
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.green(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🟢`\n`Host : {ip}`\n`Ping : {round(status.latency)} ms`\n`Play : {status.players.online} คน`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed)
            except:
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.red(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🔴`\n`Host : {ip}`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed, delete_after=10)
                await message.message.delete()

        else:
            try:
                server = MinecraftServer.lookup(f"{ip}:{port}")
                status = server.status()
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.green(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🟢`\n`Host : {ip}`\n`Port : {port}`\n`Ping : {round(status.latency)} ms`\n`Play : {status.players.online} คน`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed)
            except:
                embed = discord.Embed(title="🌐 MINECRAFT | CHECKER",color=discord.Colour.red(),timestamp=datetime.datetime.utcnow())
                embed.add_field(name ="INFO",value=f"`Status 🔴`\n`Host : {ip}`\n`Port : {port}`",inline=False)
                embed.set_footer(text='Made By Success')
                await message.send(embed=embed, delete_after=10)
                await message.message.delete()

client.run("", reconnect=True)
