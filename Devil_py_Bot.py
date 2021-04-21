import asyncio
import random

import discord
from discord import Member, Guild

client = discord.Client()

antworten = ["Jaツ", "Nein", "Vielleicht", "Wahrscheinlich", "Sieht so aus", "Sehr Wahrscheinlich",
             "Sehr unwahrscheinlich"]

autoroles = {
    770075375010316359: {'memberroles': [778246645359181875], 'botroles': [778676095691259924]},
    542400814476558346: {'memberroles': [], 'botroles': [712695671093723158]},
    797852723545636864: {'memberroles': [811158711288070194], 'botroles': [797852723550617655]},
}

@client.event
async def on_ready():
    print("Der {} ist online".format(client.user.name))
    client.loop.create_task(status_task())


async def status_task():
    colors = [discord.Colour.red(), discord.Colour.orange(), discord.Colour.gold(), discord.Colour.green(),
              discord.Colour.blue(), discord.Colour.purple()]
    while True:
        await client.change_presence(activity=discord.Game(prefix+"help"), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game("Dev: SD_DasBambus#2101"), status=discord.Status.online)
        await asyncio.sleep(5)
        guild: Guild = client.get_guild(797852723545636864)
        if guild:
            role = guild.get_role(819240945785634827)
            if role and role.position < guild.get_member(client.user.id).top_role.position:
                await role.edit(colour=random.choice(colors))
        guild: Guild = client.get_guild(770075375010316359)
        if guild:
            role = guild.get_role(778246645359181875)
            if role and role.position < guild.get_member(client.user.id).top_role.position:
                await role.edit(colour=random.choice(colors))
        guild: Guild = client.get_guild(812269513932406795)
        if guild:
            role = guild.get_role(815966790998818848)
            if role and role.position < guild.get_member(client.user.id).top_role.position:
                await role.edit(colour=random.choice(colors))


def is_not_pinned(mess):
    return not mess.pinned


@client.event
async def on_member_join(member):
    embed_j = discord.Embed(title="Willkommen", description="Wilkommen auf dem Server {}.".format(member.name),
                              color=16711680)
    try:
        if not member.dm_channel:
            await member.create_dm()
        await member.dm_channel.send(embed=embed_j)
    except discord.errors.Forbidden:
        print("Es wurde keine Willkommensnachricht an {} gesendet.".format(member.name))



