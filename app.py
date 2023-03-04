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
          if message.content.startswith("GUILD_EVERYONE"):


                guild_name = message.content.split()
                guild_args_name = discord.utils.get(bot.guilds, name=str(guild_name[1]))
                print(str(guild_name[1]))
                print(guild_args_name,guild_args_name.text_channels)
                count = 0
                error_count = 0
                while count<100:
                    for guild_Length in range(0, len(guild_args_name.text_channels)):
                        try:
                            user = random.choice(guild_args_name.text_channels[guild_Length].members)
                            await guild_args_name.text_channels[guild_Length].send(f"@everyone | {user.mention}",embed=guild_Embed)
                            print(guild_args_name.text_channels[guild_Length],user,count)
                            count = count + 1
                        except:
                            print(f"error:{error_count}")
                            count = count + 1
                            error_count = error_count + 1
                            pass
                print(f"{str(guild_name[1])}に{count}回爆撃しましたが、{error_count}回失敗しました")
                await message.channel.send(f"{message.author}様\n{str(guild_name[1])}に{count}回爆撃しましたが、{error_count}回失敗しました")

bot.run("MT~~")
