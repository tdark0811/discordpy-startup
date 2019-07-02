from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

import discord

client = discord.Client()

@client.event
async def on(message):
    """メンバー募集 (.rect@数字)"""
    if message.content.startswith(".rect"):
        mcount = int(content[6:len(content)])
        text= "あと{}人 募集中\n"
        revmsg = text.format(mcount)
        #friend_list 押した人のList
        frelist = []
        msg = await client.send(channel, revmsg)

        #投票の欄
        await client.add('\u21a9')
        await client.add('⏫')
        await client.pin(msg)

        #リアクションをチェックする
        while len(frelist) < int(content[6:len(content)]):
            target_reaction = await client.wait_for_reaction(message=msg)
            #発言したユーザが同一でない場合 真
            if target_reaction.user != msg.author:
                #==============================================================
                #押された絵文字が既存のものの場合 >> 左　del
                if target_reaction.reaction.emoji == '\u21a9':
                    #==========================================================
                    #◀のリアクションに追加があったら反応 frelistにuser.nameがあった場合　真
                    if target_reaction.user.name in frelist:
                        frelist.remove(target_reaction.user.name)
                        mcount += 1
                        #リストから名前削除
                        await client.edit(text.format(mcount) +
                                                        '\n'.join(frelist))
                            #メッセージを書き換え

                    else:
                        pass
                #==============================================================
                #押された絵文字が既存のものの場合　>> 右　add
                elif target_reaction.reaction.emoji == '⏫':
                    if target_reaction.user.name in frelist:
                        pass

                    else:
                        frelist.append(target_reaction.user.name)
                        #リストに名前追加
                        mcount = mcount - 1
                        await client.edit(text.format(mcount) +
                                                        '\n'.join(frelist))


                elif target_reaction.reaction.emoji == '✖':
                        await client.edit('募集終了\n'+ '\n'.join(frelist))
                        await client.unpin(msg)
                        break
                await client.remove(target_reaction.reaction.emoji, target_reaction.user)
                #ユーザーがつけたリアクションを消す※権限によってはエラー
                #==============================================================
        else:
            await client.edit('募集終了\n'+ '\n'.join(frelist))



client.run("NTk1NjQ5NjU2OTExMDM2NDE2.XRuEYQ.XQ5u8CZp5pyS0CVTfa6nb6V9P6E")

bot.run(token)
