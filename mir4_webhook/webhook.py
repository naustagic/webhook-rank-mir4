from discord_webhook import DiscordEmbed, DiscordWebhook


def send_webhook(url: str, content: str, embed: DiscordEmbed, username: str) -> None:
    """Sends the content and embed to the webhook url"""

    webhook = DiscordWebhook(url=url, content=content, username=username)
    webhook.add_embed(embed)

    # print(webhook.embeds)
    webhook.execute()
