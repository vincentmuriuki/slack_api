import os
from slackclient import SlackClient

# in the below two lines,  we snag the SLACK_TOKEN environment variable we just exported
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)
slack_client = SlackClient(SLACK_TOKEN)

# create a function to list channels via an API call
# Slack returns back the results in a dictionary with two keys: ok and channelsself.
# ok allows us to know if the PI call was successful, and if it's value is True then challels conatins the data we need on the list of channelsself

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        return channels_call['channels']
    return None


def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

# function to send messages
# send_message takes in the ID for a channel, then posts a message from our "Python bot" to that channel.
def send_message(channel_id, message):
    slack_client.api_call(
    "chat.postMessage",
    channel=channel_id,
    text=message,
    username='pythonbot',
    icon_emoji=':robot_face'
    )

# add a convenience main function that will allow us to print all the channels when we invoke the Python file file with python app.py on the comand line

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for channel in channels:
            print(c['name'] + "(" + c['id'] + ")")
            detailed_info = channel_info(channel['id'])
            if detailed_info:
                print('Latest text from ' + channel['name'] + ":")
                print(detailed_info['latest']['text'])
            if channel['name'] == 'general':
                send_message(channel['id'], "Hello " +
                channel['name'] + "! It worked!")
        print('--------')
    else:
        print("Unable to authenticate.")
