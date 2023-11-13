import json
import os
import requests

def lambda_handler(event, context):
    # Parse the incoming JSON payload
    payload = json.loads(event['body'])

    # Check if the payload contains an 'issue' key
    if 'issue' in payload:
        issue_url = payload['issue']['html_url']
        message = f"Issue Created: {issue_url}"

        # Prepare the message for Slack
        slack_payload = {'text': message}
        slack_webhook_url = os.environ.get('SLACK_URL')

        # Send the message to Slack
        response = requests.post(slack_webhook_url, json=slack_payload)

        return {
            'statusCode': 200,
            'body': json.dumps('Message sent to Slack')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('No issue data in payload')
        }
