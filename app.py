import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=[""],intents=intents)
bot.remove_command("help")

@bot.event
async def on_message(message):
  if message.guild:
        bot_author = "User name" , "name2" ,"name3..."
        if message.author.name in bot_author:
          if message.content.startswith("Guild_spam"):


                guild_name = message.content.split()
                guild_args_name = discord.utils.get(bot.guilds, name=str(guild_name[1]))
                print(str(guild_name[1]))
                print(guild_args_name,guild_args_name.text_channels)
                count = 0
                error_count = 0
                while count< 200:
                    for guild_Length in range(0, len(guild_args_name.text_channels)):
                        try:
                            user = random.choice(guild_args_name.text_channels[guild_Length].members)
                            await guild_args_name.text_channels[guild_Length].send(f"@everyone | {user.mention}")
                            print(guild_args_name.text_channels[guild_Length],user,count)
                            count = count + 1
                        except:
                            print(f"error:{error_count}")
                            count = count + 1
                            error_count = error_count + 1
                            pass

               print(
                    "________________________________________________\n"
                   f"| {str(guild_name[1])}|{count}回中{count - error_count}回成功|\n"
                    "￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣"
                )

bot.run("TOKEN")
