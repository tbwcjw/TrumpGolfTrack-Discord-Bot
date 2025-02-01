import crawler
import config

import discord
from discord.ext import commands

import time
import datetime
from datetime import datetime

@staticmethod
def log_action(action: str, user: discord.Member):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {user} executed: {action}")

@staticmethod
def log_execution_time(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {func.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

@staticmethod
def countdown():
    current_date = datetime.now()
    return (config.NEXT_INAUGURATION_DATE - current_date).days

class TrumpGolfTrack(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents, timeout=None)
        self.add_commands()

    def add_commands(self):
        @self.event
        async def on_ready():
            await self.tree.sync()
            print(f"Logged in as {self.user.name}")
        
        @self.tree.command(name="track", description="Get statistics about Trumps Golfing activities")
        async def track(interaction: discord.Interaction):
            log_action("/track", interaction.user)
            await self.show_track(interaction)
    
    @log_execution_time
    async def show_track(self, interaction:discord.Interaction):
        await interaction.response.defer()

        trump_golf_track = await crawler.TrumpGolfTrack.fetch()
        embed = discord.Embed(title=f"🏌️ Donald Trump Golf Tracker", color=config.EMBED_COLOR)
        for key, value in trump_golf_track.to_dict().items():
            #put value on new line if length of value is more than the split threshold
            inline = False if len(str(value)) > config.LINE_LENGTH_SPLIT else True
            embed.add_field(name=f"{key}", value=f"```{value}```", inline=inline)

        embed.add_field(name="⌛ Days until next Presidency", value=f"```{countdown()} days```")
        file = discord.File(config.GRAPHS_SAVE_PATH, filename=config.GRAPHS_FILE_NAME)
        embed.set_image(url=f"attachment://{config.GRAPHS_SAVE_PATH}")
        embed.set_footer(text=f"Data provided by {config.URL_PATH}, a nonaffiliate.")

        await interaction.followup.send(embed=embed, file=file, ephemeral=True)

intents = discord.Intents.default()
intents.message_content = True
bot = TrumpGolfTrack(command_prefix="!", intents=intents)
bot.run(config.TOKEN)