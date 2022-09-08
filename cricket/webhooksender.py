from matchinfo import match_url, title, location
from discord_webhook import DiscordEmbed, DiscordWebhook
from classes import class_commentary, class_overs, class_for_toss
from dataGetter import get_commentary, get_overs, get_score_from_title_of_site, get_toss_result


def send_webhook(webhooks):
    webhook = DiscordWebhook(url=webhooks)

    embed = DiscordEmbed(title=title,
                         description=f'LIVE at {location}', color='03b2f8')
    overs = get_overs(url=match_url, class_for_overs=class_overs)
    #embed.add_embed_field(name='Score', value=f'{get_score(url=match_url,class_for_score=class_score)} at {get_overs(url=match_url,class_for_overs=class_overs)}')
    embed.add_embed_field(
        name='Score', value=f'{get_score_from_title_of_site(url=match_url)} at {get_overs(url=match_url,class_for_overs=class_overs)}')
    embed.add_embed_field(name='Ball by ball commentary', value=get_commentary(
        url=match_url, class_for_commentary_cards=class_commentary))
    embed.set_footer(text=get_toss_result(
        url=match_url, class_for_toss=class_for_toss))
    webhook.add_embed(embed=embed)
    webhook.execute()
