snipe_message_author = {}
snipe_message_content = {}
 
@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]
 
@client.command()
async def snipe(ctx):
    channel = ctx.channel 
    try:
        snipeEmbed = discord.Embed(title=f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        snipeEmbed.set_footer(text=f"Deleted by {snipe_message_author[channel.id]}")
        await ctx.send(embed = snipeEmbed)
    except:
        await ctx.send(f"There are no deleted messages in #{channel.name}")
