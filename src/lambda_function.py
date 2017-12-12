import json
import os
import slackweb

print('Loading function')

def lambda_handler(event, context):
    url = os.getenv("SLACKURL", None)
    if url is None: exit(1)

    imageurl = os.getenv("IMAGEURL", None)
    if imageurl is None: exit(1)

    print("Received event: " + json.dumps(event, indent=2))

    channel = os.getenv("CHANNEL", "#sns")
    name = os.getenv("NAME", "Gyazo")
    slack = slackweb.Slack(url=url)
    key = event['Records'][0]['s3']['object']['key']
    message = imageurl + '/' + key

    slack.notify(channel=channel,
                 username=name,
                 text=message
    )

    return message
