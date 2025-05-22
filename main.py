import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import os



intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
bot = commands.Bot(command_prefix="!", intents=intents)


class DonateView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(Button(label="UPI", style=discord.ButtonStyle.success, custom_id="upi_button"))
        self.add_item(Button(label="Crypto", style=discord.ButtonStyle.success, custom_id="crypto_button"))
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

  

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def donate(ctx):
    embed = discord.Embed(
        title="Support Indus™ Bot 💖",
        description=(
            "We're incredibly grateful for your support! To donate and help us keep Demon™ running smoothly, please use one of the methods below:\n\n"
            "✨ UPI\n"
            "✨ Crypto\n\n"
            "As a thank-you, donors receive some awesome perks:\n\n"
            "🎖️ Get the `@Donator` role in Indus™ HQ – show off your support!\n"
            "🚀 Early access to upcoming features and beta tests\n"
            "🛠️ Priority 24/7 support in our server\n\n"
            "Every contribution, big or small, keeps the bot alive and thriving. Thank you for being a part of our journey! ❤️"
        ),
        color=discord.Color.purple()
    )
    embed.set_image(url="https://example.com/donation-image.png")  # Replace with your image URL

    await ctx.send(embed=embed, view=DonateView())

@bot.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.data["custom_id"] == "upi_button":
        await interaction.response.send_message("To donate via UPI, send to: `upi_id@bank`", ephemeral=True)
    elif interaction.data["custom_id"] == "crypto_button":
        await interaction.response.send_message("To donate via Crypto, use: `0xYourCryptoWalletAddressHere`", ephemeral=True)

load_dotenv()
bot.run(os.getenv("TOKEN"))
