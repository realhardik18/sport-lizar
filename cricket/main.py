import time
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from dataGetter import get_commentary, get_overs, get_toss_result, get_score, get_score_from_title_of_site
from classes import class_commentary, class_for_toss, class_overs, class_score
from matchinfo import location, title, match_url
from webhooksender import send_webhook
with open('webhooks.json', 'r') as f:
    webhook_urls = json.load(f)['webhooks']

send_webhook(webhooks=webhook_urls)
overs = get_overs(url=match_url, class_for_overs=class_overs)

while True:
    if overs != get_overs(url=match_url, class_for_overs=class_overs):
        overs = get_overs(url=match_url, class_for_overs=class_overs)
        #sent_webhook = webhook.edit(sent_webhook)
        send_webhook(webhook_urls)
        print('sent webhook')
    else:
        print(overs)
    time.sleep(2)
