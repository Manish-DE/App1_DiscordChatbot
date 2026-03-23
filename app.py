
import os
from ollama import chat
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ollama

load_dotenv() # Load environment variables from .env file

intents = discord.Intents.default()  # Create default intents
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready as  {bot.user.name}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello! I am a chatbot powered by Ollama. Ask me anything using /ask command!')

@bot.command(name='ask') # Command to ask a question to the chatbot
async def ask(ctx, *, question):    
        print(f"Received question: {question}")
        print("______________________________________  __________________________")

        response = chat(model='llama3', messages=[
             {
                  'role': 'system', 
                  'content': '''You are a helpful assistantwho provides 
                                concise and accurate answers to user questions 
                                in no more than 300 words.'''
            },
            {
                'role': 'user',
                'content': question,
            },
        ])  
        print(f"Received response: {response.message.content}")
        await ctx.send(response.message.content)

@bot.command(name='summarize') # Command to summarize the last 10 messages in the channel
async def summarize(ctx):
    msg = [message.content async for message in ctx.channel.history(limit=10)]
    summarize_prompt = f"""
            Summarize the following message delimited by 3 backticks:
             '''
              {msg} 
             '''
            """    


    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': '''You are a helpful assistant who summarises the provided messages in no more than 100 words.'''
        },
        {
            'role': 'user',
            'content': summarize_prompt
        }
    ])
    print(f"Received summary: {response['message']['content']}")
    await ctx.send(response['message']['content'])

@bot.command(name='clear') # Command to clear a specified number of messages (default is 5)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages!', delete_after=5)


@bot.command(name='helpme') # Command to show a help message with available commands
async def helpme(ctx):
    help_text = """
    **Available Commands:**
    - `/hello`: Greet the bot.
    - `/ask <question>`: Ask a question to the bot.
    - `/summarize`: Summarize the last 10 messages in the channel.
    - `/clear [amount]`: Clear a specified number of messages (default is 5).
    - `/helpme`: Show this help message.
    """
    await ctx.send(help_text)

@bot.command(name='ping') # Command to check if the bot is responsive
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command(name='news') # Command to fetch the latest news using a news API
async def news(ctx):
    news_prompt = """
    Fetch the latest news headlines and provide a brief summary for each headline. 
    Limit the response to 5 headlines with summaries.
    """
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': '''You are a helpful assistant who provides concise and accurate news summaries in no more than 300 words.'''
        },
        {
            'role': 'user',
            'content': news_prompt
        }
    ])
    print(f"Received news: {response['message']['content']}")
    await ctx.send(response['message']['content'])

@bot.command(name='linkedInfo') # Command to fetch information about a LinkedIn profile
async def linkedInfo(ctx, linkedin_url):
    linked_info_prompt = f"""
    Fetch information about the LinkedIn profile at the following URL: {linkedin_url}. 
    Provide a summary of the person's professional background, skills, and recent activity.
    """
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'system',
            'content': '''You are a helpful assistant who provides concise and accurate summaries of LinkedIn profiles in no more than 300 words.'''
        },
        {
            'role': 'user',
            'content': linked_info_prompt
        }
    ])
    print(f"Received LinkedIn info: {response['message']['content']}")
    await ctx.send(response['message']['content'])



bot.run(os.getenv('DISCORD_BOT_TOKEN'))
