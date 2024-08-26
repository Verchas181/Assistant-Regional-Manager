import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import openai

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
DISCORDTOKEN = os.getenv('DISCORDTOKEN')
OPENAITOKEN = os.getenv('OPENAIAPIKEY')

# Configurar a API do OpenAI
openai.api_key = OPENAITOKEN

intents = discord.Intents.default()
intents.message_content = True  # Bot lê o conteúdo das mensagens


bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'Aqui é o Dwight Schrute da Dunder Mifflin. Com quem falo?')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Todos os meus heróis são jogadores de tênis de mesa. Zoran Primorac, Jan-Ove Waldner, Wang Tao, Jorg Rosskopf e, claro, Ashraf Helmy. Tenho até um pôster em tamanho real de Hugo Hoyama na parede')

async def consultar_chatgpt(pergunta: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pergunta,
        max_tokens=300
    )
    return "Hey, Michael! Segue o que achei no ChatGPT: " + response.choices[0].text.strip()

@bot.command(name='pesquisar')
async def pesquisar(ctx, *, pergunta: str):
    resposta = await consultar_chatgpt(pergunta)
    await ctx.send(resposta)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Processa outros comandos
    await bot.process_commands(message)

@bot.command(name='help')
async def help(ctx):
    commands_list = [command.name for command in bot.commands]
    help_message = 'Comandos disponíveis:\n' + '\n +'.join(commands_list)
    await ctx.send(help_message)

### FAZER IMPLEMENTAÇÃO DO PREÇO DO BITCOIN ###

# Rodar o bot
if __name__ == "__main__":
    bot.run(DISCORDTOKEN)
