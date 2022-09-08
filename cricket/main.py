import json

with open('webhooks.json', 'r') as f:
    webhooks = json.load(f)['webhooks']

for webhook in webhooks:
    print(webhook)
