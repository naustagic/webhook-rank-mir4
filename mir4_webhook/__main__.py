"""Handles the main logic for this webhook script"""
import datetime

from discord_webhook import DiscordEmbed

from mir4_webhook.client import MirAPI
from mir4_webhook.objects import Guild
from mir4_webhook.webhook import send_webhook

"""Configuration"""
webhook_url: str = ""
username: str = "Testing a Webhook"
role: int = 123456  # ID for the role to ping when the embed is sent
today = datetime.datetime.now().strftime("%d/%m | %H:%M")


def build_embed(guild: Guild) -> DiscordEmbed:
    """Creates the embed from the guild object"""
    roster = "\n".join(
        [
            f"**{i}. - {player.name} ({player.player_class.name} {player.power})**"
            for i, player in enumerate(guild.roster, 1)
        ]
    )
    embed = DiscordEmbed(
        title=f"[SA2/SA62] -- {today}",
        description=f"""**Name: {guild.name}**
**Characters: {guild.characters}**
**Power: {guild.power}**
**Warriors: {guild.warriors}**
**Sorcerers: {guild.sorcerers}**
**Taoists: {guild.taoists}**
**Arbalists: {guild.arbalists}**
**Lancers: {guild.lancers}**

{roster}""",
    )

    return embed


def main():
    """Handles all the main functions of this webhook"""

    # instantiate a new webhook client and make the request
    api = MirAPI("32")  # "https://api.mir4.gq/v1/clan/52289808/roster/{}"
    guild = api.request()

    embed = build_embed(guild)
    send_webhook(url=webhook_url, content=f"<@&{role}>", embed=embed, username=username)


if __name__ == "__main__":
    main()
