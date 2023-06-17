import discord
from discord.ext import commands
from bot_token import token 
import requests, os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('Python/M2L1/images/mem2.jpg', 'rb') as f: 
        picture = discord.File(f)
    await ctx.send(file=picture)


######## Random Meme
@bot.command()
async def memr(ctx):
    img_name = random.choice(os.listdir('Python/M2L1/images'))
    
    with open(f'Python/M2L1/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    
    await ctx.send(file=picture)


######### Extra Task API
# def get_duck_image_url():
#     url = 'https://random-d.uk/api/random'
#     res = requests.get(url)
#     data = res.json()
#     return data['url']

# @bot.command('duck')
# async def duck(ctx):
#     '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır'''
#     image_url = get_duck_image_url()
#     await ctx.send(image_url)




bot.run(token)