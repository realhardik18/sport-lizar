import time
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from dataGetter import get_commentary, get_overs, get_toss_result, get_score
from classes import class_commentary, class_for_toss, class_overs, class_score
from matchinfo import location, title, match_url

with open('webhooks.json', 'r') as f:
    webhook_urls = json.load(f)['webhooks']

webhook = DiscordWebhook(url=webhook_urls)

embed = DiscordEmbed(title=title,
                     description=f'LIVE at {location}', color='03b2f8')
overs = get_overs(url=match_url, class_for_overs=class_overs)
embed.add_embed_field(
    name='Score', value=f'{get_score(url=match_url,class_for_score=class_score)} at {get_overs(url=match_url,class_for_overs=class_overs)}')
embed.add_embed_field(name='Ball by ball commentary', value=get_commentary(
    url=match_url, class_for_commentary_cards=class_commentary))
embed.set_footer(text=get_toss_result(
    url=match_url, class_for_toss=class_for_toss))
webhook.add_embed(embed=embed)
sent_webhook = webhook.execute()

while True:
    if overs != get_overs(url=match_url, class_for_overs=class_overs):
        overs = get_overs(url=match_url, class_for_overs=class_overs)
        webhook = DiscordWebhook(url=webhook_urls)

        embed = DiscordEmbed(title=title,
                             description=f'LIVE at {location}', color='03b2f8')
        overs = get_overs(url=match_url, class_for_overs=class_overs)
        embed.add_embed_field(
            name='Score', value=f'{get_score(url=match_url,class_for_score=class_score)} at {get_overs(url=match_url,class_for_overs=class_overs)}')
        embed.add_embed_field(name='Ball by ball commentary', value=get_commentary(
            url=match_url, class_for_commentary_cards=class_commentary))
        embed.set_footer(text=get_toss_result(
            url=match_url, class_for_toss=class_for_toss))
        webhook.add_embed(embed=embed)
        sent_webhook = webhook.edit(sent_webhook)
        print('sent webhook')
    else:
        print('no')
    time.sleep(2)
