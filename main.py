import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def load_quotes(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if client.user in message.mentions and "quote" in message.content:
        quotes = load_quotes("quotes.txt")
        random_quote = random.choice(quotes)  
        await message.channel.send(random_quote)
        
    if "war" in message.content:
        await message.channel.send("The United States, as the world knows, will never start a war. We do not want war. But we will do whatever is necessary to defend our freedom.")
    
    if client.user in message.mentions and "advice" in message.content:
        await message.channel.send("Ask not what your country can do for you, ask what you can do for your country.")

    if client.user in message.mentions and "hello" in (message.content).lower():
        await message.channel.send("Hello my fellow Americans! I love the JFK Church.")

    if "I love you" in message.content:
        await message.channel.send("Thank you fellow American.")

    if "jfk" in message.content or "JFK" in message.content:
        await message.channel.send("I am JFK, the 35th President of the United States. I am here to serve my fellow Americans.")

    if "married" in message.content:
        await message.channel.send("I am married to Jacqueline Bouvier Kennedy.")

    if "excuse me" in message.content:
        await message.channel.send("I am sorry, I am here to serve you.")

    if "alex" in message.content:
        await message.channel.send("Alex is a great citizen.")

    if "birthday" in message.content:
        await message.channel.send("I was born on May 29, 1917.")

    if "assassinated" in message.content:
        await message.channel.send("I was assassinated on November 22, 1963.")

    if "cuban missile crisis" in message.content:
        await message.channel.send("The Cuban Missile Crisis was a 13-day confrontation between the United States and the Soviet Union concerning American ballistic missile deployment in Italy and Turkey with consequent Soviet ballistic missile deployment in Cuba.")

    if "moon" in (message.content).lower():
        await message.channel.send("We choose to go to the Moon in this decade and do the other things, not because they are easy, but because they are hard.")

    if client.user in message.mentions:
        await message.channel.send("America is a nation.")

client.run(os.getenv('TOKEN'))