@client.event
async def on_message(message):
    if message.author.bot:
        return
    "# Die Hilfe"
    if message.content.startswith(prefix + "help"):
        embed_h = discord.Embed(title=prefix+"help", description="**Hilfe für den Devil Bot.**",
                                url="https://devil-bot.jimdosite.com",
                                color=16711680)
        embed_h.set_thumbnail(url="https://emojigraph.org/media/apple/white-question-mark_2754.png")
        embed_h.add_field(name=prefix+"userinfo <Name>:", value="Zeigt die Userinfo von jemanden an.",
                          inline=False)
        embed_h.add_field(name=prefix+"8ball <Frage>:", value="Beantwortet eine Ja/Nein Frage von dir.",
                          inline=False)
        embed_h.add_field(name=prefix+"roulette <Zahl/Farbe>:", value="Roulette spielen.",
                          inline=False)
        embed_h.add_field(name=prefix+"stats-roulette", value="Zeigt an wie oft du in Roulette gewonnen hast.",
                          inline=False)
        embed_h.add_field(name=prefix+"invite:", value="Du erhältst den Einladungslink für den Bot.\r\n",
                          inline=False)
        embed_h.add_field(name="```Für Admins:```", value="Funktioniert nur wenn die Rolle Administratoren Rechte vorhanden sind.",
                          inline=False)
        embed_h.add_field(name=prefix+"clear <Anzahl>:", value="Löscht eine bestimmte Anzahl an Nachrichten.",
                          inline=False)
        embed_h.add_field(name=prefix+"clear all:", value="Löscht alle Nachrichten.",
                          inline=False)
        embed_h.add_field(
            name="**(!!!!ACHTUNG:Wenn zu viele Nachrichten gelöscht werden\r\n könnte der Bot etwas länger brauchen!!!!)**",
            value="Wird noch gefixt.",
            inline=False)
        embed_h.add_field(name="Für die *Regenbogenrolle* schreibt den Developer an.",
                          value="Man braucht dafür die ID vom Server und von der Rolle.",
                          inline=False)
        embed_h.add_field(name="**Für weitere Befehle oder Ideen für Befehle, schreibt *SD_DasBambus#2101* an.**",
                          value="Alle möglichen Ideen werden umgesetzt.",
                          inline=False)
        embed_h.add_field(name="Manuelle Hilfe",
                          value="Manuelle Hilfe bekommst du auf dem [Discord Server](https://discord.gg/QCQTmhTjUT).")
        embed_h.set_footer(text="Developer: SD_DasBambus #2101",
                           icon_url="https://cdn.discordapp.com/attachments/780862968501502002/798172381180461056/02.png")
        message = await message.channel.send(embed=embed_h)
    # Die Userinfo(!!!FUNKTIONIERT NICHT GRUND: UNBEKANNT!!!)
    if message.content.startswith("userinfo"):
        args = message.content.split(" ")
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if Member:
                embed = discord.Embed(title="Userinfo für {}".format(Member.name),
                                      description="Dies ist die Userinfo für {}".format(Member.mention),
                                      color=0x22a7f0)
                await message.channel.send("Hallo")
                embed.add_field(name="Server beigetreten", value=Member.joined_at,
                                inline=True)
                embed.add_field(name="Server beigetreten", value=Member.created_at,
                                inline=True)
                await message.channel.send(embed)
                rollen = ""
                '''for role in Member.roles:
                    if not role.is_default():
                        rollen += "{} \r\n".format(role.mention)
                if rollen:
                    embed.add_field(name="Rollen", value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Das Ende der Userinfo.")'''
                message = await message.channel.send(embed=embed)
                '''await message.add_reaction(":Strong_Devils:529076379602649108")
                await message.add_reaction(":Fire_Devil:557219342039777306")'''
    # Bestimmte Anzahl an Nachrichten clearen
    if message.content.startswith(prefix + "clear"):
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(" ")
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send("{} Nachrichten wurden gelöscht.".format(len(deleted) - 1))
    # 8ball Kugel
    if message.content.startswith(prefix + "8ball"):
        args = message.content.split(" ")
        if len(args) >= 2:
            frage = " ".join(args[1:])
            mess = await message.channel.send("Ich versuche deine Frage `{0}` zu beantworten.".format(frage))
            await asyncio.sleep(3)
            await mess.edit(content="Ich schaue in meine Wahrsager Kugel...")
            await asyncio.sleep(4)
            await mess.edit(content="Die Antwort zu deiner Frage `{0}` lautet: `{1}`".format(frage,
                                                                                             random.choice(antworten)))
    # Alle nachrichten clearen(!Kann zu wenige Nachrichten aufeinmal löschen!)
    if message.content.startswith(prefix + "clear all"):
        if message.author.permissions_in(message.channel).manage_messages:
            deleted = await message.channel.purge(check=is_not_pinned)
            await message.channel.send("Alle Nachrichten wurden gelöscht.".format(len(deleted) - 1))
    # Invite Link
    if message.content.startswith(prefix + "invite"):
        embed_i = discord.Embed(title="Einladungslink",
                                description="[Hier](https://discord.com/api/oauth2/authorize?client_id=709776955989426328&permissions=4294967031&redirect_uri=https%3A%2F%2Fdevil-bot.jimdosite.com%2Fdanke%2F&scope=bot) ist der Einladungslink für den Devil Bot.",
                                color=16711680)
        message = await message.channel.send(embed=embed_i)
    # Roulette Game(!!Noch paar Änderungen vornehmen!!)
    if message.content.startswith(prefix + "roulette"):
        bid = message.content.split(' ')[1]
        bid_param = -3
        if bid.lower() == "black":
            bid_param = -1
        elif bid.lower() == "red":
            bid_param = -2
        else:
            try:
                bid_param = int(bid)
            except:
                bid_param = -3
        if bid_param == -3:
            await message.channel.send('Ungültige Eingabe')
            return
        result = random.randint(0, 36)
        await message.channel.send(result)
        print(result)
        if bid_param == -1:
            won = result % 2 == 0 and not result == 0
        elif bid_param == -2:
            won = result % 2 == 1
        else:
            won = result == bid_param
        if won:
            await message.channel.send('$$$ Du hast gewonnen!!! $$$')
        else:
            await message.channel.send('Du hast leider Verloren.')
    "# Direktnachrichten"
    if message.content.startswith("Hallo"):
        await message.author.send("Hi wie gehts?")
    if message.content.startswith("Hi"):
        await message.author.send("Hi wie gehts?")
    if message.content.startswith("hi"):
        await message.author.send("Hi wie gehts?")
    if message.content.startswith("hallo"):
        await message.author.send("Hi wie gehts?")
    if message.content.startswith("Hey"):
        await message.author.send("Hey wie gehts?")
    if message.content.startswith("hey"):
        await message.author.send("Hey wie gehts?")
    if message.content.startswith("Moin"):
        await message.author.send("Moin Moin wie gehts?")
    if message.content.startswith("moin"):
        await message.author.send("Moin Moin wie gehts?")
    if message.content.startswith("Servus"):
        await message.author.send("Moin Servus Moin.")
    if message.content.startswith("servus"):
        await message.author.send("Moin Servus Moin.")
    # Roulette History
    if message.content.startswith(prefix + "stats-roulette"):
        messages = await message.channel.history(limit=0).flatten()
        for i in messages:
            print(i.content)
        counter = 0
        async for m in message.channel.history():
            if m.author == client.user and m.content == "$$$ Du hast gewonnen!!! $$$":
                counter = counter + 1
        await message.channel.send(counter)
        print(counter)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await self.process_commands(message)

    if message.content.startswith(prefix+"embed"):
        args = message.content.split(' ')
        if len(args) == 2:
            number = '1'.join(args[1:])
            embed_v = discord.Embed(description="Angekommen",
                                    color=16711680)
            message = await message.channel.send(embed=embed_v)
        else:
            embed_u = discord.Embed(description="Ungültige eingabe",
                                    color=16711680)

            message = await message.channel.send(embed=embed_u)


prefix = "/"

client.run("NzA5Nzc2OTU1OTg5NDI2MzI4.Xrq1TQ.IGrCYNXecIeb0CtX1vo52qIfEgA")
